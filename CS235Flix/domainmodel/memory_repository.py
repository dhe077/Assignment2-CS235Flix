
class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._users = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username):
        return (user for user in self._user if user == username)

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.ID] = movie

    def get_movie(self, id):
        movie = None
        try:
            movie = self._movies_index[id]
        except KeyError:
            pass

    def get_number_of_movies(self) -> int:
        return len(self._movies)

    def get_first_movie(self) -> Movie:
        return self._movies[0]

    def get_last_movie(self) -> Movie:
        return self._movies[-1]

    def get_movies_by_id(self, ID_list: List[int]):
        movies_by_id = list()
        for movie in self._movies:
            if movie.ID in ID_list:
                movies.append(movie)
        return movies_by_id

    def get_movies_by_title(self, keyword) -> List[Movie]:
        movies_by_title = list()
        for movie in self._movies:
            if keyword in movie.title:
                movies_by_title.append(movie)
        return movies_by_title

    def get_movies_by_director(self, target_director: Director) -> List[Movie]:
        movies_by_director = list()
        for movie in self._movies:
            if movie.director == target_director:
                movies_by_director.append(movie)
        return movies_by_director

    def get_movies_by_genre(self, target_genre: Genre) -> List[Movie]:
        movies_by_genre = list()
        for movie in self._movies:
            if target_genre in movie.genres:
                movies_by_genre.append(movie)
        return movies_by_genre

    def get_movies_by_actor(self, target_actor: Actor) -> List[Movie]:
        movies_by_actor = list()
        for movie in self._movies:
            if target_actor in movie.actors:
                movies_by_actor.append(movie)
        return movies_by_actor

    def get_movies_by_rating_high(self) -> List[Movie]:
        high_to_low_movies = list()
        # find the highest rating movie then work your way down to the lowest
        copy_of_movies = self._movies.copy()
        highest = copy_of_movies[0]
        while len(copy_of_movies) != 0:
            for i in range(len(copy_of_movies)):
                if copy_of_movies[i].external_rating > highest.external_rating:
                    highest = copy_of_movies.pop(i)
            high_to_low_movies.append(highest)
        return high_to_low_movies

    def get_movies_by_rating_low(self) -> List[Movie]:
        low_to_high_movies = list()
        # find the lowest rating movie then work your way up to the highest
        copy_of_movies = self._movies.copy()
        lowest = copy_of_movies[0]
        while len(copy_of_movies) != 0:
            for i in range(len(copy_of_movies)):
                if copy_of_movies[i].external_rating < lowest.external_rating:
                    highest = copy_of_movies.pop(i)
            high_to_low_movies.append(lowest)
        return high_to_low_movies

    def get_title_of_previous_movie(self, movie: Movie):
        pass

    def get_title_of_next_movie(self, movie: Movie):
        pass