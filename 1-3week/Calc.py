from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")

# логика калькулятор
def calc(key):
    global memory
    if key == "=":
        # исключаем написание букв
        str1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol isnt't integer!")
            messagebox.showerror("Error!", "You input isn't integer")

# счет
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "="+str(result))
        except:
            calc_entry.insert(END, "Error")
            messagebox.showerror("Error!", "Please ckeck entered data")

    elif key == "-/+":
        calc_entry.delete(0, END)

# создаем все кнопки

bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "", ""
]

r=1
c=0

for i in bttn_list:
    rel = ""
    cmd=lambda x=i:  calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1



calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)





root.mainloop()
