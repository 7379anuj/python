#program for bank account
class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening  = date_of_opening 
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("has been withdrawn from your account.",amount)
            
    def check_balance(self):
        print(f"Current balance is $.",self.balance)
        
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print("Balance: /n",self.balance)   


ac_no_1 = BankAccount(2345, "01-01-2011", 1000, "anujpandey")


print("Customer Details:")
ac_no_1.print_customer_details()
