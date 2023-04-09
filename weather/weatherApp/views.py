import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid ='8851d16583808fe99692c907e3c3b372'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_ifo = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }

        all_cities.clear()
        all_cities.append(city_ifo)


    context = {'all_info': all_cities, 'form': form}


    return render(request, 'weatherApp/index.html', context)
