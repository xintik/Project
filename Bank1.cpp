#include<iostream>
#include<stdio.h>
#include<vector>
#include<windows.h>
#include<fstream>
using namespace std;

class Bank1{
    protected:
    string name,id,adress,fname,phone_number;
    int pin;
    float balance;
    public:
    Bank1(){}
    void menu();
    void new_user();
    void chack_balance();
    void deposite();
    void withdrow();
    void details();
    void delete_user();
    void report();



};

void Bank1::menu()
{
 cout<<"\n\n\t\tBank Management System";
    int x;
    do{
        cout<<"\n\t1.New User";
        cout<<"\n\t2.Chack Balance";
        cout<<"\n\t3.Deposit";
        cout<<"\n\t4.Withdrow";
        cout<<"\n\t5.User detail";
         cout<<"\n\t6.Delete user account";
        cout<<"\n\t7.Exit";
        cout<<"\n\tEnter your choice: ";
        cin>>x;
        switch(x)
        {
            case 1:
             new_user();
            break;
            case 2:
            chack_balance();
            break;
            case 3:
            deposite();
            break;
            case 4:
            withdrow();
            break;
            case 5:
            details();
            break;
            case 6:
            delete_user();
            break;
            case 7:
            exit(0);
            default :
            cout<<"\n\tYour choice is wrong try agein...";
        }
    }while(x!=7);
}

void Bank1::new_user()
{
     fstream file;
    p:
    system("cls");
   
    string n,fn,i,ad,pn;
    int p;
    float b;
    cout<<"\n\tUser ID : ";
     cin>>id;
     cout<<"\n\tUser Name: ";
     cin>>name;
     cout<<"\n\tUser father Name: ";
     cin>>fname;
     cout<<"\n\tUser Adress : ";
     cin>>adress;
     cout<<"\n\tUser pin (5 digit) : ";
     cin>>pin;
     cout<<"\n\tUser phone Number : ";
     cin>>phone_number;
     cout<<"\n\tUser Balance : ";
     cin>>balance;
     file.open("bank1.txt",ios::in);// only for read >> this is read sign
     if(!file)
     {
        file.open("bank1.txt",ios::out|ios::app);
        file<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
        file.close();
     }
     else
     {
        //thats mean file is exit so we can moov;
       // file.open("bank1.txt",ios::out|ios::app); //open for input <<this is input sign >>output sign
        file>>n>>fn>>i>>p>>ad>>pn>>b;//take input from file and chack
        while(!file.eof())
        {
            if(id==i)
            {
                cout<<"\n\tThis id is already exit";
               // getchar();
                goto p;
            }
            file>>n>>fn>>i>>p>>ad>>pn>>b;//take input from file and chack every time

        }
        file.close();

        // now this id is unique
        file.open("bank1.txt",ios::app|ios::out);
        file<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
       
        file.close();
 cout<<"\n\tAdd new user sussessfully";
     }


}

