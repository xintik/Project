

#include<iostream>
#include<fstream>
using namespace std;
class gread{
    protected:
    string name,adress;
    int roll,reg;
    float gpa;

    public:
    void menu();
    void record();
    void grad();
    void calculate_gpa();

};
void gread::menu()
{
    int choice;
    while(true)
    {
    cout<<"\n\t1.Student Gread";
    cout<<"\n\t2.Calculate GPA";
    cout<<"\n\t3.Student record";
    cout<<"\n\t4.Exit";
    cout<<"\n\tEnter your choice: ";
    cin>>choice;
    switch(choice)
    {
      case 1:
      grad();
      break;
      case 2:
      calculate_gpa();
      break;
      case 3:
      record();
      break;
      case 4:
      exit(0);
      default :
      cout<<"\n\tYour choice is wrong....";
    }
    }


}
void gread :: record()
{
    fstream file;
    cout<<"\n\tEnter student name: ";
    cin>>name;
    cout<<"\n\tEnter the roll number : ";
    cin>>roll;
    cout<<"\n\tEnter the reg number: ";
    cin>>reg;
    cout<<"\n\tEnter your GPA: ";
    cin>>gpa;
    cout<<"\n\tEnter the student adress: ";
    cin>>adress;

    file.open("Student record.txt",ios::out|ios::app);
    file<<" "<<name<<" "<<roll<<" "<<reg<<" "<<gpa<<" "<<adress<<endl;
    file.close();

}
void gread::grad()
{
    fstream file;
    int test_roll,test_reg;
    int flag=0;
    cout<<"\n\tEnter your roll number: ";
    cin>>test_roll;
    cout<<"\n\tEnter your reg number: ";
    cin>>test_reg;
     file.open("Student record.txt",ios::in); // read the file sign is >>
     file>>name>>roll>>reg>>gpa>>adress;
     while(!file.eof())
     {
          if(roll==test_roll && reg==test_reg)
          {
            cout<<"\n\tName :"<<name<<" GPA: "<<gpa<<endl;
            flag=1;
          }
           file>>name>>roll>>reg>>gpa>>adress;

     }
     if(flag==0) cout<<"\n\tinvalid roll or reg number....";



}
void gread:: calculate_gpa()
{
    fstream file;
    int t_roll,t_reg;
    float math,english,science;
   cout<<"\n\tEnter roll number: ";
   cin>>t_roll;
   cout<<"\n\tEnter reg number: ";
   cin>>t_reg;
   cout<<"\n\tEnter math mark: ";
   cin>>math;
   cout<<"\n\tEnter english mark: ";
   cin>>english;
   cout<<"\n\tEnter science mark: ";
   cin>>science;
   float g=((math+english+science)/300) * 100;
   file.open("mark.txt",ios::app|ios::out);
   file<<" "<<t_roll<<" "<<t_reg<<" "<<math<<" "<<english<<" "<<science<<" "<<g<<endl;
   file.close();



}
class regsister: public gread {
    public:
    void menu();
    void all_chack();

};
void regsister::menu()
{
    int choice;
    while(true)
    {
    cout<<"\n\t1.Student Gread";
    cout<<"\n\t2.Calculate GPA";
    cout<<"\n\t3.Student record";
    cout<<"\n\t4.all chack";
    cout<<"\n\t5.Exit";
    cout<<"\n\tEnter your choice: ";
    cin>>choice;
    switch(choice)
    {
      case 1:
      grad();
      break;
      case 2:
      calculate_gpa();
      break;
      case 3:
      record();
      break;
      case 4:
      all_chack();
      break;
      case 5:
      exit(0);
      default :
      cout<<"\n\tYour choice is wrong....";
    }
    }

}
void regsister :: all_chack()
{
    fstream file;
    int r,rg;
    float m,e,s,g;
       cout<<"\n\t1.mark chack";
       cout<<"\n\t2.Student record";
       cout<<"\n\t3.exit";
       cout<<"\n\tEnter choice: ";
       int choice;
       cin>>choice;
       switch(choice)
       {
        case 1:
        file.open("mark.txt",ios::in);
        file>>r>>rg>>m>>e>>s>>g;
        while(!file.eof())
        {
            cout<<"roll :"<<r<<" reg: "<<reg<<" math :"<<m<<" english: "<<e<<" science: "<<s<<endl;
             file>>r>>rg>>m>>e>>s>>g;


        }
        file.close();
        break;
        case 2:
        file.open("Student record.txt ",ios::in);
        file>>name>>roll>>reg>>gpa>>adress;
        while(!file.eof())
        {
            cout<<"roll :"<<roll<<" reg: "<<reg<<" name :"<<name<<" gpa: "<<gpa<<" adress: "<<adress<<endl;
          file>>name>>roll>>reg>>gpa>>adress;


        }
        file.close();
        break;
        case 3:
        exit(0);

       }



}
int main()
{
   gread obj;

regsister obj2;
int x;


   cout<<"\n\t1.teacher";
   cout<<"\n\t2.register";
   cout<<"\n\t3.exit";
   cout<<"\n\tEnter your choice: ";
   cin>>x;
   switch(x)
   {
    case 1:
    obj.menu();
    break;
    case 2:
    obj2.menu();
    break;
    case 3:
    exit(0);
    default :
    cout<<"\n\tWrong....";
   }


}
