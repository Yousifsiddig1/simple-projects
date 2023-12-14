# Basic ATM program class 
class BankAccount:
    CURRENCY_CONVERSION_RATES = {
        'USD': 1.00,
        'EGP': 30.9,  
        'EUR': 0.85,
        'SAR': 3.75,
    }

    def __init__(self, name, sex, AccNumber, balance=0, currency='USD'):
        self.name = name
        self.sex = sex
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

    def display(self):
        print(f'Account Holder name: {self.name}\nAccount number: {self.AccNumber}\n'
              f'Account Balance: {self.balance} {self.currency}')

# Example usage
person1 = BankAccount('Yousif ', 'Male ', '1234-8439-3242-1234', 100, 'USD')

while True:
    depOrWith = input("1 to deposit, 2 to withdraw, 3 to convert, 4 to display, or 5 to exit: ").lower()
    
    if depOrWith == '1':
        amount = int(input("Enter the amount to deposit: "))
        person1.deposit(amount)
    elif depOrWith == '2':
        amount = int(input("Enter the amount to withdraw: "))
        person1.withdraw(amount)
    elif depOrWith == '3':
        to_currency = input("Enter the currency to convert to (EGP, EUR, SAR): ").upper()
        amount = int(input("Enter the amount to convert: "))
        person1.convert_currency(amount, to_currency)
    elif depOrWith == '4':
        person1.display()
    elif depOrWith == '5':
        break
    else:
        print("Invalid input, Try again ")


