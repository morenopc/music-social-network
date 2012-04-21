# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.utils.text import capfirst

from colors.widgets import ColorPickerWidget
from colors.validators import hex_color_code_validator

class ColorField(models.CharField):
	default_validators = [hex_color_code_validator]
	
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 6
		super(ColorField, self).__init__(*args, **kwargs)
		
	def formfield(self, **kwargs):
		kwargs['widget'] = ColorPickerWidget(attrs={'autocomplete': 'off'})
		return super(ColorField, self).formfield(**kwargs)