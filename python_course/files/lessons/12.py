#!/usr/bin/env python3

with open('file2.txt', 'w') as the_file:
    the_file.write('This text will be written to the file.\n')
    the_file.write('Here is more text.\n')

with open('file2.txt') as the_file:
    print(the_file.read())
