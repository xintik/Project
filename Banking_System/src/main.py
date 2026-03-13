from accounts import Create_account, Update_User_account, Delete_user_account
from transactions import Deposit, Withdraw, Send_money

def menu():
    while True:
        print("\n1. Admin Panel")
        print("2. User Panel")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            # call your admin functions (Create/Update/Delete accounts)
            pass
        elif choice == "2":
            # call user functions (Deposit, Withdraw, Send_money)
            pass
        elif choice == "3":
            break