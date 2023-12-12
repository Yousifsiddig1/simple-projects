# Basic ATM program class 
class BankAccount:
    CURRENCY_CONVERSION_RATES = {
        'USD': 1.00,
        'EGP': 30.9,  
        'EUR': 0.85,
        'SAR': 3.75,
    }
    def __init__(self,name,sex,AccNumber,balance = 0, currency='USD'):
        self.name = name
        self.sex = sex
        self.AccNumber= AccNumber
        self.balance = balance
        self.currency= currency
    def deposit(self,amount):
        if  amount > 0:
            self.balance += amount
        print(f'Account Holder name : {self.name}\n Account number : {self.AccNumber} \n Account Balance : {self.balance} {self.currency}')
        return self.balance
    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount
        print(f'Account Holder name : {self.name}\n Account number : {self.AccNumber} \n Account Balance : {self.balance} {self.currency}')

        return self.balance
    def convert_currency(self, amount, to_currency):
            if amount > 0 and to_currency in self.CURRENCY_CONVERSION_RATES:
                conversion_rate = self.CURRENCY_CONVERSION_RATES[to_currency]
                converted_amount = amount * conversion_rate
                print(f'Account Holder name : {self.name}\n Account number : {self.AccNumber} \n Account Balance : {converted_amount} {self.currency}')

                return converted_amount
            else:
                print("Invalid amount or currency.")
    def display(self):
        print(f'Account Holder name : {self.name}\n Account number : {self.AccNumber} \n Account Balance : {self.balance} {self.currency}')
person1 =BankAccount('Yousif ','Male ','1234-8439-3242-1234', 100,'USD')
while True:
    depOrWith = input(" 1 to deposit or 2 to withdraw or 3 to convert or 4 to display:").lower()
    if depOrWith == '1':
        amount = int(input("Enter the amount to deposit:"))
        person1.display()
        break
    elif depOrWith =='2':
        amount = int(input("Enter the amount to withdraw:"))
        person1.display()
        break
    elif depOrWith == '3':
        to_currency = input("Enter the currency to convert to (EGP, EUR, SAR): ").upper()
        amount = int(input("Enter the amount to convert : "))
        converted_amount = person1.convert_currency(amount, to_currency)
        person1.balance = converted_amount  # Update the balance with the converted amount
        person1.currency = to_currency  # Update the currency
        print(f"The converted amount is: {converted_amount} {to_currency}")
      
        break
    elif depOrWith =='4':
        person1.display()
    else: 
        print("Invalid input , Try again ")

