from django.shortcuts import render
from wea_web.models import Weather


def index(request):
    pk = Weather.objects.last().id
    weather = Weather.objects.all()[pk-7:]
    context = {'weather': weather}
    return render(request, 'index.html', context=context)
