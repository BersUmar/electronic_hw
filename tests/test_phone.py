from src.item import Item
from src.phone import Phone


def test_repr(some_phone):
    isinstance(repr(some_phone), str)
    assert repr(some_phone) == "Phone('Смартфон', 30000, 5, 2)"

def test_self(some_phone):
    isinstance(some_phone.name, str)
    isinstance(some_phone.price, int)
    isinstance(some_phone.quantity, int)
    isinstance(some_phone.number_of_sim, int)

def test_class(some_phone):
    issubclass(some_phone.__class__, Item)

def test_number_of_sim(some_phone):
    assert some_phone.number_of_sim >= 1
    some_phone.number_of_sim = 0
    assert ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

