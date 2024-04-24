import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "secret":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def register():
    username = username_entry.get()
    password = password_entry.get()

    if username not in user_data:  
        user_data[username] = password
        messagebox.showinfo("Registration Successful", "Account created successfully.")
    else:
        messagebox.showerror("Registration Failed", "Username already exists.")


root = tk.Tk()
root.title("Login/Register")

login_register_frame = tk.LabelFrame(root, text="Login or Register")
login_register_frame.pack(padx=10, pady=10)

username_label = tk.Label(login_register_frame, text="Username:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(login_register_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_register_frame, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(login_register_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_register_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

register_frame = tk.Frame(root)  
register_frame.pack(padx=10, pady=10)  

register_label = tk.Label(register_frame, text="Username:")
register_label.grid(row=0, column=0)

register_username_entry = tk.Entry(register_frame)
register_username_entry.grid(row=0, column=1)

register_password_label = tk.Label(register_frame, text="Password:")
register_password_label.grid(row=1, column=0)

register_password_entry = tk.Entry(register_frame, show="*")
register_password_entry.grid(row=1, column=1)

register_button = tk.Button(register_frame, text="Register", command=register)
register_button.grid(row=2, columnspan=2)


root.mainloop()
