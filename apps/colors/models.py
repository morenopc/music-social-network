from django.db import models
from django.utils.translation import ugettext as _

from colors.fields import ColorField

class Color(models.Model):
	"""
	A unique color in the color library
	"""
	name = models.CharField(max_length=15, help_text="Provide a descriptive name for the color.")
	color = ColorField(unique=True, help_text="Click the input field to open the color picker.")
	#classification = models.CharField(max_length=15, choices=COLOR_NAME_CHOICES, editable=False)
	
	def __unicode__(self):
		return self.name


class ColorGroup(models.Model):
	"""
	A named group of colors, e.g. 'Black & White' which contains
	the FFF and 000 hex colors
	"""
	name = models.CharField(max_length=25, help_text="Provide a descriptive name for the color group.")
	colors = models.ManyToManyField("Color", related_name="color_groups")

	def __unicode__(self):
		return self.name