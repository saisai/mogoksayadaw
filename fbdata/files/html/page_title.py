#!/usr/bin/env python
# coding=utf-8

#<li><a rel="external" href="pages/000.html"><p><strong>000</strong></p></a></li>


for data in range(0, 299):
    counter = '{:03d}'.format(data)
    print('<li><a rel="external" href="pages/{}.html"><p><strong>{}</strong></p></a></li>'.format(counter, counter))