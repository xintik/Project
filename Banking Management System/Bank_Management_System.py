
def id_exists(user_id):
    try:
        f = open("/home/shamim/Desktop/ML/Project/Banking Management System/user_information.txt", "r")
        for line in f:
            data = eval(line.strip())   # convert string list to list
            if data[0] == user_id:      # first element = id
                f.close()
                return True
        f.close()
    except FileNotFoundError:
        return False

    return False



def read_users():
    users = []
    try:
        with open("/home/shamim/Desktop/ML/Project/Banking Management System/user_information.txt", "r") as f:
            for line in f:
                if line.strip():
                    users.append(eval(line.strip()))
    except FileNotFoundError:
        pass
    return users



def write_users(users):
    with open("/home/shamim/Desktop/ML/Project/Banking Management System/user_information.txt", "w") as f:
        for user in users:
            f.write(str(user) + "\n")



#1
def Creat_account():

    id = int(input("Enter id number : "))

    if id_exists(id):
        print("This Id Already Exist please try again !!!")
        return 

    name1 = input("Enter user first name  : ")
    name2 = input("Enter user last name : ")
    
    phone_number = input("Enter user Phone number :")
    f_f_n = input("Enter father first name :")
    f_s_n = input("Father second name : ")
    password = input("Enter user password : ")
    balance = float(input("Enter your deposite balance : "))

    data = [id, password, phone_number, balance, name1, name2, f_f_n, f_s_n]

    f = open("/home/shamim/Desktop/ML/Project/Banking Management System/user_information.txt", "a")
    f.write(str(data) + "\n")
    f.close()

    print("Account created successfully!")

#2
def  Update_User_account():
   user_id = int(input("Enter your ID: "))
   password = input("Enter your password: ")

   users = read_users()
  # print(users)
   found = False

   for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            print("User authenticated! You can now update your info.")
            
            # Ask user for new info; if left blank, keep old info
            user[4] = input(f"First name [{user[4]}]: ") or user[4]
            user[5] = input(f"Last name [{user[5]}]: ") or user[5]
            user[2] = input(f"Phone number [{user[2]}]: ") or user[2]
            user[6] = input(f"Father first name [{user[6]}]: ") or user[6]
            user[7] = input(f"Father second name [{user[7]}]: ") or user[7]
            user[1] = input(f"Password [hidden]: ") or user[1]

            print("Information updated successfully!")
            break

   if not found:
        print("User ID or password incorrect!")

   write_users(users)

#3
def  Delete_user_account():
   user_id = int(input("Enter your ID: "))
   password = input("Enter your Password : ")

   users = read_users()
   found = False


   # loop through user to find the matching account 
   for i , user in enumerate(users):
       if user[0] == user_id and user[1] == password:
           found = True
           confirm = input(f"Are you sure you want to delete account {user_id}? (yes/no): ").lower()
           if confirm == "yes":
               users.pop(i) # remove ith user from the list
               write_users(users)
               print(f"Account {user_id} delete successfully ")
           else:
               print("Account deletion cancelled ")
           break 

   if not found:
    print("User ID or Password incorrect!")


#4
def Transection_history():
    import ast

    transactions = []
    try:
        with open("/home/shamim/Desktop/ML/Project/Banking Management System/Transfer.txt", "r") as f:
            for line in f:
                if line.strip():
                    transactions.append(ast.literal_eval(line.strip()))
    except FileNotFoundError:
        print("No transaction history found.")
        return

    if not transactions:
        print("No transactions available.")
        return

    # Header
    print(f"{'No.':<5}{'Sender ID':<15}{'Receiver ID':<15}{'Amount':<10}")
    print("-" * 50)

    # Print each transaction
    for i, transaction in enumerate(transactions, 1):
        if isinstance(transaction, list) and len(transaction) == 3:
            sender, receiver, amount = transaction
            print(f"{i:<5}{sender:<15}{receiver:<15}{amount:<10}")
        else:
            print(f"{i}. Invalid transaction format: {transaction}")

    print("-" * 50)

