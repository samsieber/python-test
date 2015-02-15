__author__ = 'sam'

import argparse

from collections import Counter
from operator import itemgetter
import string
import re


def get_letters(sentence):
    return [letter for letter in "".join(re.findall("[a-zA-Z]+", sentence)).lower()]


def evaluate_sentence(sentence):
    letter_counts = Counter(get_letters(sentence))
    return sum([letter_counts.get(letter, 0) * (value_0_based+1) for (value_0_based, letter) in enumerate(string.ascii_lowercase)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    with open(args.input_file, "r") as input_file:
        cleaned = ("".join(input_file.readlines()).replace("\n", " ").replace("\r", ""))
        #   I could theoretically just split on "  " instead of ".  "
        #  but your test doesn't show the period at the end of the sentence;
        #  therefore, I'll go with ".  ", because splitting that way eats the period,
        #  just as shown in the test
        sentences = cleaned.split(".  ")
        values = {sentence: evaluate_sentence(sentence) for sentence in sentences}
        best = max(values.iteritems(), key=itemgetter(1))
        print best[0] + ", " + str(best[1])

