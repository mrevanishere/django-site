"""
WSGI config for mrevanishere_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/mrevanishere-site/')
sys.path.append('/var/www/mrevanishere-site/mrevanishere_site')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrevanishere_site.settings')

application = get_wsgi_application()
