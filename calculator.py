from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set(" ")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("349x535")
root.maxsize(349,535)
root.minsize(349,535)
root.title("calculator")


scvalue = StringVar()
scvalue.set(" ")
f=Frame(root,bg="purple")
screen = Entry(f, textvar=scvalue, bg="yellow",font="Lucida 30 bold ")
screen.pack(fill=X, ipadx=8, padx=10, pady=20)
f.pack()

f = Frame(root, bg="purple")

b = Button(f, text="1",  font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="3", font="lucida 35 bold")
b.pack(side= LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=",bg="cyan", font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="purple")
b = Button(f, text="4", font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 35 bold")
b.pack(side= LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="6", font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", bg="cyan" ,font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="purple")
b = Button(f, text="7", font="lucida 35 bold")
b.pack(side= LEFT, padx=5, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="8",  font="lucida 35 bold")
b.pack(side= LEFT, padx=11.2, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="9", font="lucida 35 bold")
b.pack(side= LEFT, padx=11.5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", bg="cyan" ,font="lucida 35 bold")
b.pack(side= LEFT, padx=11.2, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="purple")
b = Button(f, text="*", bg="cyan", font="lucida 35 bold")
b.pack(side= LEFT, padx=11, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="0" , font="lucida 35 bold")
b.pack(side= LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="/",bg="cyan", font="lucida 35 bold")
b.pack(side= LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="-", bg="cyan" , font="lucida 35 bold")
b.pack(side= LEFT, padx=13, pady=13)
b.bind("<Button-1>", click)

f.pack()
'''f = Frame(root, bg="grey")


b = Button(f, text="8", font="lucida 35 bold")
b.pack(side= LEFT, padx=10, pady=13)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 35 bold")
b.pack(side= LEFT, padx=5, pady=13)
b.bind("<Button-1>", click)

f.pack()'''
root.mainloop()
