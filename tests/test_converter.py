import pytest
import attr


class Player(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score


@attr.s
class Card(object):
    player = attr.ib()
    person = attr.ib()
    name = attr.ib(default="")
    price = attr.ib(default=1.0)


@attr.s
class Person(object):
    age = attr.ib()
    bio = attr.ib(default="")

    @age.validator
    def greater_than_zero(self, attribute, value):
        if value < 0:
            raise ValueError("must be greater than zero")
        return value


player = Player("kobe", 81)
person_dict = {"age": 24, "bio": "NBA stars"}
person = Person(**person_dict)
card_dict = {"name": "foo", "price": 10, "player": player, "person": person}
card = Card(**card_dict)


# card.__attrs_attrs__
# card.__dict__
