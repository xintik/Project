#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Employee {
private:
    vector<vector<pair<int, string>>> em;  // vector of vector of pairs {age, name}

public:
    // Constructor no longer takes input
    Employee() {}

    // Function to add employee data
    void addEmployee() {
        int id, age;
        string name;
        cout << "\n\tEnter the id: ";
        cin >> id;

        // Resize the vector to accommodate the id
        if (id >= em.size()) {
            em.resize(id + 1);  // Resize to allow access for larger ids
        }

        cout << "\n\tEnter the age: ";
        cin >> age;
        cout << "\n\tEnter the name: ";
        cin >> name;

        em[id].push_back({age, name});  // Store {age, name} pair
    }

    // Function to display employee data
    void getdata() {
        for (int i = 0; i < em.size(); i++){// i represent the id and em[i,j] represent the value of pair  em[i][j].first is the value of id number and the second is the name of thes man
            for (int j = 0; j < em[i].size(); j++) {
                cout << "\n\tID: " << i << ", Age: " << em[i][j].first << ", Name: " << em[i][j].second << endl;
            }
        }
    }
    void one_employee_information()
    {
        int flag=0;
        int id;
        cout<<"\n\tEnter the id: ";
        cin>>id;
        for(int i=0;i<em.size();i++)
        {
            for(int j=0;j<em[i].size();j++)
            {
                if(i==id)
                {
                    cout<<"\n\tName : "<<em[i][j].second<<" Age: "<<em[i][j].first<<endl;
                    flag=1;
                }
            }
        }
        if(flag==0) cout<<"\n\tId is invalid...";
    }
    void delet()
    {
        int flag=0;
        int id;
        cout<<"\n\tEnter the id : ";
        cin>>id;
        for(int i=0;i<em.size();i++)
        {
            for(int j=0;j<em[i].size();j++)
            {
                if(id==i)
                {
                    em[id].clear();
                    flag=1;
                }
            }
        }
        if(flag==0) cout<<"\n\tInvald id...";
    }
};

int main() {
    Employee obj;
    int x;
    do{
          cout<<"\n\t\t\tEmployee Panal";
   cout<<"\n\t1.Add New employee";
   cout<<"\n\t2.Search Employee information";
   cout<<"\n\t3.Search all employee information";
   cout<<"\n\t4.Delete Employee information";
   cout<<"\n\t5.Exit";
   cout<<"\n\tEnter your choice: ";
   cin>>x;
   switch(x)
   {
   case 1:
       obj.addEmployee();
    break;
   case 2:
       obj.one_employee_information();
    break;
   case 3:
       obj.getdata();
    break;
   case 4:
       obj.delet();
    break;
   case 5:
    exit(0);
   default:
    cout<<"\n\tWrong input please try again....";
   }

    }while(x!=5);



}
