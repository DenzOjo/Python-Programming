'''
Create a Bank class( a blueprint for  a bank account). This Bank class 4 properties/attributes: account_name, account_number, balance, and transaction_history.

* The account_name attribute, account_number attribute and balance attribute  will be recieved as arguments from the user.    While transaction_history attribute will be an empty list amongst the attributes of the Bank class

* Create methods for deposit, withdrawal and balance check.
deposit method: This will add to the initial balance of the account
withdrawal method: This will remove from the balance of the account

balance check method: This will display the available balance in the account

for each deposit and withdrawal action taken. a receipt is appended to the transaction_history property created.    for example if there is a deposit of 100 dollars. you do: transaction_history.append(f'A sum of {amount} was deposited')

* Then finally you create a display_transaction method that prints out all the transactions that has been stored in the transaction_history list (which is an attribute of the Bank class)
'''
class Bank:
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.balance_check()
        self.transaction_history.append(f'A sum of {amount} was deposited')

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.balance_check()
            self.transaction_history.append(f'A sum of {amount} was withdrawn')
        else:
            print("Insufficient balance!")

    def balance_check(self):
        print(f"Available balance: {self.balance}")

    def display_transaction(self):
        for transaction in self.transaction_history:
            print(transaction)


account = Bank('cranky jones','567865',500)

account.withdrawal(200)
account.deposit(1000)
account.display_transaction()

