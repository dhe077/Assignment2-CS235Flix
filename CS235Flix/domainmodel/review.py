from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = Movie("DEFAULT TITLE", 0)
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
        if 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @movie.setter
    def movie(self, new_movie: Movie):
        self.__movie = new_movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @review_text.setter
    def review_text(self, new_review_text):
        self.__review_text = new_review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        self.__rating = new_rating

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        self.__timestamp = new_timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__timestamp}>"

    def __eq__(self, other):
        if self.movie == other.movie and self.rating == other.rating and \
                self.review_text == other.review_text and self.timestamp == other.timestamp:
            return True
        return False


class TestReviewMethods:

    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        print(review.movie)
        print("Review: {}".format(review.review_text))
        print("Rating: {}".format(review.rating))

        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        movie1 = ""
        review_text1 = ""
        rating1 = 0
        review1 = Review(movie1, review_text1, rating1)

        assert review1.rating is None
        assert review1.review_text is None
        movieEx = Movie("DEFAULT TITLE", 0)
        print(movieEx)

    def test_repr(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        print()
        print(review)

    def test_eq(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        movie2 = Movie("Moana", 2016)
        review_text2 = "This movie was very enjoyable."
        rating2 = 8
        review2 = Review(movie2, review_text2, rating2)
        assert review == review2
        movie3 = Movie("Moana", 2017)
        review_text3 = "This movie was very enjoyable."
        rating3 = 8
        review3 = Review(movie3, review_text3, rating3)
        assert review != review3
        movie4 = Movie("", 0)
        review_text4 = ""
        rating4 = 0
        review4 = Review(movie4, review_text4, rating4)
        assert review != review4

    def test_getters_setters(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        assert review.rating == 8
        assert review.movie == movie
        assert review.review_text == "This movie was very enjoyable."
