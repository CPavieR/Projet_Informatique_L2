from flask import Flask, redirect, url_for, request, render_template
from manipulationquestions import *
app = Flask(__name__)


@app.route("/") #Page principale du site
def index():
    return render_template("acceuil.html")

@app.route("/register") #Page de création d'un compte
def reg():
    return render_template("register.html")

@app.route("/register",methods = ['POST']) #Code d'enregistrement d'un utilisateur
def enregistrement():
    nom_utilisateur = request.form['idUser'] #On récupère son id
    email = request.form['email'] #Son mail
    mot_de_passe = request.form['password'] #Son mot de passe
    #ouverture du csv des utilisateurs, verification que le nom d'utilisateur n'est pas déjà utilisé ni le mail, si ce n'est pas le cas, on écrit dans le csv


@app.route("/login") #Page de connexion à un compte
def log():
    return render_template("login.html")

@app.route("/login",methods = ['POST']) #Code de connexion d'un utilisateur
def connexion():
    nom_utilisateur = request.form['idUser'] #On récupère son id
    mot_de_passe = request.form['password'] #Son mot de passe
    #ouverture du csv des utilisateurs, verification que le mot de passe saisi est le même que celui du csv et si c'est le cas on le connecte


@app.route("/BDD") #Page d'accueil du compte avec la vue de toutes les questions créées et les étiquettes en haut, lorsqu'on clique sur une étiquette on ne voit plus que
def BDD():          #les questions qui ont cette étiquette
    dico = depuis_csv(IdUser)
    return render_template("BDD.html", li_dictionnaire=dico)



@app.route("/creationQuestion") #Page de création d'une question avec un nom, un énoncé, des réponses, une correction et des étiquettes
def creationQuestion():
    return render_template("creationQuestion.html")

@app.route("/creationQuestion",methods = ['POST']) #Code d'enregistrement d'une question une fois que toutes ses infos ont été rentrées pour une création
def ajoutQuestion():
    #idQuestion #= #il faudrait rajouter ici un identifiant de question pas encore utilisé
    etiquettes = request.form['etiquettes'] #Ses étiquettes = str separé par ";"
    enonce = request.form['enonce'] #Son énoncé sous la forme markdown avec un titre mis en avant dans la bdd
    reponses = request.form['li_rep_possibles'] #Ses réponses
    nb_reponses = request.form['nb_rep_possibles'] #Son nombre de bonnes réponses
    li_bonnes_reponses = [] #Initialisation de la liste des bonnes réponse
    #print(etiquettes + ' / ' + enonce + ' / ' + reponses + ' / ' + nb_reponses)
    for i in range(int(nb_reponses)): #Code de la liste des bonnes réponses
        if request.form.get(str(i), False) == 'on': #lorsque request.form[str(i)] est null, on a une erreur donc on utilise request.form.get(str(i), False) qui renvoie 'False' lorsque la requête est nulle (pas d'erreur) et 'on' sinon ('on' est renvoyé pour les réponses mises en bonnes réponses par l'utilisateur)
            li_bonnes_reponses.append(i) #On ajoute à la liste des bonnes réponses l'indice des bonnes réponses
    #print(etiquettes + ' / ' + enonce + ' / ' + reponses + ' / ' + str(nb_reponses) + ' / ')
    li_etiquettes = etiquettes.split(';') 
    li_rep = reponses.split(';')
    dictionnaire = {"Question": enonce, "ET": li_etiquettes, "REP": li_rep, "BREP": li_bonnes_reponses} #dictionnaire avec Question -> enoncé ; ET -> liste des étiquettes ; REP -> liste des réponses ; BREP -> liste des bonnes réponses
    dans_csv(IdUser, dictionnaire) #Ajout du dictionnaire d'une question dans le csv des questions

    #return render_template("question/"+idQuestion+".html") #On renvoie la personne sur la vue de la question créée (si elle a bien été créée)


@app.route("/question/<idQuestion>") #Page de visualisation d'une question
def question(idQuestion):
    return render_template(""+idQuestion+".html")

@app.route("/modificationQuestion/<idQuestion>") #Page de modification d'une question
def modifierQuestion(idQuestion):
    return render_template("modificationQuestion/"+idQuestion+".html") #pour la modification il faut récupérer les infos existantes de la question et refaire la même chose qu'à la création

@app.route("/modificationQuestion/<idQuestion>",methods = ['POST']) #Code d'enregistrement d'une question une fois que toutes ses infos ont été rentrées pour une modif
def modificationQuestion(idQuestion):
    etiquettes = request.form['etiquettes'] #Ses étiquettes = str separé par ";"
    question = request.form['question'] #Son énoncé
    reponses = request.form['reponses'] #Ses réponses
    correction = request.form['0'] #Sa correction (bonnes réponses)
    #file1 = open("question.csv","a") #On ouvre le fichier csv où la question doit être enregistrée
    #string = name+'///'+enonce+'///'+str(reponses)+'///'+str(correction)+'///'+str(etiquettes)+'\n' #On créée la ligne qui sera enregistrée en append avec '///' comme séparateur (temporaire)
    #Ici on peut pas juste écrire dans le fichier, il faut soit réecrire sur la question existante soit supprimer la question existante et écrire la nouvelle (ou atre méthode ?)
    #return render_template("question/"+idQuestion+".html")



@app.route("/creationFeuille") #Page de création d'une feuille de questions
def creationFeuille():
    return render_template("creationFeuille.html")

@app.route("/creationFeuille",methods = ['POST']) #La création d'une feuille 
def feuille():
    #récupération de la liste d'id des exos de la feuille et renvoie à feuille.html
    return render_template("feuille.html")

#@app.route("/feuille")
#def feuille():
#    return render_template("feuille.html")

if __name__ == '__main__':
    app.run(debug = True)
