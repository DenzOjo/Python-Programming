import json
import tkinter as tk
from tkinter import messagebox


class Bank:
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"A sum of {amount} was deposited")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.balance_check()
            self.transaction_history.append(f"A sum of {amount} was withdrawn")
        else:
            messagebox.showerror("Insufficient Funds", "You have insufficient funds in your account!")

    def balance_check(self):
        print(f"Available balance for account {self.account_name}: {self.balance}")

    def display_transaction(self):
        for transaction in self.transaction_history:
            print(transaction)


class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bank Account Manager")

        self.bank = None

        self.create_widgets()

        self.load_data()

    def create_widgets(self):
        self.label_name = tk.Label(self, text="Account Name")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_number = tk.Label(self, text="Account Number")
        self.label_number.grid(row=1, column=0, padx=10, pady=5)
        self.entry_number = tk.Entry(self)
        self.entry_number.grid(row=1, column=1, padx=10, pady=5)

        self.label_balance = tk.Label(self, text="Account Balance")
        self.label_balance.grid(row=2, column=0, padx=10, pady=5)
        self.entry_balance = tk.Entry(self)
        self.entry_balance.grid(row=2, column=1, padx=10, pady=5)

        self.button_create = tk.Button(self, text="Create Account", command=self.create_account)
        self.button_create.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.label_amount = tk.Label(self, text="Transaction Amount")
        self.label_amount.grid(row=4, column=0, padx=10, pady=5)
        self.entry_amount = tk.Entry(self)
        self.entry_amount.grid(row=4, column=1, padx=10, pady=5)

        self.button_deposit = tk.Button(self, text="Deposit", command=self.deposit)
        self.button_deposit.grid(row=5, column=0, padx=10, pady=5)
        self.button_withdrawal = tk.Button(self, text="Withdraw", command=self.withdrawal)
        self.button_withdrawal.grid(row=5, column=1, padx=10, pady=5)

        self.button_balance = tk.Button(self, text="View Balance", command=self.view_balance)
        self.button_balance.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.button_save = tk.Button(self, text="Save Data", command=self.save_data)
        self.button_save.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.text_transactions = tk.Text(self, height=10, width=30)
        self.text_transactions.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    def create_account(self):
        account_name = self.entry_name.get()
        account_number = self.entry_number.get()
        balance = float(self.entry_balance.get())

        self.bank = Bank(account_name, account_number, balance)

        self.entry_name.delete(0, tk.END)
        self.entry_number.delete(0, tk.END)
        self.entry_balance.delete(0, tk.END)

        self.text_transactions.insert(tk.END, "Account created\n")

    def deposit(self):
        if self.bank is not None:
            amount = float(self.entry_amount.get())
            self.bank.deposit(amount)

            self.entry_amount.delete(0, tk.END)
            self.text_transactions.insert(tk.END, f"Deposited {amount}\n")

    def withdrawal(self):
        if self.bank is not None:
            amount = float(self.entry_amount.get())
            if amount > self.bank.balance:
                messagebox.showerror("Insufficient Funds", "You have insufficient funds in your account!")
            else:
                self.bank.withdrawal(amount)

                self.entry_amount.delete(0, tk.END)
                self.text_transactions.insert(tk.END, f"Withdrawn {amount}\n")
    def view_balance(self):
        if self.bank is not None:
            self.text_transactions.insert(tk.END, f"Account balance: {self.bank.balance}\n")

        if self.bank.transaction_history:
            self.text_transactions.insert(tk.END, "Transaction history:\n")
            for transaction in self.bank.transaction_history:
                self.text_transactions.insert(tk.END, f"- {transaction}\n")

    def save_data(self):
        account_details = {
            "account_name": self.bank.account_name,
            "account_number": self.bank.account_number,
            "balance": self.bank.balance,
            "transaction_history": self.bank.transaction_history
        }

        with open("data.json", "w") as file:
            json.dump(account_details, file)

        self.text_transactions.insert(tk.END, "Data saved\n")

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                account_details = json.load(file)

            account_name = account_details["account_name"]
            account_number = account_details["account_number"]
            balance = account_details["balance"]
            transaction_history = account_details["transaction_history"]

            self.bank = Bank(account_name, account_number, balance)
            self.bank.transaction_history = transaction_history

            self.text_transactions.insert(tk.END, "Data loaded from file\n")

        except FileNotFoundError:
            self.text_transactions.insert(tk.END, "No previous data found\n")

bank_app = BankApp()
bank_app.mainloop()