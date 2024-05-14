import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
import tkinter.messagebox

landing_window = tk.Tk()

def finalize_order():   
    pass
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
    login_form = tk.Frame(login_window, padx=30, pady = 30)
    login_form.pack(padx=20,fill=tk.BOTH, expand=True)
    login_window.configure(background="dark blue")
    username_label = tk.Label(login_form, text="Username")
    username_label.grid(row=0, column=0, sticky=tk.W)
    username_entry = tk.Entry(login_form)
    username_entry.grid(row=0, column=1)
    password_label = tk.Label(login_form, text="Password")
    password_label.grid(row=1, column=0, sticky=tk.W)
    password_entry = tk.Entry(login_form, show="*")
    password_entry.grid(row=1, column=1)
    login_button = tk.Button(login_form, text="Login", command=lambda: login(username_entry, password_entry))
    login_button.grid(row=2, column=0, columnspan=2)
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
def men_page():
    main_window.withdraw()
    men_window = tk.Toplevel(main_window)
    men_window.geometry("900x600")
    men_window.title("Men's Products")
    menubar = tk.Menu(men_window)
    menubar.add_command(label="Return to Home Page", command=lambda: main_page(men_window))
    menubar.add_command(label="Exit", command=men_window.quit)
    men_window.config(menu=menubar)
    men_frame = tk.Frame(men_window, padx=30, pady = 30)
    men_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    men_window.configure(background="dark blue")
    label = tk.Label(men_frame, text="Men's Products", font=("Arial", 20))
    label.pack(pady=10)  
    tree = ttk.Treeview(men_frame)
    categories = {"-T": "Topwear", "-B": "Bottomwear", "-S": "Shoes", "-R": "Tracksuit"}
    parents = {category: tree.insert("", "end", text=name) for category, name in categories.items()}
    with open("mens.txt", "r") as file:
        for line in file:
            for category, parent in parents.items():
                if category in line:
                    tree.insert(parent, "end", text=line.strip())
                    break
    tree.pack(fill=tk.BOTH, expand=True) 
   
    button = tk.Button(men_frame, text="Add to cart", command=cart_page)
    button.pack() 
    men_frame.grid_rowconfigure(1, weight=1)
    men_frame.grid_columnconfigure(0, weight=1)
def women_page():
    main_window.withdraw()
    women_window = tk.Toplevel(main_window)
    women_window.geometry("600x400")
    women_window.title("Women's Products")
    menubar = tk.Menu(women_window)
    menubar.add_command(label="Return to Home Page", command=lambda: main_page(women_window))
    menubar.add_command(label="Exit", command=women_window.quit)
    women_window.config(menu=menubar)
    women_frame = tk.Frame(women_window, padx=30, pady = 30)
    women_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    women_window.configure(background="dark blue")
    label = tk.Label(women_frame, text="Women's Products", font=("Arial", 20))
    label.pack(pady=10)
    tree = ttk.Treeview(women_page)
    categories = {"-T": "Topwear", "-B": "Bottomwear", "-S": "Shoes", "-R": "Tracksuit"}
    parents = {category: tree.insert("", "end", text=name) for category, name in categories.items()}
    with open("mens.txt", "r") as file:
        for line in file:
            for category, parent in parents.items():
                if category in line:
                    tree.insert(parent, "end", text=line.strip())
                    break
    tree.pack()
def kids_page():
    main_window.withdraw()
    kids_window = tk.Toplevel(main_window)
    kids_window.geometry("600x400")
    kids_window.title("Kids's Products")
    menubar = tk.Menu(kids_window)
    menubar.add_command(label="Return to Home Page", command=lambda: main_page(kids_window))
    menubar.add_command(label="Exit", command=kids_window.quit)
    kids_window.config(menu=menubar)
    kids_frame = tk.Frame(kids_window, padx=30, pady = 30)
    kids_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    kids_window.configure(background="dark blue")
    label = tk.Label(kids_frame, text="Kids's Products", font=("Arial", 20))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.place(relx = 0.5, rely = 0.5, anchor = tk.TOP)
def nutritions_page():
    main_window.withdraw()
    nutritions_window = tk.Toplevel(main_window)
    nutritions_window.geometry("600x400")
    nutritions_window.title("Nutritions")
    menubar = tk.Menu(nutritions_window)
    menubar.add_command(label="Return to Home Page", command=lambda: main_page(nutritions_window))
    menubar.add_command(label="Exit", command=nutritions_window.quit)
    nutritions_window.config(menu=menubar)
    nutritions_frame = tk.Frame(nutritions_window, padx=30, pady = 30)
    nutritions_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    nutritions_window.configure(background="dark blue")
    label = tk.Label(nutritions_frame, text="Nutritions", font=("Arial", 20))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.place(relx = 0.5, rely = 0.5, anchor = tk.TOP)
