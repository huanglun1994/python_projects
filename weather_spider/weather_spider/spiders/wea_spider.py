# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import scrapy
from weather_spider.weather_spider.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather/101270101.shtml']

    def parse(self, response):
        for sel in response.xpath('//div[@id="7d"]/ul/li'):
            item = WeatherItem()
            item['day'] = sel.xpath('h1/text()').extract_first().strip()
            item['weather'] = sel.xpath('p[@class="wea"]/text()').extract_first().strip()
            item['tem_max'] = sel.xpath('p[@class="tem"]/span/text()').extract_first.strip()
            item['tem_min'] = sel.xpath('p[@class="tem"]/i/text()').extract_first.strip().split('℃')[0]
            item['wind'] = sel.xpath('p[@class="win"]/i/text()').extract_first.strip()
            item.save()
