# Python Banking System

This project is a **Python Banking System** that simulates a simple banking environment with **Admin** and **User** panels.  
All data is stored in **text files**, making it lightweight and easy to use.

---

## File Overview

| File | Description |
|------|-------------|
| `main.py` | Entry point of the program |
| `account.py` | Functions to create, update, and delete user accounts |
| `admin.py` | Admin login and panel functions |
| `transaction.py` | Logs and views transaction history |
| `database.py` | File handling and data management |
| `user_information.txt` | Stores all user data |
| `Admin_Information.txt` | Stores admin credentials |
| `README.md` | Project documentation |

---

## Admin Panel

Admins log in using credentials stored in `Admin_Information.txt`.  

**Features:**
1. **Create Account** – Add new users with unique IDs  
2. **Update Account** – Modify existing user information  
3. **Delete User Account** – Remove users from the system  
4. **View Transaction History** – View all user transactions

---

## User Panel

Users log in using their ID and password stored in `user_information.txt`.  

**Features:**
1. **Check Balance** – View current account balance  
2. **Deposit Money** – Add funds to the account  
3. **Withdraw Money** – Withdraw funds from the account  
4. **View Account Details** – See personal account information

---

## Data Structure

**`user_information.txt`** – Each user is stored as:  
