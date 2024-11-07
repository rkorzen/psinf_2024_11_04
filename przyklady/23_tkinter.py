import tkinter

def dodaj():
    a_value = a.get()
    b_value = b.get()
    wynik_label.config(text=int(a_value) + int(b_value))


root = tkinter.Tk()

a_label = tkinter.Label(root, text="a")
a_label.pack()

a = tkinter.Entry(root)
a.pack()

b_label = tkinter.Label(root, text="b")
b_label.pack()

b = tkinter.Entry(root)
b.pack()

button = tkinter.Button(root, text="dodaj", command=dodaj)
button.pack()

wynik_label = tkinter.Label(root, text="-")
wynik_label.pack()

root.mainloop()



print("print po")