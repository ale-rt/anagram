#!/usr/bin/env python
import sys
import tarfile
ita_dict = {}

# this is CPU waste... but the mapping can be useful for a future version
with tarfile.open(u'italia-1a.gz', 'r:gz') as tar:
    for member in tar.getmembers():
        for line in tar.extractfile(member).read().decode('utf8').split():
            line = str(line.strip().lower())
            key = ''.join(sorted(set(line)))
            ita_dict.setdefault(key, []).append(line)

word = "".join(sys.argv[1:]).lower()
word_key = ''.join(sorted(set(word)))
word_sorted = sorted(word)

for possible_match in ita_dict.get(word_key, []):
    if sorted(possible_match) == word_sorted:
        print(possible_match)
