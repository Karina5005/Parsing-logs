from src.analysis import count_words


def test_simple():
    input_text = 'test'
    result = count_words(input_text)
    assert result == {'test': 1}


def test_two_different_words():
    input_text = 'good test'
    result = count_words(input_text)
    assert result == {'good': 1, 'test': 1}


def test_two_same_words():
    input_text = 'test test'
    result = count_words(input_text)
    assert result == {'test': 2}


def test_difficult():
    input_text = 'Hello! How are you? You look very good.'
    result = count_words(input_text)
    assert result == {'hello': 1, 'how': 1, 'are': 1, 'you': 2, 'look': 1, 'very': 1, 'good': 1}
