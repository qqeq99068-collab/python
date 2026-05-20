from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("stack-money-cartoon-white-56217774.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey! Welcome to the denomination counter",
               bg="light blue",
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.askquestion("Alert.", "do you want to calculate the denomination?")
    if MsgBox == "yes":
        topwin()

button1 = Button(root, text="Click here to start", command=msg, bg="brown", fg="white")
button1.place(x=260, y=370)

def topwin():
    top = Toplevel()
    top.title("denomination Counter")
    top.configure(bg="light grey")
    top.geometry("400x300")
    label2 = Label(top, text="Enter the amount", bg="light blue")
    label2.place(x=150, y=50)
    entry1 = Entry(top)
    lbl1 = Label(top, text="here are the number of notes for denomination", bg="light blue")
    l1 = Label(top, text="2000", bg="light blue")
    l2 = Label(top, text="500", bg="light blue")
    l3 = Label(top, text="100", bg="light blue")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            amount = int(entry1.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(0, str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number amount.")
    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")
    label2.place(x=230, y=50)
    entry1.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl1.place(x=140, y=170)
    l1.place(x=180, y=200)
    t1.place(x=270, y=200)
    l2.place(x=180, y=230)
    t2.place(x=270, y=230)
    l3.place(x=180, y=260)
    t3.place(x=270, y=260)

root.mainloop()