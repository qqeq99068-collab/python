import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("restaurant management App")
        self.menu_items = {
            "French Fries": 2,
            "lunch meal": 2,
            "Burger": 3,
            "Pizza": 4,
            "drink": 1,
            "cheese Burger": 2.5,
        }
        self.exchange_rate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame, text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)
        self.menu_labels = {}
        self.menu_quantity = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame, text=f"{item} (${price}):", font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantity[item] = quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="currency",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items)+1,
            column=0,
            padx=10,
            pady=5
        )
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=["USD", "PKR"]
        )
        currency_dropdown.grid(
            row=len(self.menu_items)+1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_prices)
        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2, columnspan=3, padx=10, pady=10)

    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()
        original_image = tk.PhotoImage(file="Bg.png")
        background_image = original_image.subsample(max(1, original_image.width() // bg_width), max(1, original_image.height() // bg_height))
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image

    def update_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "Rs."
        rate = self.exchange_rate if currency == "PKR" else 1
        for item, price in self.menu_items.items():
            converted_price = price * rate
            self.menu_labels[item].config(text=f"{item} ({symbol}{converted_price}):")
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "Rs."
        rate = self.exchange_rate if currency == "PKR" else 1
        for item, entry in self.menu_quantity.items():
            quantity= entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    item_cost = self.menu_items[item] * quantity * rate
                    total_cost += item_cost
                    order_summary += f"{item} x {quantity} = {symbol}{item_cost}\n"
                    if total_cost > 0:
                        order_summary += f"Total Cost: {symbol}{total_cost}"
                        messagebox.showinfo("Order Placed", order_summary)
                    else:
                        messagebox.showwarning("No Items", "Please enter quantity for at least one item.")
if __name__ == "__main__":
    root = tk.Tk()
    app= RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()