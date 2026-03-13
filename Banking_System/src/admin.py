from accounts import create_account, update_account, delete_account
from display import print_transactions
from config import CONFIG

def admin_panel():
    admin_id = input("Enter admin ID: ")
    password = input("Enter password: ")
    
    with open(CONFIG["admin_file"]) as f:
        valid = any(line.strip().split()[0] == admin_id and line.strip().split()[1] == password for line in f)
    if not valid:
        print("Invalid admin credentials.")
        return
    
    # Admin menu logic (call accounts and display functions)