from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('calculator')
window.minsize(width=220 ,height=250)
window.config(padx=20 ,pady=20)



calc_entry = Entry(window,width = 30, justify='right')
calc_entry.grid(row=0,column=0,columnspan=4)

def return_():
    equation = calc_entry.get()
    try:
       answer = eval(equation)
    except:
        answer='error'
        messagebox.showinfo('message','error please recheck the equation')
    clear()
    insert(answer)

def insert (item):
    calc_entry.insert(END, item)

def clear():
    calc_entry.delete(0, END)

def del_():
    current_text=calc_entry.get()
    if current_text:
        new_text =current_text[:-1]
        calc_entry.delete(0,END)
        calc_entry.insert(0,new_text)



button1= Button(window,text='1', width=4, height=2, command= lambda: insert('1'))
button1.grid(row=2, column=0)

button2= Button(window,text='2', width=4, height=2, command= lambda: insert('2'))
button2.grid(row=2, column=1)

button3= Button(window,text='3', width=4, height=2, command= lambda: insert('3'))
button3.grid(row=2, column=2)

button4= Button(window,text='4', width=4, height=2, command= lambda: insert('4'))
button4.grid(row=3, column=0)

button5= Button(window,text='5', width=4, height=2, command= lambda: insert('5'))
button5.grid(row=3, column=1)

button6= Button(window,text='6', width=4, height=2, command= lambda: insert('6'))
button6.grid(row=3, column=2)

button7= Button(window,text='7', width=4, height=2, command= lambda: insert('7'))
button7.grid(row=4, column=0)

button8= Button(window,text='8', width=4, height=2, command= lambda: insert('8'))
button8.grid(row=4, column=1)

button9= Button(window,text='9', width=4, height=2, command= lambda: insert('9'))
button9.grid(row=4, column=2)

button0= Button(window,text='0', width=4, height=2, command= lambda: insert('0'))
button0.grid(row=5, column=1,)

buttonplus= Button(window,text='+', width=5, height=2, command= lambda: insert('+'))
buttonplus.grid(row=2, column=3)

buttonminus= Button(window,text='-', width=5, height=2, command= lambda: insert('-'))
buttonminus.grid(row=3, column=3)

buttonmultiply= Button(window,text='*', width=5, height=2, command= lambda: insert('*'))
buttonmultiply.grid(row=4, column=3)

buttondivision= Button(window,text='/', width=5, height=2, command= lambda: insert('/'))
buttondivision.grid(row=5, column=3)

buttonequals= Button(window,text='=', width=10, height=2, command= return_)
buttonequals.grid(row=6, column=0,columnspan=2)

buttonclear= Button(window,text='c', width=10, height=2, command= clear)
buttonclear.grid(row=6, column=2, columnspan=2)

buttondot= Button(window,text='.', width=4, height=2, command= lambda: insert('.'))
buttondot.grid(row=5, column=0)

buttonclear= Button(window,text='DEL', width=4, height=2, command= del_)
buttonclear.grid(row=5, column=2)

window.mainloop()