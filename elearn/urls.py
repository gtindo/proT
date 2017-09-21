from django.conf.urls import url
from elearn.views import *

urlpatterns = [
    url(r'^accueil/$', accueil, name='accueil'),
    url(r'^deconnexion/$', deconnexion, name='deconnexion'),
    url(r'^profil/$', profil, name='profil'),
    url(r'^profil/view/$', profileView, name='profileView'),
    url(r'^parametres/$', parametre, name='parametre'),
    url(r'^catalogue/$', catalogue, name='catalogue'),
    url(r'^catalogue/categorie/(?P<id_categorie>\d+)$', categorie, name="categorie"),
    url(r'^catalogue/sous-categorie/(?P<id_sous_categorie>\d+)$', sousCategorie, name="sousCategorie"),
    url(r'^catalogue/cours-presentation/(?P<id_cours>\d+)$', cours, name="cours"),
    url(r'^catalogue/cours-board/(?P<id_cours>\d+)$', coursBoard, name="coursBoard"),
    url(r'^cours/(?P<idCours>\d+)/week/(?P<idWeek>\d+)/vid/(?P<idVideo>\d+)$', coursMainVid, name="coursMainVid")
]