import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class SportsStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x1000")
        self.root.configure(bg="light blue")
        self.root.title("Спортен магазин Rodi")

        self.data = []
        self.data_dict = {}

        self.create_widgets()
    def create_widgets(self):
        self.header_label = tk.Label(self.root, text="Спортни стоки - Rodi", bg="light blue", fg="dark blue", font=("Arial", 24))
        self.header_label.pack(pady=10)

        self.open_button = tk.Button(self.root, text="Отвори файлове", command=self.open_files, fg="dark blue")
        self.open_button.pack()

        self.save_button = tk.Button(self.root, text="Запиши", command=self.save_to_file, fg="dark blue")
        self.save_button.pack()

        self.data_listbox = tk.Listbox(self.root, width=100, height=12, fg="dark blue")
        self.data_listbox.pack()

        self.search_label = tk.Label(self.root, text="Търсене по категория:", fg="dark blue")
        self.search_label.pack()

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        self.search_button = tk.Button(self.root, text="Търси", command=self.search_data, fg="dark blue")
        self.search_button.pack()

        self.search_listbox = tk.Listbox(self.root, width=100, height=12, fg="dark blue")
        self.search_listbox.pack()

        self.filter_label = tk.Label(self.root, text="Филтър по максимална цена:", fg="dark blue")
        self.filter_label.pack()

        self.filter_entry = tk.Entry(self.root)
        self.filter_entry.pack()

        self.filter_button = tk.Button(self.root, text="Филтрирай", command=self.filter_data_criteria, fg="dark blue")
        self.filter_button.pack()

        self.filter_listbox = tk.Listbox(self.root, width=100, height=12, fg="dark blue")
        self.filter_listbox.pack()

        self.add_category_entry = tk.Entry(self.root, fg="dark blue")
        self.add_category_entry.pack()
        self.add_category_entry.insert(0, "Категория")

        self.add_item_entry = tk.Entry(self.root, fg="dark blue")
        self.add_item_entry.pack()
        self.add_item_entry.insert(0, "Продукт")

        self.add_price_entry = tk.Entry(self.root, fg="dark blue")
        self.add_price_entry.pack()
        self.add_price_entry.insert(0, "Цена")

        self.add_button = tk.Button(self.root, text="Добави", command=self.add_data, fg="dark blue")
        self.add_button.pack()

    def open_files(self):
        filepaths = filedialog.askopenfilenames()
        if filepaths:
            self.data = self.read_files(filepaths)
            self.visualize_data(self.data, self.data_listbox)
            self.data_dict = self.populate_dict(self.data)

    def read_files(self, filepaths):
        data = []
        for filepath in filepaths:
            with open(filepath, 'r') as file:
                lines = file.readlines()
                data.extend([line.strip() for line in lines if line.strip()])
        return data

    def visualize_data(self, data, listbox):
        listbox.delete(0, tk.END)
        for item in data:
            listbox.insert(tk.END, item)

    def populate_dict(self, data):
        data_dict = {}
        for line in data:
            category, item, price = line.split(',')
            if category not in data_dict:
                data_dict[category] = []
            data_dict[category].append((item, float(price)))
        return data_dict

    def search_data(self):
        self.search_listbox.delete(0, tk.END)
        search_term = self.search_entry.get()
        for item in self.data:
            if search_term in item:
                self.search_listbox.insert(tk.END, item)

    def search_dict(self, data_dict, category):
        return data_dict.get(category, [])

    def filter_data_criteria(self):
        max_price = float(self.filter_entry.get())
        filtered_data = self.filter_data(self.data_dict, max_price)
        self.visualize_data([f"{item[0]}: {item[1]} - {item[2]:.2f}" for item in filtered_data], self.filter_listbox)

    def filter_data(self, data_dict, max_price):
        filtered_data = []
        for category, items in data_dict.items():
            for item, price in items:
                if price <= max_price:
                    filtered_data.append((category, item, price))
        return filtered_data

    def save_to_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            self.save_data_to_file([(category, item[0], item[1]) for category in self.data_dict for item in self.data_dict[category]], filepath)

    def save_data_to_file(self, data, filepath):
        with open(filepath, 'w') as file:
            for item in data:
                file.write(f"{item[0]}, {item[1]}, {item[2]:.2f}\n")

    def add_data(self):
        category = self.add_category_entry.get()
        item = self.add_item_entry.get()
        price = float(self.add_price_entry.get())
        self.add_data_to_dict(self.data_dict, category, item, price)
        self.visualize_data([f"{key}: {', '.join([f'{item[0]} - {item[1]:.2f}' for item in items])}" for key, items in self.data_dict.items()], self.data_listbox)

    def add_data_to_dict(self, data_dict, category, item, price):
        if category not in data_dict:
            data_dict[category] = []
        data_dict[category].append((item, float(price)))

if __name__ == "__main__":
    root = tk.Tk()
    app = SportsStoreApp(root)
    root.mainloop()