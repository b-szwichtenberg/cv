from django.contrib import admin

# Register your models here.
from .models import Gra
from .models import Adres
from .models import Wydawca
from .models import Producent
from .models import Gatunek
from .models import Gra_gatunek
from .models import Polka
from .models import Gra_polka


admin.site.register(Gra)
admin.site.register (Adres)
admin.site.register(Wydawca)
admin.site.register(Producent)
admin.site.register(Gatunek)
admin.site.register(Gra_gatunek)
admin.site.register(Polka)
admin.site.register(Gra_polka)