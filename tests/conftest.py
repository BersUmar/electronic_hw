import pytest
from src.item import Item

@pytest.fixture()
def some_item():
    item = Item("смартфон", 30000, 5)
    return item

