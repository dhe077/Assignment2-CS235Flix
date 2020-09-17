from domainmodel.movie import Movie
from domainmodel.review import Review


class User:

    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, new_user_name: str):
        self.__user_name = new_user_name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str):
        self.__password = new_password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, new_watched_movies: list):
        self.__watched_movies = new_watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @reviews.setter
    def reviews(self, new_reviews: list):
        self.__reviews = new_reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies(self, new_time: int):
        if new_time >= 0:
            self.__time_spent_watching_movies_minutes = new_time

    def __repr__(self):
        return f"<User {self.user_name}>"

    def __eq__(self, other):
        if self.user_name == other.user_name:
            return True
        return False

    def __lt__(self, other):
        if self.user_name < other.user_name:
            return True
        return False

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie: Movie):
        if type(movie) == Movie:
            self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    # extension method
    def add_review(self, review: Review):
        if type(review) == Review:
            self.__reviews.append(review)
        review.movie.add_rating_vote(review.rating)


class TestUserMethods:

    def test_init(self):
        user1 = User('Martin', 'pw12345')
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        print()
        print(user1)
        print(user2)
        print(user3)

    def test_hash(self):
        user1 = User('Martin', 'pw12345')
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        test_set = set()
        test_set.add(user1)
        test_set.add(user2)
        test_set.add(user3)
        print()
        print(test_set)

    def test_watch_movie(self):
        user1 = User('Martin', 'pw12345')
        user1.watch_movie(Movie("Moana", 2016))
        print()
        print(user1.watched_movies)

        movies = [Movie("Moana", 2016), Movie("Guardians of the Galaxy", 2014)]
        movies[0].runtime_minutes = 107
        movies[1].runtime_minutes = 121
        user = User("Martin", "pw12345")
        print(user.watched_movies)
        print(user.time_spent_watching_movies_minutes)
        for movie in movies:
            user.watch_movie(movie)
        print(user.watched_movies)
        print(user.time_spent_watching_movies_minutes)

    def test_add_review(self):
        user1 = User('Martin', 'pw12345')
        movie = Movie("Moana", 2016)
        user1.add_review(Review(movie, "Ahhh", 2))
        print()
        print(user1.reviews)
        print(movie.external_rating)
