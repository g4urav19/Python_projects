#atmdemo.py---main program
from atmmenu import menu
from bankexcep import DepositError,WithdrawError,InSuffFundError
from bankoperations import deposit,withdraw,balenq
import sys
while(True):
	try:
		menu()
		ch=int(input("Enter your Choice : "))
		if(ch==1):
			try:
				deposit()
			except DepositError:
				print("Don't Try to deposit  -ve / zero Values:")
			except ValueError:
				print("Don't  enter strs / special symbols and alpha-numerics for deposits")
		elif(ch==2):
			try:
				withdraw()
			except WithdrawError:
				print("Don't Try to Withdraw  -ve / zero Values:")
			except  InSuffFundError:
				print("U don't have sufficient Funds!")
			except  ValueError:
				print("Don't  enter strs / special symbols and alpha-numerics for withdarw")
		elif(ch==3):
			balenq()
		elif(ch==4):
			print("Thanks for using this ATM:")
			sys.exit()
		else:
			print("your Choice of Operation is wrong--try again")
	except ValueError:
		print("Don't enter strs / special symbols and alpha-numerics for choice of operation:")
