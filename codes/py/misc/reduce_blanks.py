#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import sys


def reduce_blanks(lines):
    output = []
    for x in lines:
        y = x
        if x.strip().startswith('-'):
            index = x.find('-')
            if index >= 3:
                y = ' ' * (index - 3) + x[index:]
        output.append(y)
    return output


def reduce_files(files):
    for f in files:
        print('reduce blanks on {}'.format(f))
        with open(f) as fh:
            output = reduce_blanks(fh)
        with open(f, 'w') as fh:
            fh.writelines(output)


def main():
    files = sys.argv[1:]
    reduce_files(files)


if __name__ == '__main__':
    main()
