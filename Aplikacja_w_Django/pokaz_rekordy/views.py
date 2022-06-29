from gc import get_objects
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Gra
from .models import Adres
from .models import Wydawca
from .models import Producent
from .models import Gatunek
from .models import Gra_gatunek
from .models import Polka
from .models import Gra_polka
from .formularz import GraFormularz
from .formularz import AdresFormularz
from .formularz import WydawcaFormularz
from .formularz import ProducentFormularz
from .formularz import GatunekFormularz
from .formularz import Gra_gatunekFormularz
from .formularz import PolkaFormularz
from .formularz import Gra_polkaFormularz
# Create your views here.


#######Gra
def f_pokaz_rekordy(request):
    wszystkie_gry = Gra.objects.all()
    return render(request, 'pokaz_rekordy.html', {'all_games':wszystkie_gry})

def f_dodaj_rekord(request):
    formularz = GraFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_rekordy)
    return render(request,'nowy_rekord.html',{'form':formularz})

def f_edycja_rekordu(request,id):
    pobrane_id = get_object_or_404(Gra,pk=id)
    formularz = GraFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_rekordy)
    return render(request,'edytuj_rekord.html',{'form':formularz})

def f_usuniecie_rekordu(request,id):
    pobrane_id = get_object_or_404(Gra,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_rekordy)
    return render(request,'usun_rekord.html',{'id_gry':pobrane_id})



###########Adres
def f_pokaz_adres(request):
    wszystkie_adresy = Adres.objects.all()
    return render(request, 'pokaz_adresy.html', {'all_addresses':wszystkie_adresy})

def f_dodaj_adres(request):
    formularz = AdresFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_adres)
    return render(request,'nowy_adres.html',{'form':formularz})

def f_edycja_adresu(request,id):
    pobrane_id = get_object_or_404(Adres,pk=id)
    formularz = AdresFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_adres)
    return render(request,'edytuj_adres.html',{'form':formularz})

def f_usuniecie_adresu(request,id):
    pobrane_id = get_object_or_404(Adres,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_adres)
    return render(request,'usun_adres.html',{'id_adresu':pobrane_id})



#################Wydawca
def f_pokaz_wydawca(request):
    wszyscy_wydawcy = Wydawca.objects.all()
    return render(request, 'pokaz_wydawca.html', {'all_publisher':wszyscy_wydawcy})

def f_dodaj_wydawca(request):
    formularz = WydawcaFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_wydawca)
    return render(request,'nowy_wydawca.html',{'form':formularz})

def f_edycja_wydawca(request,id):
    pobrane_id = get_object_or_404(Wydawca,pk=id)
    formularz = WydawcaFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_wydawca)
    return render(request,'edytuj_wydawca.html',{'form':formularz})

def f_usuniecie_wydawca(request,id):
    pobrane_id = get_object_or_404(Wydawca,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_wydawca)
    return render(request,'usun_wydawca.html',{'id_wydawcy':pobrane_id})



##################Producent
def f_pokaz_producent(request):
    wszyscy_producenci = Producent.objects.all()
    return render(request, 'pokaz_producent.html', {'all_developers':wszyscy_producenci})

def f_dodaj_producent(request):
    formularz = ProducentFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_producent)
    return render(request,'nowy_producent.html',{'form':formularz})

def f_edycja_producent(request,id):
    pobrane_id = get_object_or_404(Producent,pk=id)
    formularz = ProducentFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_producent)
    return render(request,'edytuj_producent.html',{'form':formularz})

def f_usuniecie_producent(request,id):
    pobrane_id = get_object_or_404(Producent,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_producent)
    return render(request,'usun_producent.html',{'id_producenta':pobrane_id})



#######################Gatunek
def f_pokaz_gatunek(request):
    wszystkie_gatunki = Gatunek.objects.all()
    return render(request, 'pokaz_gatunek.html', {'all_genres':wszystkie_gatunki})

def f_dodaj_gatunek(request):
    formularz = GatunekFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_gatunek)
    return render(request,'nowy_gatunek.html',{'form':formularz})

def f_edycja_gatunek(request,id):
    pobrane_id = get_object_or_404(Gatunek,pk=id)
    formularz = GatunekFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_gatunek)
    return render(request,'edytuj_gatunek.html',{'form':formularz})

def f_usuniecie_gatunek(request,id):
    pobrane_id = get_object_or_404(Gatunek,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_gatunek)
    return render(request,'usun_gatunek.html',{'id_gatunku':pobrane_id})



###################Gra_gatunek
def f_pokaz_gra_gatunek(request):
    wszystkie_gryIgatunki = Gra_gatunek.objects.all()
    return render(request, 'pokaz_gra_gatunek.html', {'all_games_genres':wszystkie_gryIgatunki})

def f_dodaj_gra_gatunek(request):
    formularz = Gra_gatunekFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_gra_gatunek)
    return render(request,'nowy_gra_gatunek.html',{'form':formularz})

def f_edycja_gra_gatunek(request,id):
    pobrane_id = get_object_or_404(Gra_gatunek,pk=id)
    formularz = Gra_gatunekFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_gra_gatunek)
    return render(request,'edytuj_gra_gatunek.html',{'form':formularz})

def f_usuniecie_gra_gatunek(request,id):
    pobrane_id = get_object_or_404(Gra_gatunek,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_gra_gatunek)
    return render(request,'usun_gra_gatunek.html',{'id_gra_gatunek':pobrane_id})



#################Półka
def f_pokaz_polka(request):
    wszystkie_polki = Polka.objects.all()
    return render(request, 'pokaz_polka.html', {'all_shelves':wszystkie_polki})

def f_dodaj_polka(request):
    formularz = PolkaFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_polka)
    return render(request,'nowa_polka.html',{'form':formularz})

def f_edycja_polka(request,id):
    pobrane_id = get_object_or_404(Polka,pk=id)
    formularz = PolkaFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_polka)
    return render(request,'edytuj_polka.html',{'form':formularz})

def f_usuniecie_polka(request,id):
    pobrane_id = get_object_or_404(Polka,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_polka)
    return render(request,'usun_polka.html',{'id_polki':pobrane_id})



#Gra_polka
def f_pokaz_gra_polka(request):
    wszystkie_gryIpolki = Gra_polka.objects.all()
    return render(request, 'pokaz_gra_polka.html', {'all_games_shelves':wszystkie_gryIpolki})

def f_dodaj_gra_polka(request):
    formularz = Gra_polkaFormularz(request.POST or None)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_gra_polka)
    return render(request,'nowa_gra_polka.html',{'form':formularz})

def f_edycja_gra_polka(request,id):
    pobrane_id = get_object_or_404(Gra_polka,pk=id)
    formularz = Gra_polkaFormularz(request.POST or None, instance=pobrane_id)
    if formularz.is_valid():
        formularz.save()
        return redirect(f_pokaz_gra_polka)
    return render(request,'edytuj_gra_polka.html',{'form':formularz})

def f_usuniecie_gra_polka(request,id):
    pobrane_id = get_object_or_404(Gra_polka,pk=id)
    if request.method == "POST":
        pobrane_id.delete()
        return redirect(f_pokaz_gra_polka)
    return render(request,'usun_gra_polka.html',{'id_gryIpolki':pobrane_id})