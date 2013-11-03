import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "djangosnippets.settings.production")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
