def test_lg(some_k):
    assert some_k.language == 'EN'

def test_self(some_k):
    assert some_k.name == 'Смартфон'
    assert some_k.price == 30000
    assert some_k.quantity == 5

def test_lang(some_k):
    some_k.change_lang()
    assert some_k.language == 'RU'
    some_k.change_lang()
    assert some_k.language == 'EN'