# Example usage



#5
def view_user_information():
    user_id = int(input("Enter your ID: "))
    users = read_users()  # This should return a list of users
    found = False

    for user in users:
        if user[0] == user_id:
            found = True
            print("\nUser Information:")
            print("-" * 50)
            print(f"{'Field':<20}{'Value':<30}")
            print("-" * 50)
            print(f"{'ID':<20}{user[0]:<30}")
            print(f"{'Contact Number':<20}{user[2]:<30}")
            print(f"{'Balance':<20}{user[3]:<30}")
            print(f"{'First Name':<20}{user[4]:<30}")
            print(f"{'Last Name':<20}{user[5]:<30}")
            print(f"{'Father First Name':<20}{user[6]:<30}")
            print(f"{'Father Last Name':<20}{user[7]:<30}")
            print("-" * 50)
            break

    if not found:
        print("User ID not found!")

#i 6 payment history 
def payment_history():
    import ast

    transactions = []
    try:
        with open("/home/shamim/Desktop/ML/Project/Banking Management System/Report.txt", "r") as f:
            for line in f:
                if line.strip():
                    transactions.append(ast.literal_eval(line.strip()))
    except FileNotFoundError:
        print("No Payment history found.")
        return

    if not transactions:
        print("No payment available.")
        return

    # Header
    print(f"{'No.':<5}{'Sender ID':<15}{'Amount':<10}{'BIll name':<15}{'Bill number':<15}")
    print("-" * 65)

    # Print each transaction
    for i, transaction in enumerate(transactions, 1):
        if isinstance(transaction, list) and len(transaction) == 4:
            sender, amount,BIll_name , BIll_number = transaction
            print(f"{i:<5}{sender:<15}{amount:<10}{BIll_name:<15}{BIll_number:<15}")
        else:
            print(f"{i}. Invalid payment format: {transaction}")

    print("-" * 50)



#ii 1 
def Chack_balance():
    print("Balnace")
    user_id = int(input("Enter user id : "))
    password = input("Enter password : ")
    users = read_users()
    found = False
    
    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            print(f"\nBalance = [{user[3]}] " )
            break

    if not found:
     print("User ID or password incorrect!")


#ii 2 Deposit
def Deposite():
    user_id = int(input("Enter the user id : "))
    password = input("Enter the Password : ")
    amount = float(input("Enter Deposite amount : "))
    if(amount < 0) :
        print("Enter the possitive amount !!!")
        return 
    
    users = read_users()
    found = False

    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]
            user[3] = user[3] + amount
            new_balance = user[3]
            write_users(users)
            print(f"\t\t\nOld Balance = [{old_balance}] and Deposite = [{amount}] New balance = [{new_balance}]")
            return 
    if not found :
        print("User ID or password incorrect!")



#ii 3 withdrow 
def Withdrow():
     user_id = int(input("Enter the user id : "))
     password = input("Enter the Password : ")
     amount = float(input("Enter Withdrow amount : "))
   
     users = read_users()
     found = False

     for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]
            if amount >= old_balance:
                print("Influence Balance ")
                return 
            user[3] = user[3] - amount
            new_balance = user[3]
            write_users(users)
            print(f"\t\t\nOld Balance = [{old_balance}] and withdraw = [{amount}] New balance = [{new_balance}]")
            return 
     if not found :
        print("User ID or password incorrect!")




#ii 5 payment 
def Payment():
    user_id = int(input("Enter user id : "))
    password = input("Enter password ")  
    amount = float(input("Enter payment amount : "))
    bill_name = input("Enter the bil name : ")
    payment_number = input("Enter the payment number : ")
    data = [user_id,amount,bill_name, payment_number]
    users = read_users()
    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]
            if amount >= old_balance:
                print("Influence Balance ")
                return 
            user[3] = user[3] - amount
            new_balance = user[3]
            write_users(users)
            print(f"\t\t\nOld Balance = [{old_balance}] and payment = [{amount}] New balance = [{new_balance}]")
            f = open("/home/shamim/Desktop/ML/Project/Report.txt", "a")
            f.write(str(data) + "\n")
            f.close()
            print("Payment successfully!")
            return 
        
    if not found :
        print("User ID or password incorrect!")

