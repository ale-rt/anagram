#!/usr/bin/env python
import sys
import tarfile

word = ''.join(sys.argv[1:]).lower()
word_key = set(word)
word_sorted = sorted(word)

with tarfile.open('italia-1a.gz') as tar:
    for member in tar.getmembers():
        lines = tar.extractfile(member).read().decode('utf8').lower().split()
        for line in lines:
            if sorted(line) == word_sorted:
                print(line)
