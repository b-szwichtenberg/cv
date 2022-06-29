from django.urls import path
from aplikacja.views import test_f

urlpatterns = [
    path('test/',test_f)
]
