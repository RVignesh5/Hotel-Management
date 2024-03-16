# Hotel Management
This is a simple hotel management system built using Python and MySQL. It allows users to perform various operations such as adding room details, managing room bookings, and displaying customer information.
 ![Hotel Management System Demo](https://cdn.dribbble.com/users/6498639/screenshots/15138706/media/0262f2a4841a14755bd96261e11b6334.gif)

## Features

- **Login System:** Users can log in using a username and password.
- **Room Management:** Add, update, delete, and display room details such as room type, room number, and room status.
- **Customer Management:** Display customer details including name, phone number, address, check-in and check-out dates, and number of days stayed.

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages: `mysql-connector`, `tkinter` (for GUI)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/RVignesh5/hotel-management.git
    ```

2. Install the required Python packages:

    ```bash
    pip install mysql-connector-python
    ```

3. Set up your MySQL database. Create a database named `hote` and import the `database.sql` file provided in the repository to create the necessary tables.

4. Update the MySQL connection details in the `connect()` function of `hotel_management.py` file:

    ```python
    def connect():
        try:
            con = sq.connect(host='localhost', user='your_username', password='your_password', database='hote')
            if con.is_connected() == False:
                print("not connected")
            else:
                print("\n")
            return con
        except sq.Error as err:
            print(err)
    ```

## Usage

1. Run the `hotel_management.py` script:

    ```bash
    python hotel_management.py
    ```

2. Follow the on-screen instructions to navigate through the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
