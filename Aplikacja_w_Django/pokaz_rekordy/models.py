from django.db import models

class Gra(models.Model):
    tytul = models.CharField(max_length=50, blank=False,unique=True)
    producent = models.CharField(max_length=50, blank=False)
    wydawca = models.CharField(max_length=50, blank=False)
    ocena = models.PositiveSmallIntegerField(default=0)
    premiera = models.DateField(null=True,blank=True)
    opis = models.TextField(default="")
    def __str__(self):
        return self.tytul

class Adres(models.Model):
    panstwo = models.CharField(max_length=50, blank=False)
    miasto = models.CharField(max_length=50, blank=False)
    kod = models.CharField(max_length=12, blank=False)
    ulica = models.CharField(max_length=50, blank=False)
    budynek = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        return self.miasto

class Wydawca(models.Model):
    nazwa = models.CharField(max_length=50, blank=False)
    strona = models.CharField(max_length=50)
    adres = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Producent(models.Model):
    nazwa = models.CharField(max_length=50, blank=False)
    strona = models.CharField(max_length=50)
    adres = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
        return self.nazwa

class Gra_gatunek(models.Model):
    gra = models.CharField(max_length=50, blank=False)
    gatunek = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.gra+str(self.gatunek)

class Polka(models.Model):
    nazwa = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.nazwa

class Gra_polka(models.Model):
    gra = models.CharField(max_length=50, blank=False)
    polka = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.gra+str(self.polka)