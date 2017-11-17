#!/usr/bin/env python3
coursedict = {1:'Linux', 2:'Vim'}
print(coursedict)
print(coursedict[1])
print(coursedict[2])
testdict = {1:2, 'testdir':'shiyanlou', 9:[1,2,3]}
print(testdict)
print(testdict[1])
print(testdict['testdir'])
print(testdict[9])
dict_from_tuple = dict((('123', 'Linux'), (2, 'Vim')))
print(dict_from_tuple)

coursedict[5]='Bash'
coursedict[6]='Python'
print(coursedict)
del coursedict[1]
for key,value in coursedict.items():
	print(key, value);
coursedict.pop(2)
print(coursedict)

