#bankoperations.py
from bankexcep import DepositError,WithdrawError,InSuffFundError
bal=500.00   #global variable
def   deposit():
	global bal
	damt=float(input("Enter How much amount you want to deposit :"))#ValueError
	if(damt<=0):
		raise DepositError
	else:
		bal=bal+damt
		print("\nur Account xxxxxx123 credited with INR :{}".format(damt))
		print("your Current Account Balance INR :{}".format(bal))

def   withdraw():
	global bal
	wamt=float(input("Enter How much amount you want to withdraw :")) #ValueError
	if(wamt<=0):
		raise WithdrawError
	elif(wamt+500>bal):
		raise InSuffFundError
	elif(wamt<=bal):
		bal=bal-wamt
		print("\nyour Account xxxxxx123 Debited with INR :{}".format(wamt))
		print("your Account Balance INR :{}".format(bal))

def  balenq():
		print("your Account Balance INR :{}".format(bal))
