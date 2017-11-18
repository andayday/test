#!/usr/bin/env python3

#这个是默认传参之后，不要再有参数了
#def connect(ipaddress, port = 22, macaddress):
def connect(ipaddress, port = 22):
	print("IP: ", ipaddress)
	print("Port: ", port)
#传可变参数的用法，0个或者多个参数port
def connect1(ipaddress, *ports):
	print("IP: ", ipaddress)
	for port in ports:
		print("Port: ", port)
#pyhton参数无类型
'''
不可变对象 ：数值、字符串、元组等 相当于值传递，函数中对该参数的修改不会保留
可变对象：列表、字典 相当于传引用，函数中的修改会保留
'''
def connect2(ipaddress, ports):
	print("IP: ", ipaddress)
	print("Ports ", ports)
	ipaddress = '10.10.10.1'
	ports.append(8000)

	
#name = 'User' 这是默认传参
# * 这个是把控制传参顺序，带上名字  name = 'antian'
def hello(*, name = 'User'):
	print("Hello ", name)

#默认值是任何可变对象时，例如列表、字典、大多数类的实例，这函数调用过程中会累计 f(1) f(2)1 2 
def f(a, data = []):
	data.append(a)
	return data

#print(f1(1)) 1 print(f1(2)) 2 不会再data 上追加
def f1(a, data = None):
	if data is None:
		data = []
	data.append(a)
	return data

if __name__ == '__main__':

	connect('192.168.1.11', 22)
	connect(22, '192.168.1.11')
	connect(port = 22, ipaddress = '192.168.1.11')
	connect('192.168.1.12')
#hello('shiyanlou')
	hello(name = 'shiyanlou')
	hello()
	print(f(1))
	print(f(2))
	print(f(3))
	print(f1(1))
	print(f1(2))
	print(f1(3))
	connect1('192.168.1.1', 22, 23, 24)
	connect1('192.168.1.1')
	print("=======================")
	ipaddress = '192.168.1.1'
	ports = [22, 23, 24]
	print("Before connect:")
	print("IP: ",ipaddress);
	print("In connect:")
	connect2(ipaddress, ports)	
	print("After connect:")
	print("IP: ",ipaddress)
	print("Ports: ",ports)
