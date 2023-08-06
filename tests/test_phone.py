from src.item import Item
from src.phone import Phone


def test_repr(some_phone):
    isinstance(repr(some_phone), str)
    assert repr(some_phone) == 'Phone("Смартфон", 30000, 5, 2))'

