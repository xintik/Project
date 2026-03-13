# Bapar Bank 🏦

**Bapar Bank** is a command-line Python banking system for managing user accounts, transactions, and payments.  
Admins can manage users and view reports, while users can deposit, withdraw, send money, and pay bills.

---

## Features

### User
- Check balance  
- Deposit & withdraw money  
- Send money to other users  
- Make payments  
- View transaction & payment history  

### Admin
- Create, update, and delete user accounts  
- View transaction & payment reports  

### Other
- Action logging in `logs/app.log`  
- Data stored in `data/` folder  
- Configurable file paths in `config/config.json`  

---

## Folder Structure


Banking_System/
├── src/
│ ├── main.py
│ ├── utils.py
│ ├── accounts.py
│ ├── transactions.py
│ ├── display.py
│ ├── admin.py
│ └── user.py
├── data/
│ ├── user_information.txt
│ ├── Transfer.txt
│ ├── Report.txt
│ └── Admin_Information.txt
├── config/
│ └── config.json
├── logs/
│ └── app.log
└── README.md


---

## Quick Start

1. Clone or download the repo  
2. Navigate to the project:

```bash
cd Banking_System/src

Run the program:

python main.py

Admin credentials (Admin_Information.txt):

Admin ID: 1001
Password: shamim1212

Use the menu to manage accounts and perform transactions

Notes

Passwords are stored in plain text (consider hashing for production)

All actions are logged in logs/app.log

Data is stored in data/ folder

Author: Md. Shamim Reza
Email: md.shamimreza9520@gmail.com

Date: 2026-03-13
