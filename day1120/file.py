#!/usr/bin/env python3

#r 只读模式打开,只读读取，不能编辑/删除文件内容
#w 写入模式打开，如果文件存在将会删除里面所有的内容，然后打开文件写入
#a 以追加模式打开，写入到文件中的任何数据将自动添加到末尾
#b 以二进制的方式打开

#file = open('/root/vim.txt')

#打印<class '_io.TextIOWrapper'>
#print(type(file))
#打印<_io.TextIOWrapper name='/root/vim.txt' mode='r' encoding='UTF-8'>
#print(file)


#with语句处理文件对象，会在文件用完后会自动关闭，就算发生异常也没有关系，它是try-finally块的简写
with open('/root/vim.txt') as file:
    count = 0
    for line in file:
        count += 1
    print(count)

#read 可以一次性读取整个文件的内容到字符串

filename = '/root/vim.txt'
file = open(filename)
print(file.read())
file.close()

#read读取整个文件，注意系统内存是否可以存取整个文件的内容,当read执行后，再次执行将不会有任何内容的输出
with open(filename) as file2:
    print(file2.read())
    #print(file2.read())#将不会有任何内容的输出

#readline() 用来每次读取文件的一行，readlines()可以读取所有行，但不同于read(),这个函数的返回的是一个列表，列表中每个元素都是文本文件中一行内容的字符串:

filename = '/root/file'
with open(filename) as file:
    print(file.readline(), end = '')
    print(file.readline())

filename = '/root/file'
with open(filename) as file:
    print(file.readlines())
'''
filename = input("Enter the file name: ")
with open(filename) as file:
    count = 0
    for line in file:
        count += 1
        print(line)
    print('Lines: ',count)
'''
filename = '/root/file'
with open(filename, 'w') as file:
    file.write('testline1')
    file.write('testline2')
with open(filename, 'a') as file:
    file.write('testline3')
    file.write('testline4')
    #print(file.readlines())#这样是不能执行的，会报错，可能没有数据可读

filename = '/root/file'
with open(filename) as file:
    print(file.readlines())

import sys

def copy_file(src, dst):
    with open(src, 'r') as src_file:
        with open(dst, 'w') as dst_file:
            dst_file.write(src_file.read())
        

if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1], sys.argv[2])
    else:
        print("Parameter Error")
        print(sys.argv[0], "srcfile dstfile")
        sys.exit(-1)
    sys.exit(0)

