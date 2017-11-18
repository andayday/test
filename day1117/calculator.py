#!/usr/bin/env python3
import sys

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






