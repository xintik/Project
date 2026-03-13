from utils import read_users, write_users, id_exists
import logging
import json

# Load config
with open("../config/config.json", "r") as f:
    config = json.load(f)

def Deposit():
    user_id = int(input("Enter user ID: "))
    password = input("Enter password: ")
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Enter a positive amount!")
        return

    users = read_users()
    found = False
    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]
            user[3] += amount
            write_users(users)
            print(f"Old Balance: {old_balance}, Deposit: {amount}, New Balance: {user[3]}")
            logging.info(f"User {user_id} deposited {amount}. New balance: {user[3]}")
            break

    if not found:
        print("User ID or password incorrect!")
        logging.warning(f"Failed deposit attempt: User {user_id}")

def Withdraw():
    user_id = int(input("Enter user ID: "))
    password = input("Enter password: ")
    amount = float(input("Enter withdraw amount: "))

    users = read_users()
    found = False
    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]
            if amount > old_balance:
                print("Insufficient balance")
                logging.warning(f"Failed withdraw attempt: User {user_id}, Amount {amount}")
                return
            user[3] -= amount
            write_users(users)
            print(f"Old Balance: {old_balance}, Withdraw: {amount}, New Balance: {user[3]}")
            logging.info(f"User {user_id} withdrew {amount}. New balance: {user[3]}")
            break

    if not found:
        print("User ID or password incorrect!")
        logging.warning(f"Failed withdraw attempt: User {user_id}")

def Send_money():
    user_id = int(input("Enter your user ID: "))
    password = input("Enter your password: ")
    receiver_id = int(input("Enter receiver ID: "))
    amount = float(input("Enter amount: "))

    users = read_users()
    found = False

    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            if amount > user[3]:
                print("Insufficient balance")
                logging.warning(f"Failed transfer: User {user_id} tried to send {amount}")
                return
            if not id_exists(receiver_id):
                print("Receiver ID not found")
                logging.warning(f"Failed transfer: User {user_id} tried to send to invalid ID {receiver_id}")
                return
            user[3] -= amount
            for receiver in users:
                if receiver[0] == receiver_id:
                    receiver[3] += amount
                    break
            write_users(users)
            print(f"Transferred {amount} from {user_id} to {receiver_id}")
            logging.info(f"User {user_id} sent {amount} to {receiver_id}")
            break

    if not found:
        print("User ID or password incorrect!")
        logging.warning(f"Failed transfer attempt: User {user_id}")