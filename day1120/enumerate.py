#!/usr/bin/env python3
import sys

print("Program:", sys.argv[0])
print("Parameters:")

#列表中循环，索引位置和对应值可以使用它同时得到
for i,x in enumerate(sys.argv):
    if (i == 0):
        continue
    print(i, x)


