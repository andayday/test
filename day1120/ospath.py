#!/usr/bin/env python3

import os
filename = '/root/file'

print(os.path.abspath(filename))
print(os.path.basename(filename))
print(os.path.dirname(filename))
print(os.path.isfile(filename))

print(os.path.isdir(filename))
print(os.path.exists(filename))
print(os.path.join('/root', 'vim.txt'))
