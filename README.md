# Python–MySQL Vending Machine Management System

## Overview
This project is a console-based vending machine application built using Python
and MySQL. It simulates real-world inventory management by supporting customer
purchases and administrative operations through a relational database backend.

## Features
- MySQL database setup and schema creation
- Customer interface for browsing products and purchasing items
- Admin interface for stock updates, price changes, product removal, and search
- Inventory updates with transactional consistency
- Sorting and searching products by multiple fields

## Technologies Used
- Python
- MySQL
- SQL
- mysql-connector-python

## Key Concepts Demonstrated
- Database design and relational schema management
- CRUD operations using SQL
- Transaction handling and data integrity
- Modular Python programming
- Structured problem-solving

## How to Run
1. Install dependencies:
pip install mysql-connector-python
2. Ensure MySQL is running locally
3. Run the main script:
python main.py

## Project Structure

- `main.py` – Entry point of the application
- `db_setup.py` – Database and table initialization
- `admin.py` – Admin operations (add/update/remove products)
- `customer.py` – Customer operations and billing
