from CS235Flix.domainmodel.genre import Genre
from CS235Flix.domainmodel.actor import Actor
from CS235Flix.domainmodel.director import Director


class Movie:

    def __init__(self, movie_name: str, year: int, id: int):
        if movie_name == "" or type(movie_name) is not str:
            self.__title = None
        else:
            self.__title = movie_name.strip()
        if year >= 1900:
            self.__release_year = year
        else:
            self.__release_year = None
        self.__description: str = ""
        self.__director: Director = None
        self.__actors: list = list()
        self.__genres: list = list()
        self.__runtime_minutes: int = 0

        self.__external_rating = 0
        self.__rating_votes = 0
        self.__revenue = None
        self.__metascores = None

        self.__ID: int = id

    # property mechanism of title, description, director, actors, genres,
    # runtime, external_rating, revenue and metascores
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        self.__title = new_title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str):
        self.__description = new_description

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, new_director: Director):
        self.__director = new_director

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, new_actors_list: list):
        self.__actors = new_actors_list

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, new_genres_list: list):
        self.__genres = new_genres_list

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime_minutes):
        if new_runtime_minutes > 0:
            self.__runtime_minutes = new_runtime_minutes
        else:
            raise ValueError

    # extensions properties below
    @property
    def external_rating(self) -> float:
        return self.__external_rating

    @external_rating.setter
    def external_rating(self, new_external_rating: float):
        if new_external_rating is not float:
            if float(new_external_rating) >= 0:
                self.__external_rating = float(new_external_rating)

    @property
    def rating_votes(self) -> int:
        return self.__rating_votes

    @rating_votes.setter
    def rating_votes(self, new_rating_votes: int):
        if new_rating_votes is not int:
            if int(new_rating_votes) >= 0:
                self.__rating_votes = int(new_rating_votes)

    @property
    def revenue(self) -> int:
        return self.__revenue

    @revenue.setter
    def revenue(self, new_revenue: float):
        if new_revenue is not float and new_revenue != "N/A":
            if float(new_revenue) >= 0:
                self.__revenue = float(new_revenue)

    @property
    def metascores(self) -> int:
        return self.__metascores

    @metascores.setter
    def metascores(self, new_metascores: int):
        if new_metascores is not int and new_metascores != "N/A":
            if int(new_metascores) >= 0:
                self.__metascores = int(new_metascores)

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, new_ID: int):
        self.__ID = new_ID

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, new_release_year: int):
        self.__release_year = new_release_year

    # add external rating, rating votes, revenue and meta scores as extra

    def __repr__(self) -> str:
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if self.__title == other.title and self.__release_year == other.__release_year and self.__ID == other.__ID:
            return True
        return False

    def __lt__(self, other):
        if self.title < other.title:
            return True
        return False

    def __hash__(self):
        return hash(self.title)

    def add_actor(self, actor: Actor):
        if actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

    # extension method
    def add_rating_vote(self, rating: int):
        self.__rating_votes += 1
        self.__external_rating = (self.external_rating * (self.rating_votes - 1) + rating) / self.rating_votes


class TestMovieMethods:

    def test_init(self):
        movie = Movie("Moana", 2016, 7)
        print(movie)

        director = Director("Ron Clements")
        movie.director = director
        print(movie.director)

        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        assert movie.actors == [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"),
                                Actor("Temuera Morrison")]
        assert len(movie.actors) == 4

        movie.runtime_minutes = 107
        print("Movie runtime: {} minutes".format(movie.runtime_minutes))

    def test_add_actor(self):
        movie = Movie("Moana", 2016, 1)
        movie.add_actor(Actor("Dwayne Johnson"))

        assert len(movie.actors) == 1
        assert movie.actors == [Actor("Dwayne Johnson")]

    def test_hash(self):
        movie1 = Movie("Moana1", 2016, 1)
        movie2 = Movie("Moana2", 2016, 2)
        movie3 = Movie("Moana3", 2016, 3)

        test_set = set()
        test_set.add(movie1)
        test_set.add(movie2)
        test_set.add(movie3)
        print()
        print(test_set)

    # extension test
    def test_add_rating_vote(self):
        movie = Movie("Moana", 2016, 7)
        movie.rating_votes = 5
        movie.external_rating = 6.2
        movie.add_rating_vote(8)
        print()
        print(f"Number of votes: {movie.rating_votes}")
        print(f"New rating for the movie: {movie.external_rating}")
        assert movie.external_rating == 6.5
        movie2 = Movie("ABC", 2016, 2)
        movie2.rating_votes = "2"
        movie2.external_rating = "2.5"
        movie2.add_rating_vote(10)
        assert movie2.external_rating == 5
        movie3 = Movie("", 0, 5)
        movie3.rating_votes = -1
        movie3.external_rating = "-2"
        movie3.add_rating_vote(10)
        assert movie3.external_rating == 10

    def test_revenue(self):
        movie = Movie("Moana", 2016, 7)
        movie.revenue = "23.6"
        assert movie.revenue == 23.6
        movie1 = Movie("Up", 2009, 8)
        movie1.revenue = "N/A"
        assert movie1.revenue is None
        movie2 = Movie("", 0, 1)
        movie2.revenue = 41.5
        assert movie2.revenue == 41.5
        movie3 = Movie("", 0, 1)
        movie3.revenue = -2
        assert movie3.revenue is None

    def test_metascores(self):
        movie = Movie("Moana", 2016, 7)
        movie.metascores = "23"
        assert movie.metascores == 23
        movie1 = Movie("Up", 2009, 8)
        movie1.revenue = "N/A"
        assert movie1.metascores is None
        movie2 = Movie("", 0, 1)
        movie2.metascores = 41
        assert movie2.metascores == 41
        movie3 = Movie("", 0, 1)
        movie3.metascores = -2
        assert movie3.metascores is None

    def test_ID(self):
        movie = Movie("Moana", 2016, 7)
        movie2 = Movie("Moana", 2016, 7)
        assert movie == movie2
        movie3 = Movie("Moana", 2016, 8)
        assert movie != movie3
