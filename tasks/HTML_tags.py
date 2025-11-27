from re import *
from collections import defaultdict

d = defaultdict(set)
for i in open(0):
    for j in i.split('>'):
        match = search(r'<(\w+)', j)
        if match:
            d[match.group(1)].update(set(findall(r'\s([^ ]+?)=', j)))

for key, value in sorted(d.items()):
    print(f'{key}: {", ".join(sorted(value))}')