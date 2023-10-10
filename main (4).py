'''implement a class called bank account that represents a Bank account.
   the class should have private attributes for account number,
   account holder name, and account balance.
   include methods to deposit money, withdraw money.and display
   the account balance.ensure that the
   account balance cannot be accessed divectly from outside the class.
   write a program to create an instance of the bank aaccount class and test the deposit and withdrawel functionlaity.'''
   
class BankAccount:  
  def--init--(self ,account-number, account-holder-name ,initial-balance =0.0):            


 self.-account-number=account number
 self.-account-holder-name=account-holder-name  
 self.-account-balance=initial-balance   
def deposit(self,amount):
  if amount>0:
    self.-account-balance+=account
    print(f" deposited ${amount}.New balance:${self.-account-balance}")
  else:
    print("invalid deposit amount.Amount must be greater than 0.")
    def display-balance(self):
print(f" Account Balance for{self.-account-holder-name}:${self.-account-balance}")
# create an instance of the BankAccount class
account 1=BankAccount("123456789","john Doe")
# deposit money into the account account1.deposit(1000)
# Display the account balance account1.display-balance()
# Attempt to access the account balance directly(Will not work)
# print(account1.-account-balance)




   
  