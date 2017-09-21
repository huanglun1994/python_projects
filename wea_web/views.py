from django.shortcuts import render
from wea_web.models import Weather


def index(request):
    weather = Weather.objects.all()
    context = {'weather': weather}
    return render(request, 'index.html', context=context)
