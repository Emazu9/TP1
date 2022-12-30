from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib
def index(request):

    donnees={
        'nom':'general',
        'postnom':'jhonson',
        'sexe':'Masculin'
    }

    template=loader.get_template('index.html')
    return HttpResponse(template.render(donnees,request))

def listeEtudiants(request):
    return HttpResponse("Liste des etudiants")

def loyer(request):
    template=loader.get_template('ml.html')
    return HttpResponse(template.render({},request))

def predire(request):
    #on verifie si la methode est POST pour
    #recuperer les donnees du formulaire
    if request.method=='POST':

        #on garde dans les varialbes les valeurs
        #venues des champs du formulaire
        #on les convertit en entier car le formulaire
        #retourne par defaut les chaines de caracteres
        Villa=int(request.POST['Villa'])
        Avenues=int(request.POST['Avenues'])
        Electricite=int(request.POST['Electricite'])

        #on cree un table en deux dimensions pour le soumettre
        #au modele de prediction
        tableau=[[Villa,Avenues,Electricite]]
        print(tableau)

        #on charge le modele
        regresseur=joblib.load('modele_ml/jonathan.pkl')
        resultat=regresseur.predict(tableau)
        
        print(resultat)


    return HttpResponse('ok')

