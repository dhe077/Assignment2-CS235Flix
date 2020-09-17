
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, new_name):
        self.__director_full_name = new_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.director_full_name == other.director_full_name:
            return True
        return False

    def __lt__(self, other):
        if self.director_full_name < other.director_full_name:
            return True
        return False

    def __hash__(self):
        return hash(self.director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_lt(self):
        director1 = Director("Taika Waititi")
        director4 = Director("Spielberg")
        director_list = [director1, director4]
        director_list.sort()
        assert director_list[0] == director4 and director_list[1] == director1
        director5 = Director("Taika Zielberg")
        director_list2 = [director1, director5]
        director_list2.sort()
        assert director_list2[0] == director1 and director_list2[1] == director5
        director6 = Director("Taika")
        director_list3 = [director1, director6]
        director_list3.sort()
        assert director_list3[0] == director6 and director_list3[1] == director1

    def test_eq(self):
        director1 = Director("Cheesus")
        director2 = Director("Jeebus")
        director3 = Director("Cheesus")
        assert director1 != director2
        assert director1 == director3

    def test_hash(self):
        director1 = Director("Annabelle")
        hashed = hash(director1)
        assert director1.__hash__() == hashed
