from domainmodel.movie import Movie

class WatchList:

    def __init__(self):
        self.__movie_watchlist = []
        self.__index = 0


    @property
    def movie_watchlist(self) -> list:
        return self.__movie_watchlist

    @movie_watchlist.setter
    def movie_watchlist(self, new_watchlist: list):
        self.__movie_watchlist = new_watchlist

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.movie_watchlist):
            self.__index = 0
            raise StopIteration
        self.__index += 1
        return self.__movie_watchlist[self.__index - 1]

    def add_movie(self, movie: Movie):
        if type(movie) == Movie:
            if movie not in self.__movie_watchlist:
                self.__movie_watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if type(movie) == Movie:
            if movie in self.__movie_watchlist:
                self.__movie_watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if 0 <= index < len(self.__movie_watchlist):
            return self.__movie_watchlist[index]
        return None

    def size(self):
        return len(self.movie_watchlist)

    def first_movie_in_watchlist(self):
        if self.size() >= 1:
            return self.movie_watchlist[0]
        return None


class TestWatchlistMethods:

    def test_init(self):
        watchlist = WatchList()
        print()
        print(f"Size of watchlist: {watchlist.size()}")

    def test_add_movie(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print()
        print(watchlist.first_movie_in_watchlist())

    def test_check_size_of_nonempty_watchlist(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print()
        print(f"Size of watchlist is: {watchlist.size()}")

    def test_add_same_movie_again(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Moana", 2016))
        print()
        print(f"Size of watchlist is: {watchlist.size()}")

    def test_remove_movie_which_is_not_in_watchlist(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.remove_movie(Movie("Ice Age", 2002))
        print()
        print(f"Size of watchlist is: {watchlist.size()}")

    def test_remove_movie_which_is_in_watchlist(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.remove_movie(Movie("Moana", 2016))
        print()
        print(f"Size of watchlist is: {watchlist.size()}")

    def test_select_movie_to_watch_index_ok(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print()
        print(f"Selected movie: {watchlist.select_movie_to_watch(0)}")

    def test_select_movie_to_watch_index_out_of_bounds(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print()
        print(f"Selected movie: {watchlist.select_movie_to_watch(9)}")

    def test_iterator_used(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print()
        for movie in watchlist:
            print(movie)

