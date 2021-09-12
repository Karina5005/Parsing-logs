import re
import spacy


def remove_punct(input_text):
    return re.sub(r'[^\w\s]', '', input_text)


def text_to_sent(input_text):
    nlp = spacy.load("en_core_web_sm")
    return list(map(lambda x: x.text.strip(), nlp(input_text).sents))


def text_to_words(input_text):
    nlp = spacy.load("en_core_web_sm")
    return list(map(lambda x: x.text, nlp(input_text)))


def count_words(input_text):
    input_text = remove_punct(input_text).lower().split()
    return {i: input_text.count(i) for i in input_text}


def remove_words(input_text):
    nlp = spacy.load("en_core_web_sm")
    nlp.Defaults.stop_words.clear()
    nlp.Defaults.stop_words.update(["a", "any", "the"])
    return re.sub(r'\s([?.!"](?:\s|$))', r'\1',
                  ' '.join(list(filter(lambda y: not nlp.vocab[y].is_stop, text_to_words(input_text)))))


def count_sent(input_text, input_sent):
    sents = text_to_sent(input_text)
    return list(map(lambda x: remove_punct(x).lower(), sents)).count(
        remove_punct(text_to_sent(input_sent)[0]).lower())


def remove_sent_without_noun(input_text):
    nlp = spacy.load("en_core_web_sm")
    return ' '.join(list(map(lambda sent: sent.text, list(
        filter(lambda x: len(list(filter(lambda word: nlp(word)[0].pos_ == 'NOUN', x.text.split()))) > 0,
               nlp(input_text).sents)))))

