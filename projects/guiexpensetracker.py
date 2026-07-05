import tkinter as tk

expenses = []

def add():
    expenses.append([type_entry.get(), float(amount_entry.get())])
    result.config(text="Expense Added")

    type_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def show():
    text.delete("1.0", tk.END)
    total = 0
    for expense in expenses:
        text.insert(tk.END, expense[0] + " - " + str(expense[1]) + "\n")
        total += expense[1]
    text.insert(tk.END, "\nTotal: " + str(total))

def total():
    total = 0
    for expense in expenses:
        total += expense[1]
    result.config(text="Total: " + str(total))

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("375x450")

tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold")).pack(pady=5)

tk.Label(root, text="Type of Expense", font=("Arial", 12)).pack()
type_entry = tk.Entry(root)
type_entry.pack()

tk.Label(root, text="Amount", font=("Arial", 12)).pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Show", command=show).pack()
tk.Button(root, text="Total", command=total).pack()
tk.Button(root, text="Exit", command=root.destroy).pack()

result = tk.Label(root)
result.pack()

text = tk.Text(root, height=8, width=25)
text.pack()

root.mainloop()