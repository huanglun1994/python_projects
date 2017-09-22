# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from wea_web.models import Weather


class MyspiderItem(scrapy.Item):
    pass


class WeatherItem(DjangoItem):
    django_model = Weather
