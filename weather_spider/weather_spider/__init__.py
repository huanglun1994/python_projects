import sys
sys.path.append('../../django_scrapy')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_scrapy.settings")
import django
django.setup()
