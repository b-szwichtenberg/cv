from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from .models import Gra


def test_f(request):
    #return HttpResponse("pierwszy TEST")
    #return render(request,'gry.html',{ 'gry': ["GTA 2", "Gothic"] })
    napis = "Witaj na stronie glownej"

    #wszystkie_gry = Gra.objects.all()
    #ile = Gra.objects.all().count()
    #return render(request,'index.html',{ 'napis' :napis, 'gry': wszystkie_gry, 'ile1': ile })
    return render(request, 'index.html',{'napis':napis})
