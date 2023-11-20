import json

def all_movies(_, info):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies_data = json.load(file)
        return movies_data['movies']

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie

def movies_by_director(_, info, director):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)["movies"]
        matching_movies = [movie for movie in movies if movie['director'].lower() == director.lower()]

    return matching_movies

def movie_by_title(_, info, title):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies_data = json.load(file)
        for movie in movies_data['movies']:
            if movie['title'].lower() == title.lower():
                return movie
    return None  # Retourne None si aucun film n'est trouvé avec ce titre

def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def create_movie(_, info, movieid, title, director, rating):
    new_movie = {
        "id": movieid,
        "title": title,
        "director": director,
        "rating": rating
    }

    with open('{}/data/movies.json'.format("."), "r") as file:
        movies_data = json.load(file)
        for movie in movies_data['movies']:
            if movie['id'] == movieid:
                raise Exception("Movie ID already exists")

    movies_data['movies'].append(new_movie)

    with open('{}/data/movies.json'.format("."), "w") as file:
        json.dump(movies_data, file)

    return new_movie

def delete_movie(_, info, movieid):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies_data = json.load(file)
        movies = movies_data['movies']
        movie_to_delete = next((movie for movie in movies if movie['id'] == movieid), None)

    if movie_to_delete:
        movies_data['movies'].remove(movie_to_delete)
        with open('{}/data/movies.json'.format("."), "w") as file:
            json.dump(movies_data, file)
        return {"success": True, "message": "Movie deleted successfully"}

    return {"success": False, "message": "Movie ID not found"}


