#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from natsort import natsorted, ns


def yes_no(fn) -> bool:
    ''' Asking what to do with the file '''
    answers = {'yes': True, 'y': True,
               'no': False, 'n': False}

    print('\033[91mDo you want to rename the file \033[1m%s\033[91m?\033[0;0m [y/n]' % fn)

    answer = input().lower()
    if answer in answers:
        return answers[answer]
    else:
        raise ValueError("Answer yes or no:")


def main(argv):
    filenames = natsorted(os.listdir(argv[1]), alg=ns.PATH)
    for fn, i in zip(filenames, enumerate(filenames)):
        fn = '%s%s' % (argv[1], fn)
        # Checking if the user want to rename given file
        if not yes_no(fn):
            continue
        else:
            pass

        # Renaming
        os.rename(fn, '%s%02d%s' % (argv[1], i[0], fn[-4:]))


if __name__ == '__main__':
    main(sys.argv)
