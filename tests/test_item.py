"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item(some_item):
    assert some_item.name == "смартфон"
    assert  some_item.price == 30000
    assert some_item.quantity == 5
def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 150000

def test_apply_discount(some_item):
    some_item.pay_rate = 0.9
    some_item.apply_discount()
    assert some_item.price == 27000
