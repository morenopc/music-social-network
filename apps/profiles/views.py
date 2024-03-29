from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from avatar.templatetags.avatar_tags import avatar
from friends.forms import InviteFriendForm
from friends.models import FriendshipInvitation, Friendship
from microblogging.models import Following

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None


from pinax.apps.profiles.forms import ProfileForm
from pinax.apps.profiles.models import Profile



def profiles(request, template_name="profiles/profiles.html", extra_context=None):
    if extra_context is None:
        extra_context = {}
    users = User.objects.all().order_by("-date_joined")
    search_terms = request.GET.get("search", "")
    order = request.GET.get("order")
    if not order:
        order = "date"
    if search_terms:
        users = users.filter(username__icontains=search_terms)
    if order == "date":
        users = users.order_by("-date_joined")
    elif order == "name":
        users = users.order_by("username")
    return render_to_response(template_name, dict({
        "users": users,
        "order": order,
        "search_terms": search_terms,
    }, **extra_context), context_instance=RequestContext(request))


def profile(request, username, template_name="profiles/profile.html", extra_context=None):
    
    if extra_context is None:
        extra_context = {}
    
    other_user = get_object_or_404(User, username=username)
    
    if request.user.is_authenticated():
        is_friend = Friendship.objects.are_friends(request.user, other_user)
        is_following = Following.objects.is_following(request.user, other_user)
        other_friends = Friendship.objects.friends_for_user(other_user)
        if request.user == other_user:
            is_me = True
        else:
            is_me = False
    else:
        other_friends = []
        is_friend = False
        is_me = False
        is_following = False
    
    if is_friend:
        invite_form = None
        previous_invitations_to = None
        previous_invitations_from = None
        if request.method == "POST":
            if request.POST.get("action") == "remove": # @@@ perhaps the form should just post to friends and be redirected here
                Friendship.objects.remove(request.user, other_user)
                messages.add_message(request, messages.SUCCESS,
                    ugettext("You have removed %(from_user)s from friends") % {
                        "from_user": other_user
                    }
                )
                is_friend = False
                invite_form = InviteFriendForm(request.user, {
                    "to_user": username,
                    "message": ugettext("Let's be friends!"),
                })
    
    else:
        if request.user.is_authenticated() and request.method == "POST":
            if request.POST.get("action") == "invite": # @@@ perhaps the form should just post to friends and be redirected here
                invite_form = InviteFriendForm(request.user, request.POST)
                if invite_form.is_valid():
                    invite_form.save()
            else:
                invite_form = InviteFriendForm(request.user, {
                    "to_user": username,
                    "message": ugettext("Let's be friends!"),
                })
                invitation_id = request.POST.get("invitation", None)
                if request.POST.get("action") == "accept": # @@@ perhaps the form should just post to friends and be redirected here
                    try:
                        invitation = FriendshipInvitation.objects.get(id=invitation_id)
                        if invitation.to_user == request.user:
                            invitation.accept()
                            messages.add_message(request, messages.SUCCESS,
                                ugettext("You have accepted the friendship request from %(from_user)s") % {
                                    "from_user": invitation.from_user
                                }
                            )
                            is_friend = True
                            other_friends = Friendship.objects.friends_for_user(other_user)
                    except FriendshipInvitation.DoesNotExist:
                        pass
                elif request.POST.get("action") == "decline": # @@@ perhaps the form should just post to friends and be redirected here
                    try:
                        invitation = FriendshipInvitation.objects.get(id=invitation_id)
                        if invitation.to_user == request.user:
                            invitation.decline()
                            messages.add_message(request, messages.SUCCESS,
                                ugettext("You have declined the friendship request from %(from_user)s") % {
                                    "from_user": invitation.from_user
                                }
                            )
                            other_friends = Friendship.objects.friends_for_user(other_user)
                    except FriendshipInvitation.DoesNotExist:
                        pass
        else:
            invite_form = InviteFriendForm(request.user, {
                "to_user": username,
                "message": ugettext("Let's be friends!"),
            })
    
    # Me
    user_auth=request.user.is_authenticated()
    if user_auth:
        previous_invitations_from=FriendshipInvitation.objects.invitations(to_user=request.user, from_user=other_user)
        previous_invitations_to = FriendshipInvitation.objects.invitations(to_user=other_user, from_user=request.user)
    else:
        previous_invitations_from=user_auth
        previous_invitations_to = user_auth
    
    return render_to_response(template_name, dict({
        "is_me": is_me,
        "is_friend": is_friend,
        "is_following": is_following,
        "other_user": other_user,
        "other_friends": other_friends,
        "invite_form": invite_form,
        "previous_invitations_to": previous_invitations_to,
        "previous_invitations_from": previous_invitations_from,
    }, **extra_context), context_instance=RequestContext(request))


@login_required
def profile_edit(request, form_class=ProfileForm, **kwargs):
    
    template_name = kwargs.get("template_name", "profiles/profile_edit.html")
    
    if request.is_ajax():
        template_name = kwargs.get(
            "template_name_facebox",
            "profiles/profile_edit_facebox.html"
        )
    
    profile = request.user.get_profile()
    
    if request.method == "POST":
        profile_form = form_class(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.add_message(request, messages.SUCCESS, ugettext("Your profile has been updated."))
            return HttpResponseRedirect(reverse("profile_detail", args=[request.user.username]))
    else:
        profile_form = form_class(instance=profile)
    
    return render_to_response(template_name, {
        "profile": profile,
        "profile_form": profile_form,
    }, context_instance=RequestContext(request))
