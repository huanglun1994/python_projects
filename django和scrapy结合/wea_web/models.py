from django.db import models


class Weather(models.Model):
    date = models.CharField('时间', max_length=50)  # 例如19日（今天）
    weather = models.CharField('天气状况', max_length=50)  # 例如多云
    tem_max = models.IntegerField('最高温度')  # 最高气温
    tem_min = models.IntegerField('最低温度')  # 最低气温
    wind = models.CharField('风力', max_length=50)  # 风力

    def __str__(self):
        return '{0}的天气状况是{1}，温度范围为{2}~{3}，风力为{4}。'.format(
            self.date, self.weather, self.tem_min, self.tem_max, self.wind
        )  # 默认显示
