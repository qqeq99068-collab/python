from tkinter import *

root = Tk()
root.title("Password Checker")
root.geometry("400x400")
root.config(bg="lightblue")

textbox = Entry(root)
textbox.pack()

label = Label(root, text="Password Strength Checker", bg="skyblue", font=("Arial", 16))
label.pack()
def pstrength():
    password = textbox.get()
    score = 0

    for char in password:
        if char.isdigit():
            score += 2
        elif char.isalpha():
            score += 1
        else:
            score += 3
    if score <= 3:
        label.config(text="Extremely weak password", fg="red")
    elif score <= 6:
        label.config(text="Weak password", fg="orange")
    elif score <= 9:
        label.config(text="Medium password", fg="yellow")
    else:
        label.config(text="Strong password", fg="green")

    print("Score:", score)
        
button = Button(root, text="Click Me", command=pstrength)
button.pack()

root.mainloop()