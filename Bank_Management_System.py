
def id_exists(user_id):
    try:
        f = open("/home/shamim/Desktop/ML/Project/user_information.txt", "r")
        for line in f:
            data = eval(line.strip())   # convert string list to list
            if data[0] == user_id:      # first element = id
                f.close()
                return True
        f.close()
    except FileNotFoundError:
        return False

    return False



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

    f = open("/home/shamim/Desktop/ML/Project/user_information.txt", "a")
    f.write(str(data) + "\n")
    f.close()

    print("Account created successfully!")




def Admin():
    print("\t\t\nWellcome Admin Panel")
    id = input("\t\t\nEnter your admin Id 1001 : ")
    password = input("Enter your Password shamim1212 :")
    flag = False
    with open("/home/shamim/Desktop/ML/Project/Admin_Information.txt", "r") as f:
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
        print("6. Exit")

        try:
            choice = int(input("Enter Your choice : "))
        except ValueError:
            print("Invalid Input ! Please Enter a number.")
            continue


        if choice == 1:
            Creat_account()
        elif choice == 2:
            print("2. Update account ")
        elif choice == 3:
            print("3. Delete user account")
        elif choice == 4:
          print("4. View Transaction History ")  
        elif choice == 5:
           print("5. User information ")
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
            print("User Panel")
          
        elif choice == 3:
            print("Log Out Successfully!")
            break  
        else:
            print("Invalid choice, please try again!")




print("Welcome to Bapar Bank")
menu()