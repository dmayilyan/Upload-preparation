#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_armlet(word):
    ''' Get alitirated text of passed word '''

    letters = {'a': 'ա', 'b': 'բ', 'g': 'գ', 'd': 'դ', 'e': 'ե',
               'z': 'զ', 't': 'թ', 'j': 'ժ', 'i': 'ի', 'l': 'լ',
               'x': 'խ', 'ts': 'ծ', 'k': 'կ', 'h': 'հ', 'dz': 'ձ',
               'gh': 'ղ', 'm': 'մ', 'n': 'ն', 'sh': 'շ', 'o': 'ո',
               'ch': 'չ', 'p': 'պ', 's': 'ս', 'v': 'վ', 't': 'տ',
               'r': 'ր', 'c': 'ց', 'u': 'ու', 'q': 'ք', 'ev': 'և',
               'f': 'ֆ',
               '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
               '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
               '.': '.', '(': '(', ')':')'}

    new_word = ''.join(str(letters[i]) for i in word)

    return new_word
