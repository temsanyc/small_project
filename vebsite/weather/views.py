from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import CityForm

def index(request):

    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=4a2c26313607dc81c687227b179c1e82"

    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
        return HttpResponseRedirect(request.path)

    form=CityForm
    cities= City.objects.all()
    all_cities=[]
    for city in cities:
        res=requests.get(url.format(city.name)).json()

        city_info={
        'id': city.id,
        'city':city.name,
        'temp':res["main"]["temp"],
        'icon':res['weather'][0]['icon']
        }

        all_cities.append(city_info)
    context={'all_info':all_cities,
             'form':form}
    return render(request,'weather/index.html',context)
# Create your views here.

def delete_city(request,pk):

    model=City.objects.get(pk=pk)
    context = {'models': model}
    if request.method=='POST':

        model.delete()
        return redirect('weather')
    return render(request,'weather/delete.html',context)




