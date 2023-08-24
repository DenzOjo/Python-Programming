import random
import tkinter as tk


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '@']

    nr_letters = int(letter_entry.get())
    nr_numbers = int(number_entry.get())
    nr_symbols = int(symbol_entry.get())

    password_letters = random.choices(letters, k=nr_letters)
    password_numbers = random.choices(numbers, k=nr_numbers)
    password_symbols = random.choices(symbols, k=nr_symbols)

    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)

    password_str = ''.join(password)
    password_label = tk.Label(window, text= f"Password:{password_str}")
    password_label.grid(column = 8, row = 2)


# Create a Tkinter window
window = tk.Tk()
window.title("Password Generator")
window.minsize(width=220 ,height=150)
window.config(padx=20 ,pady=20)
# Create input labels and entries
letter_label = tk.Label(window, text="How many letters?")
letter_label.grid(column = 1, row = 0)
letter_entry = tk.Entry(window)
letter_entry.grid(column= 2, row= 0)

number_label = tk.Label(window, text="How many numbers?")
number_label.grid(column = 1, row = 2)
number_entry = tk.Entry(window)
number_entry.grid(column = 2, row = 2)

symbol_label = tk.Label(window, text="How many symbols?")
symbol_label.grid(column= 1, row=4)
symbol_entry = tk.Entry(window)
symbol_entry.grid(column = 2, row=4 )

# Create a button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)

generate_button.grid(column=8,row=0, padx =10  )


window.mainloop()