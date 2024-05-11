import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage


landing_window = tk.Tk()

def landing_page():
    landing_window.geometry("300x200")
    landing_window.title("Rodi shop")

    landing_frame = tk.Frame(landing_window, padx=30, pady = 30)
    landing_frame.pack(padx=20,fill=tk.BOTH, expand=True)

    landing_window.configure(background="dark blue")

    label = tk.Label(landing_frame, text="Welcome to Rodi Shop!")
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="NSEW")
    
    register_button = tk.Button(landing_frame, text="Register", bg="dark blue", fg="white", command=lambda: register_form())
    register_button.grid(row=1, column=0)
 
    login_button = tk.Button(landing_frame, text="Login", bg="dark blue", fg="white", command=login_form)
    login_button.grid(row=1, column=1)
   
    
def register(username_entry, email_entry, password_entry):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if username and email and password:
        with open('users_info.txt', 'a', encoding="utf-8") as file:
            file.write(f'{username},{email},{password}\n')
        messagebox.showinfo("Success", "Registration Successful")
        login_form()
        register_window.withdraw()
    else:
        messagebox.showerror("Error", "All fields are required")


def register_form():
    global register_window
    register_window = tk.Toplevel(landing_window)
    register_window.geometry("300x200")
    register_window.title("Registration Form")

    register_frame = tk.Frame(register_window, padx=30, pady = 30)
    register_frame.pack(padx=20,fill=tk.BOTH, expand=True)

    register_window.configure(background="dark blue")

    username_label = tk.Label(register_frame, text="Username")
    username_label.grid(row=0, column=0, sticky=tk.W)
    username_entry = tk.Entry(register_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    email_label = tk.Label(register_frame, text="Email")
    email_label.grid(row=1, column=0, sticky=tk.W)
    email_entry = tk.Entry(register_frame)
    email_entry.grid(row=1, column=1, padx=10, pady=5)

    password_label = tk.Label(register_frame, text="Password")
    password_label.grid(row=2, column=0, sticky=tk.W)
    password_entry = tk.Entry(register_frame, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    register_button = tk.Button(register_frame, text="Register", bg="dark blue", fg="white", command=lambda: register(username_entry, email_entry, password_entry))
    register_button.grid(row=4, column=0, columnspan=2, pady=10)


def login_form():
    global login_window
    login_window = tk.Toplevel(landing_window)
    login_window.geometry("300x200")
    login_window.title("Login Form")

    login_frame = tk.Frame(login_window, padx=30, pady = 30)
    login_frame.pack(padx=20,fill=tk.BOTH, expand=True)

    login_window.configure(background="dark blue")

    login_username_label = tk.Label(login_frame, text="Username")
    login_username_label.pack()
    login_username_entry = tk.Entry(login_frame)
    login_username_entry.pack()

    login_password_label = tk.Label(login_frame, text="Password")
    login_password_label.pack()
    login_password_entry = tk.Entry(login_frame, show="*")
    login_password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", command= lambda:login(login_username_entry, login_password_entry))
    login_button.pack()

def login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        with open('users_info.txt', 'r') as file:
            users = {}
            for line in file:
                if ',' not in line:
                    continue
                user, email, pwd = line.strip().split(',', 2)
                users[user] = pwd

            if username in users and users[username] == password:
                messagebox.showinfo("Success", "Login Successful")
                login_window.withdraw()
                landing_window.withdraw()
                main_page()
            else:
                messagebox.showerror("Error", "Invalid username or password")
    else:
        messagebox.showerror("Error", "Username and password are required")


def main_page():
    global main_window
    main_window = tk.Toplevel(login_window)
    main_window.geometry("600x400")
    main_window.title("Rodi Shop")

    main_frame = tk.Frame(main_window, padx=30, pady = 30)
    main_frame.pack(padx=20,fill=tk.BOTH, expand=True)

    main_window.configure(background="dark blue")

    label = tk.Label(main_frame, text="Hello, Its time for sport!", font=("Arial", 20))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.place(relx = 0.5, rely = 0.5, anchor = TOP)
    label = tk.Label(main_frame, text="Hello, Its time for sport!", font=("Arial", 20))

landing_page()
landing_window.mainloop()
