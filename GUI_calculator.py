from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get() + text)
        screen.update()
        
root = Tk()

root.geometry("500x500")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font="lucida 40 bold")
screen.pack(fill = X, ipadx = 8, pady = 10, padx = 10)

f = Frame(root, bg = "grey")

b = Button(f, text = "C", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "**2", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "%", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "/", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text = "7", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "8", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "9", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "*", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text = "4", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "5", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "6", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "-", padx = 10 ,pady = 10, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text = "1", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "2", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "3", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "+", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text = "%", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "0", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = ".", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

b = Button(f, text = "=", padx = 9 ,pady = 9, font = "lucida 20 bold")
b.pack(side=LEFT ,padx = 2, pady = 2)
b.bind("<Button-1>", click)

f.pack()



root.mainloop()