def accessories_page():
    main_window.withdraw()
    accessories_window = tk.Toplevel(main_window)
    accessories_window.geometry("600x400")
    accessories_window.title("Accessories")
    menubar = tk.Menu(accessories_window)
    menubar.add_command(label="Return to Home Page", command=lambda: main_page(accessories_window))
    menubar.add_command(label="Exit", command=accessories_window.quit)
    accessories_window.config(menu=menubar)
    accessories_frame = tk.Frame(accessories_window, padx=30, pady = 30)
    accessories_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    accessories_window.configure(background="dark blue")
    label = tk.Label(accessories_frame, text="Accessories", font=("Arial", 20))
    label.grid(row=0, column=0, columnspan=2, pady=10)
    label.place(relx = 0.5, rely = 0.5, anchor = tk.TOP)
def cart_page():
    main_window.withdraw()
    cart_window = tk.Toplevel(main_window)
    cart_window.geometry("900x600")
    cart_window.title("Cart")
    menubar = tk.Menu(cart_window)
    menubar.add_command(label="Return to Home Page", command=lambda: main_page(cart_window))
    menubar.add_command(label="Exit", command=cart_window.quit)
    cart_window.config(menu=menubar)
    cart_frame = tk.Frame(cart_window, padx=30, pady = 30)
    cart_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    cart_window.configure(background="dark blue")
    label = tk.Label(cart_frame, text="Cart", font=("Arial", 20))
    label.pack(pady=10)
    # label.grid(row=0, column=0, columnspan=2, pady=10)
    # label.place(relx = 0.5, rely = 0.5, anchor = tk.TOP)
    tree = ttk.Treeview(cart_frame, columns=("Item", "Quantity", "Price"), show="headings")
    tree.heading("Item", text="Item")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.pack()
    
    button = tk.Button(cart_frame, text="Finalize Order", command=finalize_order)
    button.pack(pady=10)
def switch_user():
    main_window.destroy()
    login_form()
def main_page(window=None):
    if window is not None:
        window.destroy()
    global main_window
    main_window = tk.Toplevel(login_window)
    main_window.geometry("600x400")
    main_window.title("Rodi Shop")
    main_frame = tk.Frame(main_window, padx=30, pady = 30)
    main_frame.pack(padx=20,fill=tk.BOTH, expand=True)
    main_window.configure(background="dark blue")
    menubar = tk.Menu(main_window)
    menubar.add_command(label="Switch User", command=switch_user)
    menubar.add_command(label="Exit", command=main_window.quit)
    main_window.config(menu=menubar)
    label = tk.Label(main_frame, text="Hello, Its time for sport!", font=("Arial", 20), bg="dark blue", fg="white")
    label.pack(fill=tk.X, pady=10)
    men_button = tk.Button(main_frame, text="Men", command=men_page, bg="dark blue", fg="white", font=("Arial", 12), padx=10, pady=10)
    men_button.place(relx = 0.2, rely = 0.6, anchor = tk.CENTER)
    women_button = tk.Button(main_frame, text="Women", command=women_page, bg="dark blue", fg="white", font=("Arial", 12), padx=10, pady=10)
    women_button.place(relx = 0.5, rely = 0.6, anchor = tk.CENTER)
    kids_button = tk.Button(main_frame, text="Kids", command=kids_page, bg="dark blue", fg="white", font=("Arial", 12), padx=10, pady=10)
    kids_button.place(relx = 0.8, rely = 0.6, anchor = tk.CENTER)
    nutritions_button = tk.Button(main_frame, text="Nutritions", command=nutritions_page, bg="dark blue", fg="white", font=("Arial", 12), padx=10, pady=10)
    nutritions_button.place(relx = 0.2, rely = 0.8, anchor = tk.CENTER)
    accessories_button = tk.Button(main_frame, text="Accessories", command=accessories_page, bg="dark blue", fg="white", font=("Arial", 12), padx=10, pady=10)
    accessories_button.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)
    cart_button = tk.Button(main_frame, text="Cart", command=cart_page, bg="dark blue", fg="white", font=("Arial", 12), padx=10, pady=10)
    cart_button.place(relx = 0.8, rely = 0.8, anchor = tk.CENTER)
    main_window.mainloop()

landing_page()
landing_window.mainloop()