void Bank1::chack_balance()
{
    string i;
    float b;
    fstream file;
    cout<<"\n\tEnter the user id: ";
    cin>>i; 
    file.open("bank1.txt",ios::in); //only read >> use this sign;
    if(!file)
    {
        cout<<"\n\tFile does not exit...";
    }
    else 
    {
        int flag=0;
         file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
         while(!file.eof())
         {
             if(i==id)
             {
                cout<<"\n\t id : "<<id<<" Balance: "<<balance;
                flag=1;
                break;
             }
             file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
         }
         file.close();
         if(flag==0) cout<<"\n\tInvalid id";
    }
    
}
 void Bank1::deposite()
 {
    fstream file,file1,file2;
    string i;
    float b;
    int flag=0;
    SYSTEMTIME x;
    cout<<"\n\tEnter user id: ";
    cin>>i;
    cout<<"\n\tEnter deposit balance: ";
    cin>>b;
    file.open("bank1.txt",ios::in);
  if(!file)
  {
    cout<<"\n\tFile does not exit";
  }
    else 
    {
        file1.open("bank2.txt",ios::app|ios::out);
     file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
     while(!file.eof())
     {
       if(i==id)
       {
             balance+=b;
              file1<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
              flag=1;
       }
      else
      {
        file1<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
      }
       file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
       
     }
     file.close();
     file1.close();
     remove("bank1.txt");
     rename("bank2.txt","bank1.txt");
     if(flag==1)
     {

    cout<<"\n\tDeposite sussesfully";
    file2.open("t_list.txt",ios::app|ios::out);
    GetSystemTime(&x);
    file2<<" "<<id<<" "<<name<<" "<<"Deposite"<<" "<<b<<" "<<x.wDay<<"-"<<x.wMonth<<"-"<<x.wYear<<endl;
    file2.close();


     }
      
     else cout<<"\n\tInvalid id";
    }

 }

 void Bank1::withdrow()
 {
    fstream file,file1,file2;
    string test_id;
    SYSTEMTIME x;

    float b;
    int flag=0;
    cout<<"\n\tEnter the id: ";
    cin>>test_id;
    cout<<"\n\tEnter the balance: ";
    cin>>b;
    file.open("bank1.txt",ios::in);
    if(!file)
    {
        cout<<"\n\tfile does not exit";
    }
    else 
    {
        file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
        file1.open("bank2.txt",ios::app|ios::out);
        while(!file.eof())
        {
            if(test_id==id)
            {
                if(balance>=b)
                {
                balance-=b;
                file1<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
                 flag=1;
                }
                else 
                file1<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
                
               
            }
            else
            {
             file1<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
            }
             file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
        }
        
        file.close();
        file1.close();
    }
    remove("bank1.txt");
    rename("bank2.txt","bank1.txt");
    if(flag==0) cout<<"\n\tInfluence Balance try again";
    else
    {
   cout<<"\n\tWithdrow sussefully";
   GetSystemTime(&x);
    file2.open("t_list.txt",ios::app|ios::out);
    file2<<" "<<id<<" "<<name<<" "<<"Withdrow"<<" "<<b<<" "<<x.wDay<<"-"<<x.wMonth<<"-"<<x.wYear<<endl;
    file2.close();
    } 
 }
 void Bank1::details()
 {
    fstream file;
    file.open("bank1.txt",ios::in);
    if(!file) cout<<"file does not exit";
    else
    {
        
        file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
        while(!file.eof())
        {
             cout<<"\n\tName : "<<name;
              cout<<"\n\tFather Name : "<<fname;
               cout<<"\n\tid : "<<id;
                cout<<"\n\tpin : "<<pin;
                 cout<<"\n\tadress : "<<adress;
                  cout<<"\n\tPhone Number : "<<phone_number;
                   cout<<"\n\tBalance : "<<balance;
                   cout<<"\n\t-   -   -   -   -    -   -   -   -";
                    file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;

        }
     file.close();
    }
 }
 void Bank1::delete_user()
 {
    fstream file,file1;
    string i;
    cout<<"\n\tEnter id : ";
    cin>>i;
    file.open("bank1.txt",ios::in);
    if(!file) cout<<"\n\tfile does not exit";
    else 
    {
        file1.open("bank2.txt",ios::app|ios::out);
        file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
        while(!file.eof())
        {
            if(id==i)
            {
                cout<<"\n\tDelet user id sussesfully";
            }
            else 
            {
                file1<<" "<<name<<" "<<fname<<" "<<id<<" "<<pin<<" "<<adress<<" "<<phone_number<<" "<<balance<<endl;
            }
            file>>name>>fname>>id>>pin>>adress>>phone_number>>balance;
        }
        file.close();
        file1.close();

    }
  remove("bank1.txt");
  rename("bank2.txt","bank1.txt");

 }
 class Manager: public Bank1{
    private :
    string pass;
    public:
    Manager(){}
    void menu();
    void all_report();

 };
 void Manager :: menu()
 {
    cout<<"\n\tManager Panal";
    
    int x;
      
    do{
        cout<<"\n\t1.New User";
        cout<<"\n\t2.Chack Balance";
        cout<<"\n\t3.Deposit";
        cout<<"\n\t4.Withdrow";
        cout<<"\n\t5.User detail";
         cout<<"\n\t6.Delete user account";
         cout<<"\n\t7.Transection report";
        cout<<"\n\t8.Exit";
        cout<<"\n\tEnter your choice: ";
        cin>>x;
        switch(x)
        {
            case 1:
             new_user();
            break;
            case 2:
            chack_balance();
            break;
            case 3:
            deposite();
            break;
            case 4:
            withdrow();
            break;
            case 5:
            details();
            break;
            case 6:
            delete_user();
            break;
            case 7:
            all_report();
            break;
            case 8:
           exit(0);
            default :
            cout<<"\n\tYour choice is wrong try agein...";
        }
    }while(x!=8);
    }
    
 
 void Manager::all_report()
 {
    fstream file;
    string n,i,date,t;
    float b;
    file.open("t_list.txt",ios::in);
    if(!file) cout<<"\n\tFile does not exit";
    else 
    {
        file>>i>>n>>t>>b>>date;
        while(!file.eof())
        {
         cout<<"Name: "<<n<<" id: "<<i<<" Trensection : <<"<<t<<" balance: "<<b<<" date: "<<date<<endl;
         file>>i>>n>>t>>b>>date;
        }
        file.close();
    }
 }
 

int main()
{
    int x;
    
    Bank1 obj;//constructor
    
    Manager em;//constructor

do{
    
       char ch;
    string gmail;
    string pass;
     
 cout<<"\n\n\t\tWellcome to Bapar Bank";
   cout<<"\n\t1.Employee";
   cout<<"\n\t2.Manager";
   cout<<"\n\t3.Exit";
   cout<<"\n\tEnter your choice: ";
   cin>>x;
   switch(x)
   {
  case 1:
  obj.menu();//pllymorphism
  break;
  case 2:
   
    cout << "\n\nPassword: ";
          cin>>pass;
    cout<<"\n\tEnter gmail adress: ";
    cin>>gmail;
    if(pass=="12345" && gmail=="Shamim@gmail.com")
  em.menu();//polymorphism
  else cout<<"\n\twrong password or gmail";
  break;

  case 3:
  exit(0);

   }
}while(x!=3);
return 0;
  
  
    
   
}