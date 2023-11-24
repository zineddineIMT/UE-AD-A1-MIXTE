from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify, make_response

import resolvers as r

# Configuration du port et de l'hôte pour le serveur Flask
PORT = 3001
HOST = '0.0.0.0'
app = Flask(__name__)

# Chargement des définitions de types GraphQL depuis un fichier
type_defs = load_schema_from_path('movie.graphql')

# Création des types de requêtes et de mutations
query = QueryType()
mutation = MutationType()

# Création des types d'objet pour Movie et Actor
movie = ObjectType('Movie')
actor = ObjectType('Actor')

# Configuration des résolveurs pour les requêtes
query.set_field('all_movies', r.all_movies)
query.set_field('movie_with_id', r.movie_with_id)
query.set_field('movies_by_director', r.movies_by_director)
query.set_field('movie_by_title', r.movie_by_title)

# Configuration des résolveurs pour les mutations
mutation.set_field('update_movie_rate', r.update_movie_rate)
mutation.set_field('create_movie', r.create_movie)
mutation.set_field('delete_movie', r.delete_movie)

# Configuration du résolveur pour les acteurs dans un film
movie.set_field('actors', r.resolve_actors_in_movie)

# Création du schéma exécutable
schema = make_executable_schema(type_defs, movie, query, mutation, actor)

# Route racine pour un message d'accueil
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

# Route pour l'interface de test GraphQL (Playground)
@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200

# Route pour le serveur GraphQL
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
                        schema,
                        data,
                        context_value=None,
                        debug=app.debug
                    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
