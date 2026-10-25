#!/usr/bin/env python
# coding=utf-8

files = [f.strip('\n') for f in open('_links.txt', 'r')]

count = 0
with open('new_links.txt', 'w') as f:
    for data in reversed(files):
        counter = '{:03d}'.format(count)
        f.write('{}|{}\n'.format(counter, data))
        count += 1
