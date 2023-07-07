from django import template
from .illegal_words import illegal_words

register = template.Library()

obscene_words = illegal_words


@register.filter
def censor_obscene(value):
    words = value.split()
    censored_words = []
    for word in words:
        if word.lower() in obscene_words:
            censored_word = word[0] + '*' * (len(word) - 1)
            censored_words.append(censored_word)
        else:
            censored_words.append(word)
    return ' '.join(censored_words)
