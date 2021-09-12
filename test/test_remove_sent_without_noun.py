from src.analysis import remove_sent_without_noun


def test_simple():
    input_text = 'test.'
    result = remove_sent_without_noun(input_text)
    assert result == 'test.'


def test_remove_nothing():
    input_text = 'a good test.'
    result = remove_sent_without_noun(input_text)
    assert result == 'a good test.'


def test_remove_all_words():
    input_text = 'a any the'
    result = remove_sent_without_noun(input_text)
    assert result == ''


def test_difficult():
    input_text = 'A dog? Good! The biggest. Any colors.'
    result = remove_sent_without_noun(input_text)
    assert result == 'A dog? Any colors.'
