
class Genre:

    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.genre_name == other.genre_name:
            return True
        return False

    def __lt__(self, other):
        if self.genre_name < other.genre_name:
            return True
        return False

    def __hash__(self):
        return hash(self.genre_name)


class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Comedy")
        assert repr(genre1) == "<Genre Comedy>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(42)
        assert genre3.genre_name is None

    def test_lt(self):
        genre1 = Genre("Comedy")
        genre4 = Genre("Horror")
        genre_list = [genre4, genre1]
        genre_list.sort()
        assert genre_list[1] == genre4 and genre_list[0] == genre1
        genre5 = Genre("Comedian")
        genre_list2 = [genre1, genre5]
        genre_list2.sort()
        assert genre_list2[0] == genre5 and genre_list2[1] == genre1
