from src.analysis import count_sent


def test_simple():
    input_text = 'test.'
    result = count_sent(input_text, 'test.')
    assert result == 1


def test_empty_result():
    input_text = 'good test.'
    result = count_sent(input_text, 'test')
    assert result == 0


def test_two_same_sents():
    input_text = 'test. test.'
    result = count_sent(input_text, 'test.')
    assert result == 2


def test_difficult():
    input_text = 'Hello! You look very good. How are you? ' \
                 'You look very good. How are you? Hello! ' \
                 'You look very good. How are you? You look very good.'
    result = count_sent(input_text, 'How are you?')
    assert result == 3
