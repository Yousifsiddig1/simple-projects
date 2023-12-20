#Basic ATM 
class BankAccount:
    CURRENCY_CONVERSION_RATES = {
        'USD': 1.00,
        'EGP': 30.9,  
        'EUR': 0.85,
        'SAR': 3.75,

    }
    def __init__(self, name, AccNumber, balance=0, currency='USD'): 
        self.name = name
        self.AccNumber = AccNumber
        self.balance = balance
        self.currency = currency
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposit of {amount} {self.currency} successful.')
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal of {amount} {self.currency} successful.')
        else:
            print("Invalid withdrawal amount or insufficient funds.")
        self.display()
    def convert_currency(self, amount, to_currency):
        if amount > 0 and to_currency in self.CURRENCY_CONVERSION_RATES:
            conversion_rate = self.CURRENCY_CONVERSION_RATES[to_currency]
            converted_amount = amount * conversion_rate
            print(f'Converted {amount} {self.currency} to {converted_amount} {to_currency}.')
            self.display()
            return converted_amount
        else:
            print("Invalid amount or currency.")
    def transacation(self, amount, target_account):
        try:
            target_account.balance += amount
            self.balance -= amount
            print('Transaction Successful!')
            self.display()
        except :
            print(f'Error occured during the transaction')
    def display(self):
        print(f'Account Holder name: {self.name}\n\nAccount number: {self.AccNumber}\n\n'
              f'Account Balance: {self.balance} {self.currency}')
#Testing our class methods
# Example usage
person1 = BankAccount('Yousif ', '1111', 7867, 'USD') # made the account numbers short to test the transation method faster #
person2 =BankAccount('Mohamed', '2222',3446 ,'USD')

while True: # loop to ask the user which service he/she would like to use 
    service = input("1 to deposit, 2 to withdraw, 3 to convert, 4 to display,5 to transfer or 6 to exit: ").lower()
##############################################################################
    if service == '1': #deposit 
        amount = int(input("Enter the amount to deposit: "))
        accNo =input("\nEnter the account number you want to use :\n") # ask the user about their Account Number 
        if accNo =='1111':
            person1.deposit(amount)
        elif accNo == '2222':
            person2.deposit(amount)
    elif service == '2':
##############################################################################
        amount = int(input("Enter the amount to withdraw: ")) # withdraw 
        accNo =input("\nEnter the account number you want to use :\n")
        if accNo =='1111':
            person1.withdraw(amount)
        elif accNo == '2222':
            person2.withdraw(amount)
##############################################################################
    elif service == '3': # Convert curreny 
        to_currency = input("Enter the currency to convert to (EGP, EUR, SAR): ").upper()
        amount = int(input("Enter the amount to convert: "))
        accNo =input("\nEnter the account number you want to use :\n")
        if accNo =='1111':
            person1.convert_currency(amount , to_currency)
        elif accNo == '2222':
            person2.convert_currency(amount,to_currency)
#############################################################################
    elif service == '4': #display info
        accNo =input("\nEnter the account number you want to use :\n")
        if accNo =='1111':
            person1.display()
        elif accNo == '2222':
            person2.display()
##############################################################################
    elif service =='5': # transfer money 
        amount = int(input("Enter the amount to transfer: "))
        accNo=input("\nEnter the account number you want to send the money to:\n")
        if accNo=='1111':
            person2.transacation(amount,person1)
        elif accNo=='2222':
            person1.transacation(amount,person2)
##############################################################################
    elif service == '6':# exit
        print("Don\'t Forget to take your Credit Card 👍 \n" )
        break
    else:
        print("Invalid input, Try again ")
##############################################################################

