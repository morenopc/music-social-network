#!/usr/bin/python
# -*- coding: UTF8 -*-
from django import forms
from math_captcha.forms import MathCaptchaForm

class VoteForm(MathCaptchaForm):
    video_id=forms.CharField(required=True, widget=forms.widgets.HiddenInput())
