import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import mysql.connector


class Bird(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="maureen123",
            database="nutrition"
        )
        self.db_cursor = self.db_connection.cursor()

        self.bird_id_label = tk.Label(self, text="Bird ID:")
        self.bird_id_entry = tk.Entry(self)

        self.age_label = tk.Label(self, text="Age:")
        self.age_entry = tk.Entry(self)

        self.purchase_date_label = tk.Label(self, text="Purchase Date:")
        self.purchase_date_cal = Calendar(self)

        self.mortality_label = tk.Label(self, text="Mortality:")
        self.mortality_combo = ttk.Combobox(self, values=["Yes", "No"])
        self.mortality_combo.current(0)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        self.view_button = tk.Button(self, text="View Entries", command=self.view_entries)

        # Place widgets using grid layout
        self.bird_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.bird_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.purchase_date_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.purchase_date_cal.grid(row=2, column=1, padx=10, pady=5)

        self.mortality_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.mortality_combo.grid(row=3, column=1, padx=10, pady=5)

        self.submit_button.grid(row=4, columnspan=2, pady=10)
        self.view_button.grid(row=5, columnspan=2, pady=10)

    def submit_form(self):
        bird_id = self.bird_id_entry.get()
        age = self.age_entry.get()
        purchase_date = self.purchase_date_cal.get_date()
        mortality = self.mortality_combo.get()

        # Insert the data into the MySQL database
        query = "INSERT INTO bird (bird_Id, Age, purchased_date, mortality) VALUES (%s, %s, %s, %s)"
        values = (bird_id, age, purchase_date, mortality)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        # Process the form data (e.g., save to database, display, etc.)
        messagebox.showinfo("Form Submitted",
                            f"Bird ID: {bird_id}\nAge: {age}\nPurchase Date: {purchase_date}\nMortality: {mortality}")

    def view_entries(self):
        # Fetch all entries from the database
        query = "SELECT * FROM bird"
        self.db_cursor.execute(query)
        entries = self.db_cursor.fetchall()
        # Create a new window to display entries
        view_window = tk.Toplevel(self)
        view_window.title("View Entries")

        # Display headers
        headers = ("Bird_ID", "Age", "Purchased_date", "Mortality")
        for j, header in enumerate(headers):
            label = tk.Label(view_window, text=header)
            label.grid(row=0, column=j, padx=5, pady=3, sticky="w")

        # Display entries below headers
        for i, entry in enumerate(entries):
            for j, value in enumerate(entry):
                label = tk.Label(view_window, text=value)
                label.grid(row=i + 1, column=j, padx=5, pady=3, sticky="w")


class Eggs(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="maureen123",
            database="nutrition"
        )
        self.db_cursor = self.db_connection.cursor()

        self.egg_id_label = tk.Label(self, text="Egg_ID:")
        self.egg_id_entry = tk.Entry(self)

        self.sales_label = tk.Label(self, text="Sales:")
        self.sales_entry = tk.Entry(self)

        self.production_label = tk.Label(self, text="Production:")
        self.production_cal = Calendar(self)

        self.bird_id_label = tk.Label(self, text="Bird_ID:")
        self.bird_id_entry = tk.Entry(self)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        self.view_button = tk.Button(self, text="View Entries", command=self.view_entries)

        # Place widgets using grid layout
        self.bird_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.bird_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.sales_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.sales_entry.grid(row=1, column=1, padx=10, pady=5)

        self.production_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.production_cal.grid(row=2, column=1, padx=10, pady=5)

        self.egg_id_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.egg_id_entry.grid(row=3, column=1, padx=10, pady=5)

        self.submit_button.grid(row=4, columnspan=2, pady=10)
        self.view_button.grid(row=5, columnspan=2, pady=10)

    def submit_form(self):
        egg_id = self.egg_id_entry.get()
        sales = self.sales_entry.get()
        production = self.production_cal.get_date()
        bird_id = self.bird_id_entry.get()

        # Insert the data into the MySQL database
        query = "INSERT INTO  eggs (bird_Id,sales, production, egg_id) VALUES (%s, %s, %s, %s)"
        values = (bird_id, sales, production, egg_id)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        # Process the form data (e.g., save to database, display, etc.)
        messagebox.showinfo("Form Submitted",
                            f"Bird ID: {bird_id}\nEgg_id: {egg_id}\nProduction: {production}\nsales: {sales}")

    def view_entries(self):
        # Fetch all entries from the database
        query = "SELECT * FROM eggs"
        self.db_cursor.execute(query)
        entries = self.db_cursor.fetchall()

        # Create a new window to display entries
        view_window = tk.Toplevel(self)
        view_window.title("View Entries")

        # Display headers
        headers = ("Bird_ID", "Sales", "Production", "egg_id")
        for j, header in enumerate(headers):
            label = tk.Label(view_window, text=header)
            label.grid(row=0, column=j, padx=5, pady=3, sticky="w")

        # Display entries below headers
        for i, entry in enumerate(entries):
            for j, value in enumerate(entry):
                label = tk.Label(view_window, text=value)
                label.grid(row=i + 1, column=j, padx=5, pady=3, sticky="w")


