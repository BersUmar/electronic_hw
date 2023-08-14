import pytest
from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone
@pytest.fixture()
def some_item():
    item = Item("Смартфон", 30000, 5)
    return item

@pytest.fixture()
def some_phone():
    phone = Phone("Смартфон", 30000, 5, 2)
    return phone\

@pytest.fixture()
def some_k():
    keyboard = Keyboard("Смартфон", 30000, 5)
    return keyboard
