Airport Management Software
This is a Python GUI project using Tkinter and SQLite, designed for managing an airport's operations. The software provides functionalities for managing tickets and users, as well as generating reports. Here's a guide on how to use and understand this project.

Table of Contents
Prerequisites
Getting Started
Project Structure
Usage
Login
Main Menu
Tickets Tab
Users Tab
Reports Tab
Contributing
License
Prerequisites
Before running this project, make sure you have the following dependencies installed:

Python (>= 3.x)
Tkinter (usually included with Python)
SQLite (usually included with Python)
Getting Started
Clone this repository or download the project files.

Ensure you have the prerequisites installed.

Run the main.py file to start the application.

Project Structure
main.py: The main script to run the application.
baza.py: Contains the database operations using SQLite.
README.md: The project's documentation.
Other Python files: Modules containing various functions and classes used in the application.
Usage
Login
When you run the application, it will open a login screen.
Enter your username and password to log in.
If the credentials are correct, you will be directed to the main menu.
Main Menu
The main menu consists of several tabs for different functionalities.

Tickets Tab
In the "Karte" tab, you can perform various ticket-related operations.
Click "Prikazi Sve" to display all tickets.
Use the search fields to filter tickets based on criteria like ID Leta, Ime, Prezime, Prodavac, or Cena.
Click "Dodaj" to add a new ticket.
Select a ticket from the list to edit or delete it.
Click "Izmeni" to update a ticket's information.
Click "Izbrisi" to delete a ticket.
Users Tab
In the "Radnici" tab, you can manage airport staff (users).
Click "Prikazi Sve" to display all users.
Use the search fields to filter users based on criteria like Username, Password, or Radnomesto.
Click "Dodaj" to add a new user.
Select a user from the list to edit or delete them.
Click "Izmeni" to update a user's information.
Click "Izbrisi" to delete a user.
Reports Tab
In the "Izvestaji" tab, you can generate reports.
See the total value of sold tickets.
Select a staff member (Radnik) from the dropdown menu and click "Potvrdi" to generate a report for that user.
Contributing
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome and appreciated.

License
This project is licensed under the MIT License. See the LICENSE file for details.