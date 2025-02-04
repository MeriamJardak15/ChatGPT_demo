from flask import Flask, render_template, jsonify, request
import config
import openai
import aiapi

#render : une fonction qui rend les templates html 
#jsonify: Une fonction pour convertir des données Python en JSON
#request: Un objet qui contient les données de la requête client, utilisé ici pour accéder aux données envoyées via les formulaires POST

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__) #creation d'une instance d application Flask
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found) #enregistrer la fonction page_not_found comme gestionnaire d'erreur pour les erreurs 404


@app.route('/', methods = ['POST', 'GET']) #un décorateur qui relie la route '/' à la fonction index(). Cette route correspond à la page d'accueil du site et accepte les méthodes HTTP POST et GET

def index():
    
    if request.method == 'POST' :  #un formulaire a été soumis depuis le frontend
       prompt = request.form['prompt']
       res ={}
       res['answer']= aiapi.generateChatResponse(prompt)

       return jsonify(res), 200 # renvoie le dictionnaire res sous forme de réponse JSON avec le code d'état HTTP 200


    return render_template('index.html', **locals())
# Si la méthode de la requête n'est pas POST, cela signifie que 
# l'utilisateur accède simplement à la page d'accueil.
#  Dans ce cas, nous rendons le template 'index.html' avec les variables 
# locales disponibles.

if __name__ == '__main__': #C'est une condition qui vérifie si ce fichier est le fichier principal
    app.run(host='0.0.0.0', port='8888', debug=True)
    #L'option debug=True active le mode de débogage, ce qui signifie que des erreurs détaillées 
    #seront affichées en cas de problème





