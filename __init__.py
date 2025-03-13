from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
  
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")


@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    somme_valeurs = valeur1 + valeur2
    parite = "paire" if somme_valeurs % 2 == 0 else "impaire"
    return f"<h2>La somme de vos valeurs est : {somme_valeurs}</h2><p>La somme est {parite}.</p>"

@app.route('/sommetotale/<path:val>')
def sommetot(val):
    sommet = list(map(int, val.split('/')))
    sommetotale = sum(sommet)
    return "La somme totale des valeurs est :" + str(sommetotale)
  
@app.route('/jeu_des/')
def Jeu_Des():
    return render_template('Jeu_Des_Base.html')

@app.route('/roulette_russe/')
def barillet():
    return render_template('Barillet_Vide.html')

if __name__ == "__main__":
  app.run(debug=True)







