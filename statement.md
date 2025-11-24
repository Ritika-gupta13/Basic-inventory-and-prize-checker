# Project Statement: Basic Inventory & Price Checker

# Problem Statement

Small retail businesses, particularly those operating in e-commerce or small physical stores, require a simple and reliable tool to manage their product stock and pricing. The lack of an efficient system can lead to time-consuming manual checks, potential stockouts (missed sales), or over-ordering. The core problem is the need for a management tool that digitally tracks stock levels and automatically flags products needing reorder.

# Scope of the Project

The Basic Inventory & Price Checker will be a Command-Line Interface (CLI) application built entirely in Python.

The scope is strictly limited to:

Core CRUD Operations: Creation, Reading (Viewing), and Updating of product records.

Local Data Persistence: All inventory data is saved to and loaded from a local JSON file (inventory_data.json).

Single-User Focus: The application is designed for use by a single manager on a local machine; network functionality or multi-user access is outside this scope.

Business Logic: Implementation of a single business rule: the "Low Stock Alert" feature.

# Target Users

The primary users of this application are:

Small Business Owners/Managers: Individuals responsible for purchasing and operations in small retail or boutique e-commerce ventures.

Inventory Clerks: Staff tasked with daily stock audits and logging incoming/outgoing products.

Students/Learners: Users seeking a practical example of Object-Oriented Programming (OOP) and persistent data handling in a real-world context.

# High-Level Features

The application will provide the following essential features:

Add Product: Allows the user to input a product name, initial stock, and price, with an automatic, unique ItemCode generation (e.g., ITM001).

View All Inventory: Displays a formatted, comprehensive list of all products, their codes, prices, and stock levels.

Update Stock/Price: Enables the manager to modify the price and/or stock level of an existing product using its unique ItemCode.

Low Stock Alert: Filters the inventory to display only those products whose stock level is below the predefined LOW_STOCK_THRESHOLD (set to 10 units).

Save & Load: Ensures automatic saving of the entire inventory list to the inventory_data.json file upon exit and loads it upon startup.
