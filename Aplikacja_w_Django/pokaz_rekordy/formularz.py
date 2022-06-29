from django.forms import ModelForm
from .models import Gra
from .models import Adres
from .models import Wydawca
from .models import Producent
from .models import Gatunek
from .models import Gra_gatunek
from .models import Polka
from .models import Gra_polka

class GraFormularz(ModelForm):
    class Meta:
        model = Gra
        fields = ['tytul','producent','wydawca','ocena','premiera','opis']

class AdresFormularz(ModelForm):
    class Meta:
        model = Adres
        fields = ['panstwo','miasto','kod','ulica','budynek']

class WydawcaFormularz(ModelForm):
    class Meta:
        model = Wydawca
        fields = ['nazwa','strona','adres']

class ProducentFormularz(ModelForm):
    class Meta:
        model = Producent
        fields = ['nazwa','strona','adres']

class GatunekFormularz(ModelForm):
    class Meta:
        model = Gatunek
        fields = ['nazwa']

class Gra_gatunekFormularz(ModelForm):
    class Meta:
        model = Gra_gatunek
        fields = ['gra','gatunek']

class PolkaFormularz(ModelForm):
    class Meta:
        model = Polka
        fields = ['nazwa']

class Gra_polkaFormularz(ModelForm):
    class Meta:
        model = Gra_polka
        fields = ['gra','polka']