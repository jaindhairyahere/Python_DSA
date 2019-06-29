class CreditCard:
	def __init__(self,customer,bank,acnt,limit,balance=0):
		self._customer= customer
		self._bank = bank
		self._acnt=acnt
		self._limit=limit
		self._balance=balance
	def get_customer(self):
		return self._customer
	def get_bank(self):
		return self._bank
	def get_acnt(self):
		return self._acnt
	def get_limit(self):
		return self._limit
	def get_balance(self):
		return self._balance
	def charge(self,price):
		if type(amount)!=type(1.0):
			raise TypeError		
		if price + self._balance>self._limit:
			return False
		else:
			self._balance +=price
			return True
	def make_payment(self,amount):
		if type(amount)!=type(1.0):
			raise TypeError
		if amount<0:
			raise ValueError
		self._balance -=amount
		return True
if __name__=='__main__':
	wallet=[]
	wallet.append(CreditCard("Dhairya","SBI",'180080006',800))
	wallet.append(CreditCard("Dhairya","Canara",'180080011',900))
	wallet.append(CreditCard("Dhairya","SBI Current",'180080006',1000))

for val in range(1,17):
	wallet[0].charge(val)
	wallet[1].charge(2*val)
	wallet[2].charge(3*val)

for c in range(3):
	print('Customer =', wallet[c].get_customer())
	print('Bank =', wallet[c].get_bank())
	print('Account =', wallet[c].get_acnt())
	print('Limit =', wallet[c].get_limit())
	print('Balance =', wallet[c].get_balance())
	while wallet[c].get_balance()>100:
		wallet[c].make_payment(100)
		print('New Balance =',wallet[c].get_balance())
	print()
print()

class PredatoryCreditCard(CreditCard):
	
	def __init__(self,customer,bank,acnt,limit,apr):
				'''Create a new predatory credit card instance.

 				The initial balance is zero.

 				customer 					the name of the customer (e.g., John Bowman )
 				bank 						the name of the bank (e.g., California Savings )
				acnt 						the acount identifier (e.g., 5391 0375 9387 5309 )
 				limit 						credit limit (measured in dollars)
 				apr 						annual percentage rate (e.g., 0.0825 for 8.25% APR)
 				'''
	#	super().__init__(self,customer,bank,acnt,limit)
	#	self._apr=apr
	def charge(self,price):
		success = super().charge(price)
		if not success:
			self._balance +=5
		return success
	def process_month(self):
		if self._balance>0:
			monthly_factor= pow(1+ self._apr, 1.0/12)
			self._balance *=monthly_factor	

class Bank:
	def __init__(self,name):
		self._Bank_name=name
	