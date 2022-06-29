"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from aplikacja.views import test_f
from pokaz_rekordy.views import f_pokaz_rekordy
from pokaz_rekordy.views import f_dodaj_rekord
from pokaz_rekordy.views import f_edycja_rekordu
from pokaz_rekordy.views import f_usuniecie_rekordu
from pokaz_rekordy.views import f_pokaz_adres
from pokaz_rekordy.views import f_dodaj_adres
from pokaz_rekordy.views import f_edycja_adresu
from pokaz_rekordy.views import f_usuniecie_adresu
from pokaz_rekordy.views import f_pokaz_wydawca
from pokaz_rekordy.views import f_dodaj_wydawca
from pokaz_rekordy.views import f_edycja_wydawca
from pokaz_rekordy.views import f_usuniecie_wydawca
from pokaz_rekordy.views import f_pokaz_producent
from pokaz_rekordy.views import f_dodaj_producent
from pokaz_rekordy.views import f_edycja_producent
from pokaz_rekordy.views import f_usuniecie_producent
from pokaz_rekordy.views import f_pokaz_gatunek
from pokaz_rekordy.views import f_dodaj_gatunek
from pokaz_rekordy.views import f_edycja_gatunek
from pokaz_rekordy.views import f_usuniecie_gatunek
from pokaz_rekordy.views import f_pokaz_gra_gatunek
from pokaz_rekordy.views import f_dodaj_gra_gatunek
from pokaz_rekordy.views import f_edycja_gra_gatunek
from pokaz_rekordy.views import f_usuniecie_gra_gatunek
from pokaz_rekordy.views import f_pokaz_polka
from pokaz_rekordy.views import f_dodaj_polka
from pokaz_rekordy.views import f_edycja_polka
from pokaz_rekordy.views import f_usuniecie_polka
from pokaz_rekordy.views import f_pokaz_gra_polka
from pokaz_rekordy.views import f_dodaj_gra_polka
from pokaz_rekordy.views import f_edycja_gra_polka
from pokaz_rekordy.views import f_usuniecie_gra_polka




urlpatterns = [
    path('admin&123/', admin.site.urls),
    path('',test_f),
    path('pokaz_rekordy/',f_pokaz_rekordy),
    path('nowy_rekord/',f_dodaj_rekord),
    path('edycja/<int:id>',f_edycja_rekordu,name="link_edycja1"),
    path('usun/<int:id>',f_usuniecie_rekordu,name="link_usuniecie1"),

    path('pokaz_adres/',f_pokaz_adres),
    path('nowy_adres/',f_dodaj_adres),
    path('edycja_adres/<int:id>',f_edycja_adresu,name="link_edycja2"),
    path('usun_adres/<int:id>',f_usuniecie_adresu,name="link_usuniecie2"),

    path('pokaz_wydawca/',f_pokaz_wydawca),
    path('nowy_wydawca/',f_dodaj_wydawca),
    path('edycja_wydawca/<int:id>',f_edycja_wydawca,name="link_edycja3"),
    path('usun_wydawca/<int:id>',f_usuniecie_wydawca,name="link_usuniecie3"),

    path('pokaz_producent/',f_pokaz_producent),
    path('nowy_producent/',f_dodaj_producent),
    path('edycja_producent/<int:id>',f_edycja_producent,name="link_edycja4"),
    path('usun_producent/<int:id>',f_usuniecie_producent,name="link_usuniecie4"),

    path('pokaz_gatunek/',f_pokaz_gatunek),
    path('nowy_gatunek/',f_dodaj_gatunek),
    path('edycja_gatunek/<int:id>',f_edycja_gatunek,name="link_edycja5"),
    path('usun_gatunek/<int:id>',f_usuniecie_gatunek,name="link_usuniecie5"),

    path('pokaz_gra_gatunek/',f_pokaz_gra_gatunek),
    path('nowy_gra_gatunek/',f_dodaj_gra_gatunek),
    path('edycja_gra_gatunek/<int:id>',f_edycja_gra_gatunek,name="link_edycja6"),
    path('usun_gra_gatunek/<int:id>',f_usuniecie_gra_gatunek,name="link_usuniecie6"),

    path('pokaz_polka/',f_pokaz_polka),
    path('nowy_polka/',f_dodaj_polka),
    path('edycja_polka/<int:id>',f_edycja_polka,name="link_edycja7"),
    path('usun_polka/<int:id>',f_usuniecie_polka,name="link_usuniecie7"),

    path('pokaz_gra_polka/',f_pokaz_gra_polka),
    path('nowy_gra_polka/',f_dodaj_gra_polka),
    path('edycja_gra_polka/<int:id>',f_edycja_gra_polka,name="link_edycja8"),
    path('usun_gra_polka/<int:id>',f_usuniecie_gra_polka,name="link_usuniecie8")
    #path('aplikacja1/',include('aplikacja.urls'))
]
