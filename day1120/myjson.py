#!/usr/bin/env python3

#dumps和loads分别执行了序列化和反序列化的操作，并且json序列化后的内容为字符串，所以文本的写入和读取不需要用二进制格式(pickle)
import json
course = {1:'Linux', 2:'Vim', 3:'Git'}
print(json.dumps(course))

with open('course.json', 'w') as file:
    file.write(json.dumps(course))

with open('course.json', 'r') as file:
    new_course = json.loads(file.read())
print(type(new_course))

