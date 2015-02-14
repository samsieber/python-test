__author__ = 'sam'

import argparse

from collections import Counter
from operator import itemgetter
import re


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()
input_file = args.input_file


with open(input_file, "r") as f:
    counts = Counter([word.lower() for line in f.readlines() for word in re.split("[\s.]+", line)])

counts[''] = 0
print max(counts.iteritems(), key=itemgetter(1))[0]