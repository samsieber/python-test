__author__ = 'sam'

import argparse

def reverse_string(string):
    return string[::-1]

def hex(number):
    return "%x" % number

def binary(number):
    number = int(number)
    rev_answer = ""
    while number > 0:
        rev_answer += '0' if (number % 2 == 0) else '1'
        number /= 2
    return reverse_string(rev_answer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    number = float(args.input_file)
    print binary(number)
    print hex(number)


