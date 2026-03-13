from utils import read_users, write_users, id_exists
import logging
import json

# Load config
with open("../config/config.json", "r") as f:
    config = json.load(f)

def Create_account():
    user_id = int(input("Enter ID number: "))
    if id_exists(user_id):
        print("This ID already exists!")
        logging.warning(f"Failed account creation attempt: ID {user_id} exists")
        return

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    father_first = input("Father first name: ")
    father_last = input("Father second name: ")
    password = input("Enter password: ")
    balance = float(input("Enter initial deposit: "))

    data = [user_id, password, phone, balance, first_name, last_name, father_first, father_last]

    users = read_users()
    users.append(data)
    write_users(users)

    print("Account created successfully!")
    logging.info(f"Account created: User {user_id}, Initial balance: {balance}")

def Update_User_account():
    user_id = int(input("Enter your ID: "))
    password = input("Enter your password: ")

    users = read_users()
    found = False
    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            print("User authenticated! Update info (leave blank to keep current):")
            user[4] = input(f"First name [{user[4]}]: ") or user[4]
            user[5] = input(f"Last name [{user[5]}]: ") or user[5]
            user[2] = input(f"Phone number [{user[2]}]: ") or user[2]
            user[6] = input(f"Father first name [{user[6]}]: ") or user[6]
            user[7] = input(f"Father second name [{user[7]}]: ") or user[7]
            user[1] = input(f"Password [hidden]: ") or user[1]

            write_users(users)
            print("Information updated successfully!")
            logging.info(f"User {user_id} updated account information")
            break

    if not found:
        print("User ID or password incorrect!")
        logging.warning(f"Failed account update attempt: User {user_id}")

def Delete_user_account():
    user_id = int(input("Enter your ID: "))
    password = input("Enter your password: ")

    users = read_users()
    found = False

    for i, user in enumerate(users):
        if user[0] == user_id and user[1] == password:
            found = True
            confirm = input(f"Are you sure you want to delete account {user_id}? (yes/no): ").lower()
            if confirm == "yes":
                users.pop(i)
                write_users(users)
                print(f"Account {user_id} deleted successfully")
                logging.info(f"Account deleted: User {user_id}")
            else:
                print("Account deletion cancelled")
            break

    if not found:
        print("User ID or password incorrect!")
        logging.warning(f"Failed account deletion attempt: User {user_id}")