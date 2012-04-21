# pinax.wsgi is configured to live in projects/dev/deploy.

import os
import sys

from os.path import abspath, dirname, join
from site import addsitedir

sys.path.append('/home/webtalentos/apps_wsgi')
#sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "dev.settings"

#sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
sys.path.append('/home/webtalentos/pinax/pinax-env/lib/python2.4/site-packages')

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
