import random
from typing import List, Iterable

from CS235Flix.repositorydir import AbstractRepository
from CS235Flix.domainmodel.movie import Movie


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()
    if quantity >= movie_count:
        # Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
        quantity = movie_count - 1

    # pick distinct and random movies
    random_ids = random.sample(range(1, movie_count), quantity)
    movies = repo.get_articles_by_id(random_ids)


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'ID': movie.ID,
        'release_year': movie.release_year,
        'title': movie.title,
        'director': movie.director,
        'actors': movie.actors,
        'genres': movie.genres,
        'runtime_minutes': movie.runtime_minutes,
        'description': movie.description,
        'external_rating': movie.external_rating,
        'rating_votes': movie.rating_votes,
        'revenue': movie.revenue,
        'metascores': movie.metascores
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]