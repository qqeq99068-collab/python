import tkinter as tk

def inch_to_cm():
    result = float(input_box.get("1.0", tk.END)) * 2.54
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

root = tk.Tk()
input_box = tk.Text(root, height=2)
input_box.pack()
tk.Button(root, text="Submit", command=inch_to_cm).pack()
output_box = tk.Text(root, height=2)
output_box.pack()
root.mainloop()