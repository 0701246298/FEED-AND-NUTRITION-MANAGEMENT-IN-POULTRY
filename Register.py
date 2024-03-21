import tkinter as tk
from tkinter import ttk, messagebox, Entry
import bcrypt
import mysql.connector

import dashboard

# Database connection details
db_connection = mysql.connector.connect(
    database="nutrition",
    user="root",
    password="maureen123",
    host="localhost",
    port="3306")
cursor = db_connection.cursor()


def create_users_table():
    # Create the 'users' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    db_connection.commit()


def main_acc():
    create_users_table()  # Ensure 'users' table is created
    global main_screen
    main_screen = tk.Tk()
    main_screen.title("Main")
    ttk.Label(main_screen, text="Login or Register", background="#b1abf1", foreground="white", width="300",
              font=("Calibri", 13)).pack(padx=20, pady=10)
    ttk.Button(main_screen, text="LOGIN", width=15, command=login).pack(pady=5)
    ttk.Button(main_screen, text="REGISTER", width=15, command=register).pack(pady=5)
    # Update the main window size based on the content
    content_width = 400  # Increased minimum width to 400
    content_height = sum(
        widget.winfo_reqheight() for widget in main_screen.winfo_children()) + 50  # Increased padding to 50

    main_screen.geometry(f"{content_width}x{content_height}")

    main_screen.protocol("WM_DELETE_WINDOW", on_closing)
    main_screen.mainloop()


def register():
    global register_screen
    register_screen = tk.Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("320x350")

    global username_entry
    global password_entry

    username_entry = tk.StringVar()
    password_entry = tk.StringVar()

    ttk.Label(register_screen, text="Enter Details Below to Register!", background="#D8BFD8", foreground="black",
              width="300", font=("Calibri", 13)).pack(padx=20, pady=23)
    ttk.Label(register_screen, text="").pack()

    unLabel = ttk.Label(register_screen, text="Username", foreground="black", background="#D8BFD8")
    unLabel.pack(pady=5)

    username_entry = Entry(register_screen, textvariable=username_entry)
    username_entry.pack()

    passLabel = ttk.Label(register_screen, text="Password", foreground="black", background="#D8BFD8")
    passLabel.pack(pady=5)

    password_entry = Entry(register_screen, textvariable=password_entry, show='*')
    password_entry.pack()

    ttk.Label(register_screen, text="").pack()
    ttk.Button(register_screen, text="Register", width=10, command=register_user).pack()


def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    login_screen = tk.Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("320x350")
    ttk.Label(login_screen, text="Enter Details Below to Login!", background="#c0ecc0", foreground="black",
              width="300", font=("Calibri", 13)).pack(padx=20, pady=23)
    ttk.Label(login_screen, text="").pack()

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    ttk.Label(login_screen, text="Username", foreground="black", background="#c0ecc0").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack(pady=5)

    ttk.Label(login_screen, text="").pack()
    ttk.Label(login_screen, text="Password", foreground="black", background="#c0ecc0").pack(pady=5)

    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    ttk.Label(login_screen, text="").pack()
    ttk.Button(login_screen, text="Login", width=10, command=login_verify).pack()


def register_user():
    global username_entry, password_entry

    username_info = username_entry.get()
    password_info = password_entry.get()

    # Check if both username and password are not empty`
    if not username_info or not password_info:
        messagebox.showerror("Error", "Both username and password are required!")
        return

    # Hash the password before storing it (use your preferred hashing method)
    hashed_password = bcrypt.hashpw(password_info.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into the 'users' table
    cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (username_info, hashed_password))
    db_connection.commit()
    messagebox.showinfo("Registration Success", "Registration is successful!")
    register_screen.destroy()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    # Retrieve user from 'users' table
    cursor.execute("SELECT * FROM users WHERE name = %s", (username1,))
    user = cursor.fetchone()
    print(user)#debug print statement.

    if user and bcrypt.hashpw(password1.encode('utf-8'), user[2].encode('utf-8')):
        messagebox.showinfo("Login Success", "Login successfuly!!")
        login_screen.destroy()

    else:
        messagebox.showerror("login Error", "Invalid username or password")

def open_dashboard_page():
    main_screen.destroy()  # Close the main screen
    dashboard.main()  # Call the main function of landing.py to open the landing page




def on_closing():
    db_connection.close()
    main_screen.destroy()


def main():
    main_acc()


if __name__ == "__main__":
    main()
