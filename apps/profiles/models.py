#!/usr/bin/python
# -*- coding: UTF8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from timezones.fields import TimeZoneField

# Me
ESTADOS=(
    ('AC','AC'),
    ('AL','AL'),
    ('AM','AM'),
    ('AP','AP'),
    ('BA','BA'),
    ('CE','CE'),
    ('DF','DF'),
    ('ES','ES'),
    ('GO','GO'),
    ('MA','MA'),
    ('MG','MG'),
    ('MS','MS'),
    ('MT','MT'),
    ('PA','PA'),
    ('PB','PB'),
    ('PE','PE'),
    ('PI','PI'),
    ('PR','PR'),
    ('RJ','RJ'),
    ('RN','RN'),
    ('RO','RO'),
    ('RR','RR'),
    ('RS','RS'),
    ('SC','SC'),
    ('SE','SE'),
    ('SP','SP'),
    ('TO','TO'),
)
class ListaEstados(models.Model):
    lestados=models.CharField(max_length=2, choices=ESTADOS)
    def __unicode__(self):
        return self.lestados

class Profile(models.Model):
    
    user = models.ForeignKey(User, unique=True, verbose_name=_("user"))
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"),
        max_length = 40,
        null = True,
        blank = True
    )
    # Me
    estado=models.ForeignKey(ListaEstados, verbose_name=_('Estado'), null=True, blank=True)
    
    website = models.URLField(_("website"),
        null = True,
        blank = True,
        verify_exists = False
    )
    
    # Me
    nartistico=models.CharField(_(u'Nome artístico'), max_length=56, null=True, blank=True)
    data_nascimento=models.DateField(null=True, blank=True)
    orkut=models.URLField(blank=True, null=True, verify_exists=False)
    twitter=models.URLField(blank=True, null=True, verify_exists=False)
    facebook=models.URLField(blank=True, null=True, verify_exists=False)
    data_criacao=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={
            "username": self.user.username
        })


def create_profile(sender, instance=None, **kwargs):
    if instance is None:
        return
    profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_profile, sender=User)
