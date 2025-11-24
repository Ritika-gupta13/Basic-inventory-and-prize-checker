# Basic-inventory-and-prize-checker
Python CLI app for basic retail inventory tracking, stock management, and identify items which are getting low in stock.
# Project themes and concepts
This project is made on retail and e-commerce domain.
# Features
This python application does the following things
1)Product creation: Allows the user to create the product by assigning a unique id ITMxxx.

2)inventory: Shows all the inventory that is available.

3)stock management: Enables the user to alter the stock and prize.

4)low stock alert: Automatically tells the stocks which is below the threshold limit which is 10 as taken in this application.

5)storage: save the data entered in json file [inventory_data.json]
# Installation and setup
This project is written in python.
# Running the Application
1)Download: Download the inventory_manager.py file to a local folder.

2)Open Terminal: Navigate to that folder using your terminal or command prompt.

3)Execute: Run the file using the Python interpreter:

            python main.py
# Technical Details & Architecture
This project was built to demonstrate several core programming concepts:

# Core Concepts Demonstrated:
1)Object-Oriented Programming (OOP): Uses the Product class to model real-world data, including dedicated methods (__str__, to_dict) for printing and serialization.

2)Data Persistence (File I/O): Utilizes Python's standard json library for structured saving and loading of the inventory state.

3)Data Structures: The active inventory is managed as a list of Product objects, facilitating linear searches and manipulation.

4)Input Validation: Robust while loops and try-except blocks ensure the user enters valid, positive numbers for price and stock.

# Data Storage
Data File: inventory_data.json
Item Code Format: ITM### (e.g., ITM001, ITM002, etc.)
# Project Structure
The project is minimalist and fully contained within a few files:

# Inventory_manager/

 ├── main.py   # The Python application code.
 
 └── README.md # This guide.

# Author
Ritika Gupta

            




