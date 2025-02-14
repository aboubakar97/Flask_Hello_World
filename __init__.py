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

@app.route('/calcul_carre/', methods=['GET'])
def calculer_carre():
    # Récupérer le nombre passé en paramètre dans l'URL
    try:
        # Vérifier si la valeur "valeur" existe dans les paramètres de la requête
        valeur = float(request.args.get('valeur'))
        carre = valeur ** 2
        return jsonify({"valeur": valeur, "carre": carre}), 200
    except TypeError:
        return jsonify({"error": "Le paramètre 'valeur' est manquant ou invalide."}), 400
    except ValueError:
        return jsonify({"error": "La valeur doit être un nombre."}), 400



  
@app.route('/cnam/')
def cnam():
    return render_template('mise_en_ligne.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
