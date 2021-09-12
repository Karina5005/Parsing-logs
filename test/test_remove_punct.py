from src.analysis import remove_punct


def test_simple():
    input_text = 'test'
    result = remove_punct(input_text)
    assert result == 'test'


def test_remove_one_punct():
    input_text = 'a good test.'
    result = remove_punct(input_text)
    assert result == 'a good test'


def test_remove_all_words():
    input_text = '.?,'
    result = remove_punct(input_text)
    assert result == ''


def test_difficult():
    input_text = 'A dog? Good luck! The biggest dog. Any colors.'
    result = remove_punct(input_text)
    assert result == 'A dog Good luck The biggest dog Any colors'
