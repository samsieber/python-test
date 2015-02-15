__author__ = 'sam'

import argparse


def reverse_string(string):
    return string[::-1]


def binary(value):
    rev_answer = ""
    while value > 0:
        rev_answer += '0' if (value % 2 == 0) else '1'
        value /= 2
    return reverse_string(rev_answer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number")
    args = parser.parse_args()
    try:
        number = int(args.number)
        print binary(number)
        print hex(number)
    except ValueError as ve:
        print "You gave an non-integer decimal number (%s). We require a whole number." % args.number


