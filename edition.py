#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
from natsort import natsorted, ns

from aliterator import get_armlet


def make_bold(w):
    ''' Make it Bold'''
    return '<strong>' + w + '</strong>'


def add_player(dirname):
    ''' Add Player code '''
    return '[audioplayer file="http://url/qwe.mp3" rightbg="27CDA5" transparentpagebg="yes"]' % dirname


def modify(fn):
    ''' Generating the text from each filename'''
    if '.' in fn[-4:]:
        fn = fn[:-4]
    alit_word = get_armlet(fn)
    alit_word = alit_word.capitalize()

    index = 0
    digit = re.search('\d', alit_word)
    if digit:
        index = digit.start()
        alit_word = alit_word[:index] + ' ' + alit_word[index:]

    index += 2
    index_old = index
    digit = re.search('\d', alit_word[index:])
    if digit:
        index = digit.start() + index_old
        alit_word = alit_word[:index] + ' ' + alit_word[index:]

    mas = re.search('մաս', alit_word)
    if mas:
        index = mas.start()
        alit_word = alit_word[:index] + '. ' + alit_word[index:]

    return alit_word


def main(argv):
    ''' Looping through filenames and printing '''
    dirname = argv[1]
    dirname = dirname[2:-1]
    with open("up.txt",'w') as f:
        for fn in natsorted(os.listdir(dirname), alg=ns.PATH):
            lit_fn = modify(fn)
            print(make_bold(lit_fn))
            f.write(make_bold(lit_fn))
            print()
            f.write('\r\n')
            f.write('\r\n')
            print(add_player(dirname))
            f.write(add_player(dirname))
            f.write('\r\n')
            f.write('\r\n')
            print()


if __name__ == '__main__':
    main(sys.argv)
