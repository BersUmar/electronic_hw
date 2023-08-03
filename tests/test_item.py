"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item


def test_repr(some_item):
    isinstance(repr(some_item), str)
    assert repr(some_item) == "Item('Смартфон', 30000, 5)"

def test_str(some_item):
    isinstance(str(some_item), str)
    assert str(some_item) == "Смартфон"

def test_item(some_item):
    assert some_item.name == "Смартфон"
    assert some_item.price == 30000
    assert some_item.quantity == 5


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 150000


def test_apply_discount(some_item):
    some_item.pay_rate = 0.9
    some_item.apply_discount()
    assert some_item.price == 27000


def test_name(some_item):
    some_item.name = 'Bers'
    isinstance(some_item.name, str)
    assert some_item.name == "Bers"
    assert some_item.name.isalpha()
    assert len(some_item.name) <= 10
    some_item.name = 'bersbersbers'
    assert some_item.name == 'bersbersbe'


def test_string_to_number(some_item):
    assert some_item.string_to_number('7') == 7


def test_instantiate_from_csv(some_item):
    new_item = some_item.instantiate_from_csv()
    assert new_item is None
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[2].name == 'Кабель'
    assert Item.all[3].name == 'Мышка'
    assert Item.all[4].name == 'Клавиатура'
    assert Item.all[0].price == 100.0
    assert Item.all[1].price == 1000.0
    assert Item.all[2].price == 10.0
    assert Item.all[3].price == 50.0
    assert Item.all[4].price == 75.0
    assert Item.all[0].quantity == 1
    assert Item.all[1].quantity == 3
    assert Item.all[2].quantity == 5
    assert Item.all[3].quantity == 5
    assert Item.all[4].quantity == 5
    # assert Item.all
    # some_item.instantiate_from_csv()
    # assert len(some_item.all) == 5
    # assert (new_item, csv.DictReader) == True
    # isinstance(some_item, Item)
