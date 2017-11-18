#!/usr/bin/env python3
import sys

def Arg2Salary(args):
	dict_salary = { };
	for arg in args:
		em_salary = arg.split(':')
		try:
			temp = int(em_salary[1])
		except ValueError:
			print("Salary Type Return Error")
			sys.exit()
		dict_salary[em_salary[0]] = temp
	return dict_salary

#返回税后工资
def SalaryCalc(Salary):
	#参数判断
	
	if Salary <= 0:
		print("Param is Invaliad")
		return -1
	
	#交完五险一金的薪水
	Actual_Base = Salary - Salary * 0.165

	#不用纳税的分支
	if Actual_Base <= 3500:
		return Actual_Base 

	tmp = Actual_Base
	#纳税的分支
	Actual_Base = Actual_Base - 3500 
	if Actual_Base <= 1500:
		Actual_Base = (format((Actual_Base*0.03 - 0),".2f")	)
	elif Actual_Base > 1500 and Actual_Base <= 4500:
		Actual_Base = (format((Actual_Base*0.03 - 105),".2f")	)
	elif Actual_Base > 4500 and Actual_Base <= 9000:
		Actual_Base = (format((Actual_Base*0.03 - 555),".2f")	)
	elif Actual_Base > 9000 and Actual_Base <= 35000:
		Actual_Base = (format((Actual_Base*0.03 - 1005),".2f"))
	elif Actual_Base > 35000 and Actual_Base <= 55000:
		Actual_Base = (format((Actual_Base*0.03 - 2755),".2f"))
	elif Actual_Base > 55000 and Actual_Base <= 80000:
		Actual_Base = (format((Actual_Base*0.03 - 5055),".2f"))
	else:
		Actual_Base = (format((Actual_Base*0.03 - 13550),".2f"))
		
	Actual_Base = tmp - float(Actual_Base)
	format(Actual_Base, ".2f")
	return Actual_Base


if __name__ == '__main__':
	Dict_ActualSalary = {}
	
	#提取命令行
	Dict_Salary = Arg2Salary(sys.argv[1:])

	for em_num,salary in Dict_Salary.items():
		Dict_ActualSalary[em_num] = SalaryCalc(salary)
		print(em_num, Dict_ActualSalary[em_num])
'''
Arg_Count = len(sys.argv)
if __name__ == '__main__':
	if Arg_Count != 2:
		print("param num error")
		sys.exit()
try:
	Salary = int(sys.argv[1])	
except ValueError:
	print("Please Input Salary Type")
	sys.exit()
if Salary <= 3500:
	print("NoUpLimit")
	sys.exit()
Actual_Base = Salary - 3500
if Actual_Base <= 1500:
	print(format((Actual_Base*0.03 - 0),".2f")	)
elif Actual_Base > 1500 and Actual_Base <= 4500:
	print(format((Actual_Base*0.03 - 105),".2f")	)
elif Actual_Base > 4500 and Actual_Base <= 9000:
	print(format((Actual_Base*0.03 - 555),".2f")	)
elif Actual_Base > 9000 and Actual_Base <= 35000:
	print(format((Actual_Base*0.03 - 1005),".2f"))
elif Actual_Base > 35000 and Actual_Base <= 55000:
	print(format((Actual_Base*0.03 - 2755),".2f"))
elif Actual_Base > 55000 and Actual_Base <= 80000:
	print(format((Actual_Base*0.03 - 5055),".2f"))
else:
	print(format((Actual_Base*0.03 - 13550),".2f"))
'''
