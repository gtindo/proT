from django import forms
from django.contrib.auth.models import User
from elearn.models import Etudiant, Cours

SEXES = (
    ('1','Masculin'), ('2','Féminin')
)
STATUTS = (
    ('1',''),
    ('2','Employé(e) à temps plein(au moins 35 heures par semaine)'),
    ('3','Employé(e) à temps partiel(moins de 35 heures par semaine)'),
    ('4','Travailleur indépendant à temps plein(au moins 35 heures par semaine)'),
    ('5','Travailleur indépendant à temps partiel(moins de 35 heures par semaine)'),
    ('6','Personne au foyer, aidant familial ou en congé de maternité/parental'),
    ('7','Au chômage et en recherche d\'emploi'),
    ('8','Au chômqge et sans emploi'),
    ('9','À la retraite'),
    ('10','Inapte au travail')
)

ETUDE = (
    ('1', ''),
    ('2','Moins qu\'un diplôme d\'enseignement secondaire(ou équivalent)'),
    ('3','Diplôme d\'enseignement secondaire(ou équivalent)'),
    ('4','Études universitaires(sans diplôme)'),
    ('5','Diplôme sanctionnant 2 années d\'étude universitaires'),
    ('6','Licence'),
    ('7','Master'),
    ('8','Diplôme d\'école professionnelle'),
    ('9','Doctorat')
)

STATUTE = (
    ('1', ''),
    ('2','Oui, je suis actuellement un(e) étudiant(e) à temps complet dans un programme de formation délivrant un diplôme universitaire'),
    ('3','Oui, je suis actuellement un(e) étudiant(e) à temps partiel dans un programme de formation délivrant un diplôme universitaire'),
    ('4','Non, je ne suis pas actuellement un(e) étudiant(e) dans un programme de formation délivrant un diplôme universitaire')
)

CONFIDENTIALITE = (
    ('1','Seleument moi'),
    ('2','La communauté Elearn'),
    ('3','Tout le web')
)

class InscriptionForm(forms.Form):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label='Nom d\'utilisateur', max_length=30)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    confirmation = forms.CharField(label='Confirmation du mot de passe', widget=forms.PasswordInput)

    def clean_confirmation(self):
        confirmation = self.cleaned_data['confirmation']
        password = self.cleaned_data['password']

        if confirmation != password:
            raise forms.ValidationError("Confirmation differente du mot de passe")

        return confirmation

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError("L'utilisateur existe deja")
        except User.DoesNotExist:
            pass

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("L'email existe deja")
        except User.DoesNotExist:
            pass

        return email

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class ProfileForm(forms.Form):
    photo = forms.ImageField(label="Photo", required=False)
    localisation = forms.CharField(label="Localisation", required=False)
    sexe = forms.ChoiceField(label='Sexe',required=False, choices=SEXES, widget=forms.RadioSelect)
    date = forms.DateField(label="Date de naissance", required=False, widget=forms.DateInput)
    statutPro = forms.ChoiceField(label="Statut professionnel", required=False, widget=forms.Select, choices=STATUTS)
    niveauEtude = forms.ChoiceField(label='Niveau d\'étude', required=False, choices=ETUDE, widget=forms.Select)
    statutEtudiant = forms.ChoiceField(label='Statut de l\'étudiant', required=False, choices=STATUTE, widget=forms.Select)
    aPropos = forms.CharField(label='À mon sujet', required=False, widget=forms.Textarea)
    confidentialite = forms.ChoiceField(label='Confidentialité (Qui peut voir ces infos)',required=False, choices=CONFIDENTIALITE, widget=forms.Select)

class CompteForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    email = forms.CharField(label="Email")

class PasseForm(forms.Form):
    passeActuel = forms.CharField(label="Mot de passe actuel", widget=forms.PasswordInput)
    passeNouveau = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput)
    passeNouveauConfirmation = forms.CharField(label="Retaper le mot de passe", widget=forms.PasswordInput)

class InscriptionCoursForm(forms.Form):
    idCours = forms.CharField(widget=forms.HiddenInput, required=False)
    idEtudiant = forms.CharField(widget=forms.HiddenInput, required=False)
    dateInscription = forms.DateField(widget=forms.HiddenInput, required=False)




