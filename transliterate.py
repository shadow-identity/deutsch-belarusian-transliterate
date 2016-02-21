#!/bin/python3
import csv
from collections import OrderedDict


def normalize(chars):
    return chars.strip(' -').lower()

words = [
    # 'Haidhausen',
    # 'Seghers',
    # 'Bodensee',
    'Kitzbühel',
    # Кіцбюэль
    'Tschöggelberg'
    # Чэґельбэрґ
]
# word = 'schauestaarauea'

words = map(lambda word: word.lower(), words)
strings = []
trans_dict = {}
with open('all.csv', 'r') as csv_file:
    csv_file = csv.reader(csv_file)
    for row in csv_file:
        for cell in row:
            if '=' in cell:
                cell = cell.split('=')
                bel = normalize(cell[1])
                germans = cell[0].split(',')
                germans = [normalize(value) for value in germans]
                trans_dict.update({ger: bel for ger in germans})
        strings.append(row)

sorted_trans_dict = OrderedDict(sorted(trans_dict.items(),
                                       key=lambda key: len(key[0]),
                                       reverse=True))

for word in words:
    for ger in sorted_trans_dict:
        while word.find(ger) != -1:
            word = word.replace(ger, sorted_trans_dict[ger], 1)
    print(word)
