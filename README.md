# Inventory & Warehouse Management CLI

## Project Description

Inventory & Warehouse Management CLI is a Python-based command-line application designed to help administrators manage suppliers, warehouses, products, and inventory stock levels. The system uses Object-Oriented Programming (OOP), JSON file persistence, modular design, and automated testing to provide a simple but effective inventory management solution.

The application features an interactive menu-driven interface that allows users to perform inventory operations without memorizing command-line arguments.

## Features

    1.Supplier Management
        Add suppliers
        View supplier list

    2.Warehouse Management
        Add warehouses
        Manage warehouse information

    3.Product Management
        Add products
        View products
        Search products

    4.Inventory Management
        Stock-in products
        Stock-out products
        Track product quantities

    5.Reporting
        Inventory dashboard
        Product stock summary

    6.Technical Features
        JSON data persistence
        Rich terminal tables and formatting
        Unit testing with Pytest
        Modular project structure
        Object-Oriented Programming principles


## Installation
Clone the Repository
git clone <repository-url>
Navigate into the Project
cd inventory-management-cli
Create a Virtual Environment
python3 -m venv venv
Activate the Virtual Environment

Linux/macOS:

source venv/bin/activate

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt

## Running the Application

Start the application using:

python main.py

You will see the following menu:

INVENTORY SYSTEM

1. Add Supplier
2. List Suppliers
3. Add Warehouse
4. Add Product
5. List Products
6. Stock In
7. Stock Out
8. Search Product
9. Dashboard
0. Exit

Select a number and follow the prompts.

## Example Workflow
Step 1: Add a Supplier

    Choose:

    1

    Enter:

    Name: Dell
    Email: sales@dell.com

Step 2: Add a Warehouse

    Choose:

    3

    Enter:

    Name: Main Warehouse
    Location: Nairobi

Step 3: Add a Product

    Choose:

    4

    Enter:

    SKU: LAP001
    Name: Dell Laptop
    Price: 65000
    Quantity: 10
    Supplier ID: 1
    Warehouse ID: 1

Step 4: View Products

    Choose:

    5

    The products will be displayed in a formatted table.

Step 5: Update Stock

    Stock In:

    6

    Stock Out:

    7

Step 6: Search Products

    Choose:

    8

    Enter a product name to search.

Step 7: View Dashboard

    Choose:

    9

    Displays inventory summary statistics.

## Running Tests

Run all tests:

pytest

Run tests with detailed output:

pytest -v

Run a specific test file:

pytest tests/test_product.py

## Data Persistence

The application stores data locally using JSON files located in the data/ directory:

suppliers.json
products.json
warehouses.json
transactions.json
state.json

This ensures data remains available between application runs.

## Technologies Used
Python 3.10+
Rich
Pytest
JSON
Object-Oriented Programming (OOP)

## Future Improvements
Product editing
Product deletion
Supplier deletion
Warehouse deletion
CSV export
PDF reports
Database integration (SQLite/PostgreSQL)
User authentication system
Author

Gad Ontune

Python CLI Inventory & Warehouse Management System