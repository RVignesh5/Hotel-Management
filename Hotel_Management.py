import mysql.connector as mysql
import random
import datetime
import tkinter as tk

# Function to establish connection with MySQL database
def establish_connection():
    try:
        connection = mysql.connect(host='localhost', user='root', password='8520', database='hote')
        if connection.is_connected() == False:
            print("not connected")
        else:
            print("\n")
        return connection
    except mysql.Error as error:
        print(error)

# Function to handle login using Tkinter GUI
def login():
    root = tk.Tk()
    root.geometry('800x400')
    username = tk.StringVar()
    password = tk.StringVar()

# Function to display login form and handle user authentication
def show_login_form():
    username_input = username.get()
    password_input = password.get()
    if username_input == "veee" and password_input == "12345":
        menu()
    else:
        print("please check username and password")

    root.title("WELCOME")
    label = tk.Label(root, text="LOGIN FORM", font=("arial", 16, "bold")).grid(row=0, column=1)
    label1 = tk.Label(root, text="uid").grid(row=1)
    label2 = tk.Label(root, text="password").grid(row=2)
    entry1 = tk.Entry(root, textvariable=username).grid(row=1, column=1)
    entry2 = tk.Entry(root, textvariable=password).grid(row=2, column=1)
    tk.Button(root, text="exit", command=root.quit).grid(row=3, column=2)
    tk.Button(root, text="show", command=show_login_form).grid(row=4, column=2)
    tk.mainloop()
    login()

# Function to display menu options
def menu():
    print("WELCOME TO HOTEL")
    print("1. Add Room Detail\n2. Display Details of the Room\n3. Update Room Details\n4. Delete Room Details\n5. Search Room Details\n6. Display Customer Details\n7. Search Customer Details")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        decision = 'y'
        while decision == 'y':
            add_room()
            decision = input("Do you want to continue? ")
    elif choice == 2:
        display_room_details()
    elif choice == 3:
        update_room()
    elif choice == 4:
        delete_room()
    elif choice == 5:
        search_room()
    elif choice == 6:
        display_customer_details()
    elif choice == 7:
        search_customer_details()

# Function to insert room details into the database
def add_room():
    try:
        connection = establish_connection()
        room_type = input("Enter room type: ")
        room_no = int(input("Enter room number: "))
        room_rent = int(input("Enter room rent: "))
        room_status_input = int(input("Enter room status (0 for booked, 1 for available): "))
        if room_status_input == 0:
            room_status = "Room already Booked"
        else:
            room_status = "Available"
        cursor = connection.cursor()
        cursor.execute("INSERT INTO room(roomtype, roomno, roomrent, room_status) VALUES('%s', %d, %d, '%s')" % (room_type, room_no, room_rent, room_status))
        connection.commit()
        print("Data inserted successfully\n")
        menu()
    except mysql.Error as error:
        print(error)

# Function to display room details from the database
def display_room_details():
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM room")
        for row in cursor.fetchall():
            print(f'Room Type: {row[0]}\nRoom Number: {row[1]}\nRoom Rent: {row[2]}\nRoom Status: {row[3]}')
        menu()
    except mysql.Error as error:
        print(error)

# Function to update room details in the database
def update_room():
    try:
        connection = establish_connection()
        room_type = input("Enter room type: ")
        room_no = int(input("Enter room number: "))
        room_rent = float(input("Enter room rent: "))
        room_status = input("Enter room status: ")
        if room_status == 0:
            print("Room available")
        else:
            print("Room booked")
        cursor = connection.cursor()
        cursor.execute("UPDATE room SET roomtype='%s', roomrent=%f, roomstatus='%s' WHERE roomno=%d" % (room_type, room_rent, room_status, room_no))
        connection.commit()
        print("Data updated successfully\n")
        menu()
    except mysql.Error as error:
        print(error)

# Function to delete room details from the database
def delete_room():
    try:
        connection = establish_connection()
        room_no = int(input("Enter room number: "))
        cursor = connection.cursor()
        cursor.execute("DELETE FROM room WHERE roomno=%d" % (room_no))
        connection.commit()
        print("Data deleted successfully\n")
        menu()
    except mysql.Error as error:
        print(error)

# Function to search for room details in the database
def search_room():
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        room_no = int(input("Enter room number: "))
        cursor.execute("SELECT * FROM booking WHERE roomno=%d" % (room_no))
        row = cursor.fetchone()
        if row is None:
            print("Record not found\n")
            menu()
    except mysql.Error as error:
        print(error)

# Function to display customer details from the database
def display_customer_details():
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM booking")
        for row in cursor.fetchall():
            print(f'CID: {row[0]}\nCustomer Name: {row[1]}\nPhone Number: {row[2]}\nAddress: {row[3]}\nRoom Number: {row[4]}\nCheck-in Date: {row[5]}\nCheck-out Date: {row[6]}\nNumber of Days: {row[7]}')
    except mysql.Error as error:
        print(error)

# Function to search for customer details in the database
def search_customer_details():
    try:
        connection = establish_connection()
        cursor = connection.cursor()
        customer_name = input("Enter customer name: ")
        cursor.execute("SELECT * FROM booking WHERE cname='%s'" % (customer_name))
        for row in cursor.fetchall():
            if row[8] == 0:
                print("Display customer details")
            else:
                print("Do not display customer details")
                print(f'CID: {row[0]}\nCustomer Name: {row[1]}\nPhone Number: {row[2]}\nAddress: {row[3]}\nRoom Number: {row[4]}\nCheck-in Date: {row[5]}\nCheck-out Date: {row[6]}\nNumber of Days: {row[7]}')
    except mysql.Error as error:
        print(error)
