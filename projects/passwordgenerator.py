import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    result.config(text=password)
    length_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")
root.geometry("375x225")

title = tk.Label(root, text="Password Generator", font=("Arial", 14))
title.pack(pady=10)

tk.Label(root, text="Enter Password Length:").pack()

length_entry = tk.Entry(root, bg="lightyellow", fg="black")
length_entry.pack()

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()