class Feed(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="maureen123",
            database="nutrition"
        )
        self.db_cursor = self.db_connection.cursor()

        self.type_feed_label = tk.Label(self, text="Type_Feed:")
        self.type_feed_entry = tk.Entry(self)

        self.Age_label = tk.Label(self, text="Age:")
        self.Age_entry = tk.Entry(self)

        self.purchased_label = tk.Label(self, text="Purchased:")
        self.purchased_cal = Calendar(self)

        self.bird_id_label = tk.Label(self, text="Bird_ID:")
        self.bird_id_entry = tk.Entry(self)

        self.consumed_label = tk.Label(self, text="Consumption:")
        self.consumed_entry = tk.Entry(self)


        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        self.view_button = tk.Button(self, text="View Entries", command=self.view_entries)

        # Place widgets using grid layout
        self.bird_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.bird_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.type_feed_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.type_feed_entry.grid(row=1, column=1, padx=10, pady=5)

        self.purchased_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.purchased_cal.grid(row=2, column=1, padx=10, pady=5)

        self.consumed_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.consumed_entry.grid(row=3, column=1, padx=10, pady=5)

        self.submit_button.grid(row=4, columnspan=2, pady=10)
        self.view_button.grid(row=5, columnspan=2, pady=10)

    def submit_form(self):
        type_feed = self.type_feed_entry.get()
        Age = self.Age_entry.get()
        purchased = self.purchased_cal.get_date()
        consumed=self.consumed_entry.get()
        bird_id = self.bird_id_entry.get()

        # Insert the data into the MySQL database
        query = "INSERT INTO  feed (bird_Id,type_feed, purchased, Age,consumed) VALUES (%s, %s, %s, %s)"
        values = (bird_id,type_feed, purchased, Age,consumed)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        # Process the form data (e.g., save to database, display, etc.)
        messagebox.showinfo("Form Submitted",
                            f"Bird ID: {bird_id}\nAge: {Age}\nPurchased: {purchased}\nConsumption: {consumed}\nType_Feed: {type_feed}")

    def view_entries(self):
        # Fetch all entries from the database
        query = "SELECT * FROM feed"
        self.db_cursor.execute(query)
        entries = self.db_cursor.fetchall()

        # Create a new window to display entries
        view_window = tk.Toplevel(self)
        view_window.title("View Entries")

        # Display headers
        headers = ("Type Feed", "Age", "Bird_ID", "Purchased", "Consumption")
        for j, header in enumerate(headers):
            label = tk.Label(view_window, text=header)
            label.grid(row=0, column=j, padx=5, pady=3, sticky="w")

        # Display entries below headers
        for i, entry in enumerate(entries):
            for j, value in enumerate(entry):
                label = tk.Label(view_window, text=value)
                label.grid(row=i + 1, column=j, padx=5, pady=3, sticky="w")


# Your existing code...
root = tk.Tk()
root.geometry('500x600')
root.title('Dashboard')


def bird_page():
    hide_frames()
    bird_form.pack(pady=20)


def eggs_page():
    hide_frames()
    eggs_form.pack(pady=20)


def feed_page():
    hide_frames()
    feed_form.pack(pady=20)


def hide_frames():
    for frame in [bird_form, eggs_form, feed_form]:
        frame.pack_forget()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    page()


def hide_indicators():
    bird_indicate.config(bg='#c3c3c3')
    eggs_indicate.config(bg='#c3c3c3')
    feed_indicate.config(bg='#c3c3c3')


options_frame = tk.Frame(root, bg='#c3c3c3')
bird_btn = tk.Button(options_frame, text='bird', font=('Bold', 16), fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(bird_indicate, bird_page))
bird_btn.place(x=10, y=50)
bird_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
bird_indicate.place(x=3, y=50, width=5, height=40)
bird_indicate.bind("<Button-1>", lambda event: indicate(bird_indicate, bird_page))

eggs_btn = tk.Button(options_frame, text='eggs', font=('Bold', 16), fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(eggs_indicate, eggs_page))
eggs_btn.place(x=10, y=100)
eggs_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
eggs_indicate.place(x=3, y=100, width=5, height=40)
eggs_indicate.bind("<Button-1>", lambda event: indicate(eggs_indicate, eggs_page))

feed_btn = tk.Button(options_frame, text='feed', font=('Bold', 16), fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(feed_indicate, feed_page))
feed_btn.place(x=10, y=150)
feed_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
feed_indicate.place(x=3, y=150, width=5, height=40)
feed_indicate.bind("<Button-1>", lambda event: indicate(feed_indicate, feed_page))

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=700)

main_frame = tk.Frame(root)
bird_form = Bird(main_frame)
eggs_form = Eggs(main_frame)
feed_form=Feed(main_frame)



main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1000, width=1000)

root.mainloop()
