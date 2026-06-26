## Python Project
 Vehicle Management System (Car Rental CLI)

## Overview
 The Vehicle Management System is a Python-based CLI application that simulates a real-world car rental workflow using 
 Object-Oriented Programming. It provides separate Admin and Customer panels to manage vehicles, handle rentals, and
 track returns efficiently. This project demonstrates practical Python logic, user interaction flow, and basic system
 design for a rental management use case.

## Key Features
-  Admin Panel to manage vehicle inventory (add, remove, and view vehicles)
-  Customer Panel for customer operations and vehicle rentals
-  The system allows customers to rent available vehicles through the rent_vehicles function.
-  It also provides a smooth return process for rented vehicles using the return_vehicles function.
-  All data is managed using in-memory dictionaries to store and track vehicles and customer information.
-  Built using Object-Oriented Programming (OOP) with separate classes for Admin and Customer
-  Interactive Command-Line Interface (CLI) based user experience
-  Simple workflow-based system for managing rental operations

## Core Concept
-  Object-Oriented Programming (OOP)
-  Python Dictionaries for data storage
-  Functions and modular programming
-  Conditional statements and loops
-  Command-Line Interface (CLI) interaction

## Architecture
*The Vehicle Management System follows a simple modular and layered structure using Python.
-  The application starts from main.py, which acts as the entry point of the system.
-  The logic is divided into two main modules:
   * admin.py → Handles all admin-related operations 
   * customer.py → Handles customer actions 
-  Data is stored in in-memory dictionaries (vehicles and customers) shared between modules.
-  The system follows a menu-driven CLI flow, where user input controls navigation between Admin and Customer panels.

## How to Run
* Clone the Repository
- "git clone https://github.com/sansreebrama33-wq/vehicle-management-system.git"
* Move into the project folder
- "cd vehicle-management-system"
* Run the program
- "python main.py"

## Screenshots
* Main menu
! [Main menu](screenshot/main-panel.png)
* Admin Panel
! [Admin panel](screenshot/admin-panel.png)
* Customer Panel
! [Customer panel](screenshot/customer-panel.png)
* Rented Vehicle
! [Rented vehicle](screenshot/rented-vehicle.png)
* Returned Vehicle
! [Returned vehicle](screenshot/returned-vehicle.png)

## Conclusion
   This project demonstrates a simple Vehicle Management System built using Python and OOP concepts. It helped in
 understanding modular programming, CLI-based interaction, and basic data handling using dictionaries.
