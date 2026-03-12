def deposit_balance():
    user_id = int(input("Enter your ID: "))
    password = input("Enter your password: ")
    amount = float(input("Enter amount to deposit: "))

    users = read_users()  # load all users
    found = False

    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]              # current balance
            user[3] = old_balance + amount     # add deposit
            print(f"Balance updated: {old_balance} + {amount} = {user[3]}")
            break

    if not found:
        print("User ID or password incorrect!")

    write_users(users)  # save all users back to file