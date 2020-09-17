import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> set:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> set:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                actors = row['Actors'].split(",")
                genres = row['Genre'].split(",")
                director = Director(row['Director'])
                rating = row['Rating']
                votes = row['Votes']
                revenue = row['Revenue (Millions)']
                metascore = row['Metascore']
                movie = Movie(title, release_year)
                movie.director = director
                # extension attribute application
                movie.external_rating = rating
                movie.rating_votes = votes
                movie.revenue = revenue
                movie.metascores = metascore

                # adding the actors, genres, director and the movie to the corresponding datasets
                for i in range(len(actors)):
                    actor = Actor(actors[i])
                    movie.add_actor(actor)
                    if actor not in self.__dataset_of_actors:
                        # adding only unique actors to the dataset
                        self.__dataset_of_actors.add(actor)
                for i in range(len(genres)):
                    genre = Genre(genres[i])
                    movie.add_genre(genre)
                    if genre not in self.__dataset_of_genres:
                        # adding only unique genres to the dataset
                        self.__dataset_of_genres.add(genre)
                if movie.director not in self.__dataset_of_directors:
                    # adding only unique directors to the dataset
                    self.__dataset_of_directors.add(movie.director)

                self.__dataset_of_movies.append(movie)
                index += 1

                # print(f"Movie {index} with title: {title}, release year {release_year}")