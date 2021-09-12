from src.analysis import remove_words


def test_simple():
    input_text = 'test'
    result = remove_words(input_text)
    assert result == 'test'


def test_remove_one_words():
    input_text = 'a good test'
    result = remove_words(input_text)
    assert result == 'good test'


def test_remove_all_words():
    input_text = 'a any the'
    result = remove_words(input_text)
    assert result == ''


def test_difficult():
    input_text = 'A dog? Good luck! The biggest dog. Any colors. A big any the.'
    result = remove_words(input_text)
    assert result == 'dog? Good luck! biggest dog. colors. big.'