#ii 5
def Send_money():
    user_id = int(input("Enter user id : "))
    password = input("Enter the password: ")
    users = read_users()
    Received_user_id = int(input("Enter the receving user id : "))
    amount = float(input("Enter the amount : "))
    found = False
    data = [user_id,Received_user_id,amount]
    for user in users:
        if user[0] == user_id and user[1] == password:
            found = True
            old_balance = user[3]
            if amount >= old_balance:  #chack enoug balance is avaiable
                print("Influence Balance ")
                return 
            if  not id_exists(Received_user_id):#chack receving id is exit
                print("Invalid Receiving id !!!")
                return 
            user[3] = user[3] - amount
            new_balance = user[3]
            write_users(users)
            print(f"\t\t\nOld Balance = [{old_balance}] Transfer amount  = [{amount}] New balance = [{new_balance}]")
            f = open("/home/shamim/Desktop/ML/Project/Banking Management System/Transfer.txt", "a")
            f.write(str(data) + "\n")
            f.close()
            print("Payment successfully!")
            recevied  = read_users()
            for rev in  recevied :
                if(rev[0]==Received_user_id): rev[3] = rev[3] + amount
                write_users( recevied)
            return 
        
    if not found :
        print("User ID or password incorrect!")
# i
def Admin():
    print("\t\t\nWellcome Admin Panel")
    id = input("\t\t\nEnter your admin Id 1001 : ")
    password = input("Enter your Password shamim1212 :")
    flag = False
    with open("//home/shamim/Desktop/ML/Project/Banking Management System/Admin_Information.txt", "r") as f:
     for line in f:
        parts = line.strip().split()  # split line by spaces
        chack_id = parts[0]                 # first item is ID
        chack_pass = parts[1]            # last item is salary
        if (id == chack_id) and (password == chack_pass):
            flag = True
            break


    if(flag == False): 
        print("Invalid id or Password please try again !!! ") 
        return 
    while True:
        print("\n1. Create an account ")
        print("2. Update account ")
        print("3. Delete user account")
        print("4. View Transaction History ")
        print("5. User information ")
        print("6. Payment History ")
        print("7. Exit")

        try:
            choice = int(input("Enter Your choice : "))
        except ValueError:
            print("Invalid Input ! Please Enter a number.")
            continue


        if choice == 1:
            Creat_account()
        elif choice == 2:
            Update_User_account()
        elif choice == 3:
           Delete_user_account()
        elif choice == 4:
         Transection_history() 
        elif choice == 5:
         view_user_information()
        elif choice == 6:
            payment_history()
        elif choice == 7 :
            break 
        else:
            print("Invalid choice, please try again!")

     
#ii
def User():
 while True:
    print("\t\nWellcome user panel\n")
    print("1. Chack Balance ")
    print("2. Deposite")
    print("3. Withdrow")
    print("4. Payment")
    print("5. Send money ")
    print("6. Exit ")
    try:
            choice = int(input("Enter Your choice : "))
    except ValueError:
        print("Invalid Input ! Please Enter a number.")
        continue
    
    if choice == 1:
          Chack_balance()
    elif choice == 2:
           Deposite()
    elif choice == 3:
         Withdrow()
    elif choice == 4:
          Payment()
    elif choice == 5:
       Send_money()
    elif choice == 6: 
         break 
    else:
            print("Invalid choice, please try again!")


    



def menu():
    while True:
        print("\n1. Admin")
        print("2. User")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
           
            Admin()
           
        elif choice == 2:
           User()
          
        elif choice == 3:
            print("Log Out Successfully!")
            break  
        else:
            print("Invalid choice, please try again!")




print("Welcome to Bapar Bank")
menu()