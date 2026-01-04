class Account():
	def __init__(self, balance, account_no):
		self.balance = balance
		self.account_no = account_no

	def debit(self, amount):
		self.balance -= amount

	def credit(self, amount):
		self.balance += amount

	def print_balance(self):
		print(f"the balance for account number {self.account_no} is {self.balance}")

user1 = Account(100, 2345)
user1.credit(30)
user1.debit(12)
user1.print_balance()
