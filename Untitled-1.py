import tkinter as tk

root = tk.Tk()

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

label = tk.Label(root)
label.pack()
def check():
 label.config(text=int(e1.get()) * int(e2.get()))
tk.Button(root, text="Check", command=check).pack()

root.mainloop()