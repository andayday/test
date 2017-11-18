#!/usr/bin/env python3

def char_count(str, char):
	return str.count(char)
def count_char(str):
	#生成集合，为了遍历去重
	char_list = set(str)
	for char in char_list:
		print(char, str.count(char))
def count_char2(str):
	countdict = {}
	for char in str:
		c = countdict.get(char)
		if c is None:
			countdict[char] = 1
		else:
			countdict[char] += 1
	print(countdict)

if __name__ == '__main__':
	result = char_count('shiyanlou.com', 's')
	print(result)
	count_char('shiyanlou.com')
	count_char2('shiyanlou.com')

