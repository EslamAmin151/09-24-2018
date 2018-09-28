from random import randint

class Customer:
	def __init__(self,first_name,last_name):

		self.first_name = first_name
		self.last_name = last_name

	def print_customer_name(self):
		print(f"Hi {self.first_name} {self.last_name}")


class BankAccount:
	def __init__(self,account_number,account_type,customer,balance,status):

		self.account_number = account_number
		self.account_type = account_type
		self.customer = customer
		self.balance = balance
		self.status = status

	def showAccountInfo(self):
		print("Here's your account information.)
		print("\tAccount type: (self.account_type)")
		print("\tAccount status: (self.status)")
		print("\tAccount balance: $(self.balance)")

	def transfer(self,amount,toAccount):

		print("transfering funds...")
		toAccount.balance += amount

	def deposit_funds(self,amount,account_type):
		print("How much money would you like to deposit?")
		account_type.balance += amount


	def withdraw_funds(self,amount):
		if amount > self.balance:

			print("""Withdrawing {amount} dollars will overdraw your account
				and a $35.00 fee will be charged to your account.
				 """)
			answer = input("Would you like to proceed? (Y/N): \n").lower()
			if answer == "y":
				self.balance -= amount
			else:
				print("What you wou")
	def balance(self, balance):
		self.balance += initial_deposit


prompt1 = None
while prompt1 != 'q':
	print("/////////////////////////////////////////////////////////")
	print("*************** Welcome to Bank,*************")
	print("                                                         ")
	print("\tPress '1' to open a new account")
	print("                                                         ")
	print("\tPress 'q' to quit application")
	print("----------------------------------------------------------")
	prompt1 = int(input())
	print("\tYou request is processing... Please wait")
	if prompt1 == 1:
		acct_type = input(print("""Awesome! Would you like to open a Savings Account or a Checking Account?
			Enter 'S' for Savings or 'C' for Checking"""))
		print("Processing youre request... Please wait")
		print("\tExcellent choice!")
		user_first_name = input(print("What is your first name?")).title()
		user_last_name = input(print("What is your last name?")).title()
		initial_deposit = input(print("What is your initial deposit amount?"))
		account_number = randint(00000,99999)

		if acct_type == 'S'.lower():
			acct_type == 'Savings Account'
			user1 = Customer(user_first_name,user_last_name)
			balance = initial_deposit
			status = 'open'



		else:
			acct_type == 'Checking Account'
			user1 = Customer(user_first_name,user_last_name)
			checking_account = (acct_type,account_number,initial_deposit)
			#print(f"Great! Here's your newly created Checking Account#: {account_number}")

	else:
		print("Press '2' to check your balance")
		print("Press '3' to make a deposit")
		print("Press '4' to withdraw funds")
		print("Press '5' to transfer funds")
		print("Press '0' to log-off")
		prompt2 = int(input())
		print("\tYou request is processing... Please wait")

		if prompt2 == 2:
			balance = BankAccount()
	print(f"Great! Here's your newly created Checking Account#: {account_number}")


savings_account = BankAccount(account_number,acct_type,user1,balance,status)
savings_account.showAccountInfo()
