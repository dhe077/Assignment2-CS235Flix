from typing import List, Iterable

from CS235Flix.repositorydir.repository import AbstractRepository
from CS235Flix.domainmodel.movie import Movie


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie(movie_ID: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_ID)
    if movie is None:
        raise NonExistentMovieException
    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):
    movie = repo.get_first_movie()
    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):
    movie = repo.get_last_movie()
    return movie_to_dict(movie)


def get_movies_by_year(year, repo: AbstractRepository):
    movies = repo.get_movies_by_year(year)
    movies_dto = list()
    prev_year = next_year = None
    if len(movies) > 0:
        prev_year = repo.get_year_of_previous_movie(movies[0])
        next_year = repo.get_year_of_next_movie(movies[0])

        # convert movies to dict form
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_year, next_year


def get_movies_by_ids(id_list, repo: AbstractRepository):
    movies = repo.get_movies_by_id(id_list)
    movies_as_dict = movies_to_dict(movies)
    return movies_as_dict


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


# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_movie(dictn):
    movie = Movie(dictn[title], dictn.release_year, dictn[ID])
    return movie
