#!/usr/bin/env python3
course = set()
print(type(course))
course = {}
print(type(course))
print(course)
print(type(course))
course = {'Linux', 'C++', 'Vim', 'Linux'}
print(course)
print('Linux' in course)
print('Python' not in course)

course.add('Python')
print('Python' not in course)
course.remove('Python')
#course.remove('Python')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)
print(set1.union(set2))
print(set1)
print(set1 - set2)

print(set1 ^ set2)
