#!/usr/bin/env python3

a = 9
print("outside ",a)
def change():
	global a
	a = 90
	print(a)


if __name__ == '__main__':

	print("Before the function call ",a)
	print("inside change function", end=' ')
	change()
	print("after the function call ",a)

