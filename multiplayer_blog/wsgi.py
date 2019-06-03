"""
WSGI config for multiplayer_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile=os.environ.get('MULTIPLAYER_BLOG_PROFILE','develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multiplayer_blog.settings.%s"%profile)

application = get_wsgi_application()
