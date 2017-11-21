#!/usr/bin/env python3

#序列化是指将内存中的对象转化为可以存储的格式
#最常用的两种方式序列化1、pickle模块 2、json模块


import pickle

course = {1:'Linux', 2:'Vim', 3:'Git'}
with open('./course.data', 'wb') as file:
    #pickle.dump(course, file)
    pass

with open('./course.data', 'rb') as file:
    #new_course = pickle.load(file)
    pass

#print(new_course)

#print(type(new_course))

