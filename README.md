### Languages and Tools

- **Python**: For developing the object-oriented system.
- **CSV Handling**: For reading and writing customer and product data.
- **Error Handling**: For ensuring the system runs smoothly even when errors occur.

# Warehouse Management Application using Object-Oriented Programming

## Overview

This project is a **warehouse management application** developed using object-oriented programming principles in Python. The goal of the project is to simulate a warehouse environment, where customers place orders for products, and the stock of products is updated accordingly. This application includes functionalities for managing customers, products, and orders, and provides a structured solution for warehouse operations. Additionally, the project introduces different types of customers—retail and wholesale—each with their own discount structures.

### Key Features

1. **Customer Management**:
   - The application manages customers by allowing the addition and retrieval of customer information.
   - Customers can be of two types: **Retail Customers** and **Wholesale Customers**.
   - Each customer type has its own discount structure, and these discounts are applied when placing orders.
   - The system allows dynamic updates to customer records, including discount rates.

2. **Product Management**:
   - Products in the warehouse are tracked by their **ID**, **name**, **price**, and **stock quantity**.
   - Products can be updated based on customer orders, with stock levels automatically reduced when orders are placed.
   - The application also allows for combo products, where multiple products are sold together as a single unit at a discounted price.

3. **Order Management**:
   - Orders are managed by associating customers with the products they purchase.
   - Each order can contain multiple products, and the application calculates the total price of the order based on the product prices and applicable discounts.
   - The order history is tracked, allowing for viewing previous orders, updating stock levels, and displaying the total cost of each order.

4. **Combo Products**:
   - A **Combo class** is introduced to handle products that are sold as a package (e.g., a combo pack containing multiple items).
   - Combo products are sold at a discount compared to the sum of their individual prices, and the application ensures that stock levels for each product in the combo are updated accordingly.

### System Design

1. **Customer Class**:
   - The `Customer` class contains customer attributes such as **ID** and **name**, as well as a method to retrieve discounts on orders.
   - Two types of customers are supported: **RetailCustomer** and **WholesaleCustomer**, each with specific discount structures.
   - **RetailCustomer**: Offered a flat discount rate on all orders if they have placed orders before.
   - **WholesaleCustomer**: Discounted rates are applied based on a threshold amount, with different rates for amounts above and below the threshold.

2. **Product Class**:
   - The `Product` class tracks information for individual products, including **ID**, **name**, **price**, and **stock**.
   - Products can be updated, and the stock is adjusted as orders are placed.

3. **Order Class**:
   - The `Order` class handles orders made by customers. Each order contains information about the **customer**, **products**, and **quantities** ordered.
   - The application updates stock levels when an order is completed and provides detailed billing information, including discounts applied.

4. **Combo Class**:
   - The `Combo` class represents a collection of products sold as a single item.
   - Combo products are offered at a discounted rate compared to the sum of their individual product prices.

5. **Records Class**:
   - The `Records` class serves as the central repository for managing customers and products.
   - It can read customer and product information from external files (`customers.txt` and `products.txt`) and update the product and customer lists dynamically.
   - The class includes methods to search for and list all customers and products.

6. **Operations Class**:
   - The `Operations` class provides the main interface for the program, allowing users to interact with the system through a menu-driven interface.
   - It supports operations such as placing orders, listing customers and products, and handling combo products.

### Tasks and Results

1. **Customer and Product Management**:
   - The system successfully reads customer and product data from external files and updates them dynamically.
   - Users can add new customers and products, view existing records, and manage stock levels efficiently.

2. **Order Processing**:
   - Orders are placed, and stock levels are updated accordingly.
   - The total cost of each order is displayed, with discounts applied based on the customer type.

3. **Combo Products**:
   - Combo products are successfully created and managed, with the application updating stock levels for each product in the combo when orders are placed.

4. **Error Handling**:
   - The system handles errors gracefully, such as invalid product quantities and file handling errors.
   - The menu-driven interface ensures smooth navigation and interaction with the system.

### Files in the Repository

- **`ITP_A2_3969393.py`**: Python file containing the code, which serves as the foundation written with no object-oriented concepts
- **`ITP_A3_3969393.py`**: Python file containing the main code, including the object-oriented implementation of the warehouse management system.

### How to Run the Project

1. **Download and Set Up**:
   - Download the Python files (`ITP_A3_3969393.py`) to your local machine.

2. **Run the Program**:
   - Run the program in a Python environment. The main menu will appear, allowing you to perform various operations such as placing orders, viewing customers, and managing products.

3. **Files**:
   - Ensure the `customers.txt` and `products.txt` files are available in the same directory for reading customer and product data.

### Data Source

The project uses customer and product data provided in external files (`customers.txt` and `products.txt`). These files contain information about existing customers, products, and their respective attributes.
