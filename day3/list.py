#!/usr/bin/env python3
course = ["Linux", "Python", "Vim", "C++"]
course.append("PHP")
print(course);

course.insert(0, "Java")

print(course);

course.insert(1, "Ruby")

print(course);

print(course.count("Java"))

course.remove("Java")

print(course)
del course[-1]
print(course)
course.append("PHP")
print(course)
course.reverse()

print(course)

new_courses = ["BigData", "Cloud"]
course.extend(new_courses)
print(course)
course.sort()

print(course)
c = course.pop()
print
print(c)
print(course)
course.pop(0)
print(course)
