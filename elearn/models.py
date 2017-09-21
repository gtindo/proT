from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ressource(models.Model):
    url = models.URLField()
    titre = models.CharField(max_length=250)

    def __str__(self):
        return self.titre

class Lecture(models.Model):
    texte = models.TextField()
    duree = models.CharField(max_length=10)
    ressources = models.ManyToManyField(Ressource)
    titre = models.CharField(max_length=100)

    def __str__(self):
        return "Lecture {}".format(self.titre)

class Ligne(models.Model):
    question = models.CharField(max_length=100)
    reponse = models.CharField(max_length=100)
    choix1 = models.CharField(max_length=100)
    choix2 = models.CharField(max_length=100)
    choix3 = models.CharField(max_length=100)
    quiz = models.ForeignKey("Quiz")

    def __str__(self):
        return "Ligne : "+self.nom

class Quiz(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return "Quiz : "+self.titre

class Video(models.Model):
    titre = models.CharField(max_length=100)
    htmlCode = models.TextField()
    duree = models.CharField(max_length=10)

    def __str__(self):
        return "Video : "+self.titre

class Week(models.Model):
    syllabus = models.TextField()
    lectures = models.ManyToManyField(Lecture)
    videos = models.ManyToManyField(Video)
    quizs = models.ManyToManyField(Quiz)
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre

class Enseignant(models.Model):
    user = models.OneToOneField(User)
    nom = models.CharField(max_length=100)
    titre = models.CharField(max_length=50)
    domaine = models.ForeignKey("Categorie")
    tel = models.CharField(max_length=15)
    dateNaissance = models.DateField()

    def __str__(self):
        return "Enseignant {}".format(self.user.username)

class Etudiant(models.Model):
    user = models.OneToOneField(User)
    tel = models.CharField(max_length=15)
    dateNaissance = models.DateField(null=True)
    photo = models.ImageField(upload_to='images_profil')
    localisation = models.CharField(max_length=50)
    sexe = models.CharField(max_length=10)
    statutProfessinnel = models.CharField(max_length=100)
    niveauEtude = models.CharField(max_length=100)
    statutEtudiant = models.CharField(max_length=100)
    aPropos = models.TextField(max_length=250)
    confidentialite = models.CharField(max_length=100)

    def __str__(self):
        return "Etudiant {}".format(self.user.username)

class DispenseCours(models.Model):
    cours = models.ForeignKey("Cours")
    enseignant = models.ForeignKey("Enseignant")

class Inscription(models.Model):
    dateInscription = models.DateTimeField(auto_now_add=True, auto_now=False)
    cours = models.ForeignKey("Cours")
    etudiant = models.ForeignKey("Etudiant")

class ReponseSujet(models.Model):
    contenu = models.TextField(max_length=300)
    dateReponse = models.DateTimeField(auto_now_add=True, auto_now=False)
    autheur = models.OneToOneField(User)
    sujet = models.ForeignKey("SujetDiscussion")

class SujetDiscussion(models.Model):
    titre = models.CharField(max_length=100)
    texte = models.TextField(max_length=300)
    reponses = models.ManyToManyField(ReponseSujet)
    autheur = models.OneToOneField(User)
    forum = models.ForeignKey("Forum")

class Forum(models.Model):
    objet = models.CharField(max_length=100)


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey("Categorie")

    def __str__(self):
        return self.nom


class Cours(models.Model):
    nom = models.CharField(max_length=50)
    duree = models.CharField(max_length=10, blank=True)
    sousCategorie = models.ForeignKey("SousCategorie")
    objectif = models.TextField()
    langue = models.CharField(max_length=30)
    weeks = models.ManyToManyField(Week, blank=True)
    etudiants = models.ManyToManyField(Etudiant, through="Inscription")
    enseignants = models.ManyToManyField(Enseignant, blank=True)
    forums = models.ManyToManyField(Forum, blank=True)
    logo = models.ImageField(upload_to='images_cours/')
    ecole = models.ForeignKey("Ecole")
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Ecole(models.Model):
    nom = models.CharField(max_length=50)
    urlLogo = models.CharField(max_length=250)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.nom


