# still working on it ^^
# I used the sqlite3 library to create a database and store the bank account information in it.
# I used the Basic Atm project to create the bank account class and its methods. 
import sqlite3 as sq 
class Bank:
    CURRENCY_CONVERSION_RATES = {
        'USD': 1.00,
        'EGP': 30.9,  
        'EUR': 0.85,
        'SAR': 3.75,

    }
    def __init__(self, name, AccNumber, balance,currency):
        self.name = name
        self.AccNumber = AccNumber
        self.balance = balance
        self.currency = currency
        self.conn = sq.connect('bank.db')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists bank (name text, AccNumber integer, Balance integer)')
    def insert(self): # insert data into the database
        # execute the insert command
        self.cur.execute('insert into bank values(?,?,?)',(self.name, self.AccNumber, self.balance))
        self.conn.commit() # commit the changes
    def update(self): # update data in the database
        self.cur.execute('update bank set Balance = ? where AccNumber = ?',(self.balance, self.AccNumber))
        self.conn.commit()
    def delete(self): # delete data from the database
        self.cur.execute('delete from bank where AccNumber = ?',(self.AccNumber,))
        self.conn.commit()
    def display(self):
        self.cur.execute('select * from bank')
        print(self.cur.fetchall())
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
        print(f'Account Holder name: {self.name}\n\nAccount number: {self.AccNumber}\n'
              f'Account Balance: {self.balance} {self.currency}')
#Testing our class methods  [You can add more accounts if you want]
b1 = Bank('Yousif', 1111, 10000, 'USD')
b2 = Bank('Mohamed', 2222, 20000, 'USD')
b3 = Bank('Ali', 3333, 30000, 'USD')

while True: # loop to ask the user which service he/she would like to use 
    service = input("1 to deposit, 2 to withdraw, 3 to convert, 4 to display,5 to transfer or 6 to exit: ").lower()

    if service == '1': #deposit 
        amount = int(input("Enter the amount to deposit: "))
        accNo = input("\nEnter the account number you want to use:\n") # ask the user about their Account Number 
        if accNo == '1111': # check the account number and deposit the amount to the right account
            b1.deposit(amount) 
        elif accNo == '2222':
            b2.deposit(amount)
        elif accNo == '3333':
            b3.deposit(amount)
        else:
            print("Invalid account number.")
    elif service == '2':
        amount = int(input("Enter the amount to withdraw: ")) # withdraw 
        accNo = input("\nEnter the account number you want to use:\n")
        if accNo == '1111':
            b1.withdraw(amount)
        elif accNo == '2222':
            b2.withdraw(amount)
        elif accNo == '3333':
            b3.withdraw(amount)
        else:
            print("Invalid account number.")
    elif service == '3': # Convert currency 
        to_currency = input("Enter the currency to convert to (EGP, EUR, SAR): ").upper()
        amount = int(input("Enter the amount to convert: "))
        accNo = input("\nEnter the account number you want to use:\n")
        if accNo == '1111':
            b1.convert_currency(amount, to_currency)
        elif accNo == '2222':
            b2.convert_currency(amount, to_currency)
        elif accNo == '3333':
            b3.convert_currency(amount, to_currency)
        else:
            print("Invalid account number.")
    elif service == '4': # display info
        accNo = input("\nEnter the account number you want to use:\n")
        if accNo == '1111':
            b1.display()
        elif accNo == '2222':
            b2.display()
        elif b3.display():
            b3.display()
        else:
            print("Invalid account number.")
    elif service == '5': # transfer money 
        amount = int(input("Enter the amount to transfer: ")) # ask the user about the amount to transfer
        accNo = input("\nEnter the account number you want to send the money to:\n")
        if accNo == '1111': # check the account number and transfer the amount to the right account
            b2.transacation(amount, b1)
        elif accNo == '2222':
            b1.transacation(amount, b2)
        elif accNo == '3333':
            b3.transacation(amount, b1)
        else:
            print("Invalid account number.")    
    elif service == '6': # exit
        print("Don't Forget to take your Credit Card 👍 \n")
        break
    else:
        print("Invalid input, Try again ")
b1.insert()
b2.insert()
b3.insert()

##############################################################################

