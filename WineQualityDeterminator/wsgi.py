"""
WSGI config for WineQualityDeterminator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from winequality.wine_quality_determinator import WineQualityDeterminator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WineQualityDeterminator.settings')

WineQualityDeterminator.train()

application = get_wsgi_application()
