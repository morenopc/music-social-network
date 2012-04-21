import re

from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

hex_color_code_re = re.compile(r'([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})')
hex_color_code_validator = RegexValidator(hex_color_code_re, _(u"Enter a valid hex color code."), 'invalid')