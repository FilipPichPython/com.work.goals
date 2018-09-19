from django.urls import path
from .views import filmy_calosc, nowy_film, edytuj_film, usun_film
from django.conf.urls import url, include
from rest_framework import routers
from .views import UzytkownikSet, FilmSet

router = routers.DefaultRouter()
router.register(r'users', UzytkownikSet)
router.register(r'movies', FilmSet)


urlpatterns = [
    path('filmy/', filmy_calosc, name='wszystkie_filmy'),
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name='edytuj_film'),
    path('usun/<int:id>/', usun_film, name='usun_film'),
    url(r'^', include(router.urls)),
]
