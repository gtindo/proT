from django.shortcuts import render
from elearn.forms import *
from elearn.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from pprint import pprint
import datetime

def testInscriptionCours(idCours, idEtudiant):
    inscription = Inscription.objects.filter(cours_id=idCours, etudiant_id=idEtudiant)
    if len(inscription) == 0:
        return False
    return True

def inscriptionConnexion(inscriptionForm, connexionForm, request):
    envoi = False
    error = False

    if inscriptionForm.is_valid():
        username = inscriptionForm.cleaned_data['username']
        password = inscriptionForm.cleaned_data['password']
        email = inscriptionForm.cleaned_data['email']
        user = User.objects.create_user(username=username, email=email, password=password, is_staff=False)
        etudiant = Etudiant(user=user)
        etudiant.tel = '0'
        etudiant.save()

        envoi = True

    if connexionForm.is_valid():
        username = connexionForm.cleaned_data['username']
        password = connexionForm.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
        else:
            error = True

    return [envoi, error]

def accueil(request):
    inscriptionForm = InscriptionForm(request.POST or None)
    connexionForm = ConnexionForm(request.POST or None)
    error = False

    tests = inscriptionConnexion(inscriptionForm, connexionForm, request)
    error = tests[1]

    return render(request, 'elearn/accueil.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(accueil))

def profil(request):

    profileForm = ProfileForm(request.POST or None)


    error = False

    if profileForm.is_valid():
        pprint('valid form')
        photo = profileForm.cleaned_data['photo']
        localisation = profileForm.cleaned_data['localisation']
        sexe = profileForm.cleaned_data['sexe']
        date = profileForm.cleaned_data['date']
        statutPro = profileForm.cleaned_data['statutPro']
        niveauEtude = profileForm.cleaned_data['niveauEtude']
        statutEtudiant = profileForm.cleaned_data['statutEtudiant']
        aPropos = profileForm.cleaned_data['aPropos']
        confidentialite = profileForm.cleaned_data['confidentialite']

        etudiant = Etudiant.objects.get(user__username=request.user.username)
        etudiant.photo = photo
        etudiant.localisation = localisation
        etudiant.sexe = sexe
        etudiant.date = date
        etudiant.statutPro = statutPro
        etudiant.niveauEtude = niveauEtude
        etudiant.aPropos = aPropos
        etudiant.confidentialite = confidentialite
        etudiant.save()

    else:
        error = True

    pprint(error)

    return render(request, 'elearn/profile.html', locals())

def profileView(request):
    return render(request, 'elearn/profileView.html', locals())

def parametre(request):
    compteForm = CompteForm(request.POST or None)
    passeForm = PasseForm(request.POST or None)

    return render(request, 'elearn/parametres.html', locals())

def catalogue(request):
    categories = Categorie.objects.all()

    inscriptionForm = InscriptionForm(request.POST or None)
    connexionForm = ConnexionForm(request.POST or None)
    error = False

    tests = inscriptionConnexion(inscriptionForm, connexionForm, request)
    error = tests[1]

    return render(request, 'elearn/catalogue.html', locals())

def categorie(request, id_categorie):
    categories = Categorie.objects.all()
    categorie = Categorie.objects.get(id=id_categorie)
    sousCategories = categorie.souscategorie_set.all()
    tabCours = {}

    for sousCate in sousCategories:
        cours = sousCate.cours_set.all()
        tabCours[sousCate.nom] = cours

    inscriptionForm = InscriptionForm(request.POST or None)
    connexionForm = ConnexionForm(request.POST or None)
    error = False

    tests = inscriptionConnexion(inscriptionForm, connexionForm, request)
    error = tests[1]

    return render(request, 'elearn/categorie.html', locals())

def sousCategorie(request, id_sous_categorie):
    sousCategorie = SousCategorie.objects.get(id=id_sous_categorie)
    categorie = sousCategorie.categorie
    categories = Categorie.objects.all()
    cours = sousCategorie.cours_set.all()

    inscriptionForm = InscriptionForm(request.POST or None)
    connexionForm = ConnexionForm(request.POST or None)
    error = False

    tests = inscriptionConnexion(inscriptionForm, connexionForm, request)
    error = tests[1]

    return render(request, 'elearn/sousCategorie.html', locals())

def cours(request, id_cours):
    cours = Cours.objects.get(id=id_cours)
    sousCategorie = cours.sousCategorie
    categorie = sousCategorie.categorie
    enseignants = cours.enseignants.all()
    testInscription = False

    weeks = cours.weeks.all()
    dictWeek = {}
    i = 1

    for week in weeks:
        videos = week.videos.all()
        lectures = week.lectures.all()
        quizs = week.quizs.all()
        str = "Semaine {}".format(i)
        dictWeek[str] = [week, [len(videos), videos], [len(lectures), lectures], [len(quizs), quizs]]
        i += 1


    inscriptionForm = InscriptionForm(request.POST or None)
    connexionForm = ConnexionForm(request.POST or None)
    error = False

    tests = inscriptionConnexion(inscriptionForm, connexionForm, request)
    error = tests[1]

    coursInscriptionForm = InscriptionCoursForm()
    if coursInscriptionForm.is_valid():
        pass
    else :
        if request.user:
            user = request.user
            pprint(user.id)
            etudiant = Etudiant.objects.get(user_id=user.id)
            addInscription = Inscription.objects.create(dateInscription=datetime.date, cours=cours, etudiant=etudiant)
        pprint('formulaire incorrect')

    if request.user:
        user = request.user
        pprint(user.id)
        etudiant = Etudiant.objects.get(user_id=user.id)
        testInscription = testInscriptionCours(cours.id, etudiant.id)


    return render(request, 'elearn/cours_presentation.html', locals())

def coursBoard(request):

    return render(request, 'elearn/coursBoard.html', locals())

def coursMainVid(request, idCours, idWeek, idVideo):
    cours = Cours.objects.get(id=idCours)
    semaine = Week.objects.get(id=idWeek)
    video = Video.objects.get(id=idVideo)

    videos = semaine.videos.all()
    lecutres = semaine.lectures.all()

    return render(request, 'elearn/cours-main.html', locals())
