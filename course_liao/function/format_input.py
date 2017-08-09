# -*- coding: utf-8 -*-

def format_word(word):
    if isinstance(word, str):
        return word[0].upper() + word[1:].lower()
    else:
        return word

L1 = ['adam', 'LISA', 'barT', 123, '1234']
L2 = list(map(format_word, L1))
print(L2)