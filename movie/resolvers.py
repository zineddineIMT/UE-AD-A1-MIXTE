import json

# Chemin vers les fichiers de données
MOVIES_DATA_FILE = '{}/data/movies.json'.format(".")


# Résolveur pour récupérer tous les films
def all_movies(_, info):
    with open(MOVIES_DATA_FILE, "r") as file:
        return json.load(file)['movies']


# Résolveur pour récupérer un film par son ID
def movie_with_id(_, info, _id):
    return find_movie_by_id(_id)


# Résolveur pour récupérer les films par réalisateur
def movies_by_director(_, info, director):
    with open(MOVIES_DATA_FILE, "r") as file:
        movies = json.load(file)["movies"]
        return [movie for movie in movies if movie['director'].lower() == director.lower()]


# Résolveur pour récupérer un film par son titre
def movie_by_title(_, info, title):
    with open(MOVIES_DATA_FILE, "r") as file:
        movies = json.load(file)['movies']
        return next((movie for movie in movies if movie['title'].lower() == title.lower()), None)


# Résolveur pour mettre à jour la note d'un film
def update_movie_rate(_, info, _id, _rate):
    return update_and_save_movie(_id, _rate)


# Résolveur pour créer un nouveau film
def create_movie(_, info, movieid, title, director, rating):
    return create_and_save_movie(movieid, title, director, rating)


# Résolveur pour supprimer un film
def delete_movie(_, info, movieid):
    return delete_and_save_movie(movieid)


# Fonction auxiliaire pour trouver un film par son ID
def find_movie_by_id(movie_id):
    with open(MOVIES_DATA_FILE, "r") as file:
        movies = json.load(file)['movies']
        return next((movie for movie in movies if movie['id'] == movie_id), None)


# Fonction auxiliaire pour mettre à jour et sauvegarder un film
def update_and_save_movie(movie_id, new_rate):
    with open(MOVIES_DATA_FILE, "r") as file:
        movies_data = json.load(file)
        movies = movies_data['movies']
        movie = next((movie for movie in movies if movie['id'] == movie_id), None)

        if not movie:
            return {"error": "Movie not found"}

        movie['rating'] = new_rate
        save_movies_data(movies_data)

    return movie


# Fonction auxiliaire pour créer et sauvegarder un nouveau film
def create_and_save_movie(movieid, title, director, rating):
    new_movie = {"id": movieid, "title": title, "director": director, "rating": rating}
    with open(MOVIES_DATA_FILE, "r") as file:
        movies_data = json.load(file)
        if any(movie['id'] == movieid for movie in movies_data['movies']):
            return {"error": "Movie ID already exists"}

        movies_data['movies'].append(new_movie)
        save_movies_data(movies_data)

    return new_movie


# Fonction auxiliaire pour supprimer et sauvegarder la suppression d'un film
def delete_and_save_movie(movie_id):
    with open(MOVIES_DATA_FILE, "r") as file:
        movies_data = json.load(file)
        movies = movies_data['movies']
        movie = next((movie for movie in movies if movie['id'] == movie_id), None)

        if not movie:
            return {"error": "Movie not found"}

        movies_data['movies'] = [m for m in movies if m['id'] != movie_id]
        save_movies_data(movies_data)

    return {"success": True, "message": "Movie deleted successfully"}


# Fonction auxiliaire pour sauvegarder les données des films
def save_movies_data(movies_data):
    with open(MOVIES_DATA_FILE, "w") as file:
        json.dump(movies_data, file, indent=4)
