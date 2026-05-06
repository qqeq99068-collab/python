import tkinter as tk
from datetime import date
from tkinter import messagebox

root = tk.Tk()
root.title("Age Calculator")
root.geometry("250x200")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Age Calculator", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack()

tk.Label(frame, text="Day:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=3)
day = tk.Entry(frame, width=5)
day.grid(row=0, column=1)

tk.Label(frame, text="Month:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=3)
month = tk.Entry(frame, width=5)
month.grid(row=1, column=1)

tk.Label(frame, text="Year:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=3)
year = tk.Entry(frame, width=5)
year.grid(row=2, column=1)

result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
result.pack(pady=8)

def calculate():
    try:
        dob = date(int(year.get()), int(month.get()), int(day.get()))
    except:
        messagebox.showerror("Error", "Invalid date")
        return
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    result.config(text=f"You are {age} years old")

tk.Button(root, text="Calculate", command=calculate, bg="#4a90d9", fg="white", relief="flat", padx=10, pady=4).pack()

root.mainloop()