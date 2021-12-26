#include<iostream>
#define M 10
using namespace std;
typedef struct node
{
      char name[M];
      int prn;
      char type;
      struct node *next;
}NODE;

class Pinnacle
{
      NODE *head,*last;
      public:
          Pinnacle()
          {
                head=NULL;
          }
          void create()
          {
                NODE *t;
                t=new NODE;
                t->next=NULL;
                cout<<"\Enter Name :";
                cin>>t->name;
                cout<<"\nEnter PRN No  :";
                cin>>t->prn;
                cout<<"\Enter TYPE :";
                cin>>t->type;
                if(head==NULL)
                {
                      head=t;
                      last=t;
                }

                else
                {
                      if(t->type=='p')
                      {
                            t->next=head;
                            head=t;
                            cout<<"You are a President";
                      }
                       else if(t->type=='s')
                      {
                            last->next=t;
                            last=t;
                            cout<<"You are a Secretary";
                      }
                      else
                      {
                            if(head==last)
                            {
                                  head->next=t;
                                  last=t;
                            }
                            else
                            {
                                  t->next=head->next;
                                  head->next=t;
                                  cout<<"Member entry created successfully";

                            }
                      }

                }

      }

      void display()
      {
            NODE *t1;
            t1=head;
            while(t1!=NULL)
            {
                  if(t1->type=='p')
                  {
                    cout<<"\n##################PRESIDENT##################";
                    cout<<"\nname ;"<<t1->name;
                    cout<<"\nprn :"<< t1->prn;
                  }

                  if(t1->type=='s')
                  {
                    cout<<"\n##################SCERATARY##################";
                    cout<<"\nname ;"<<t1->name;
                    cout<<"\nprn :"<< t1->prn;
                  }
                  t1=t1->next;
            }
            t1=head;
            while(t1!=NULL)
            {
                  if(t1->type=='m')
                  {
                    cout<<"\n---------------------------member";
                    cout<<"\nname ;"<<t1->name;
                    cout<<"\nprn :"<< t1->prn;
                  }
                  t1=t1->next;
            }
      }

      void Change_President()
      {
            head->type='m';
            NODE *t;
            t=new NODE;
            t->type='p';
            t->next=NULL;

            cout<<"\nEnter Name :-";
            cin>>t->name;
            cout<<"\nEnter PRN no :";
            cin>>t->prn;
            t->next=head;
            head=t;

      }

      void Change_Sceratary()
      {
            last->type='m';
            NODE *t;
            t=new NODE;
            t->type='s';
            t->next=NULL;
            cout<<"\nEnter Name :-";
            cin>>t->name;
            cout<<"\nEnter PRN no :";
            cin>>t->prn;
            last->next=t;
            last=t;

      }

      void Delete_President()
      {
            NODE *t;
            t=head;
            head=head->next;
            head->type='p';
            delete t;
            cout<<"President Entry Deleted Successfully:";
      }

      void Delete_Sceratary()
      {
            NODE *t,*t1;
            t=head;
            while(t->next!=last)
            {
                  t=t->next;
            }
            t1=t->next;
            last=t;
            last->type='s';
            last->next=NULL;
            delete t1;
            cout<<"Scretary Entry Deleted Successfully";
      }

      void Delete_Member()
      {
            NODE *t1,*t2;
            int t;
            cout<<"Enter PRN :";
            cin>>t;
            t1=head->next;
            t2=head;
            while(t1!=NULL)
            {
                  if(t==t1->prn)
                  {
                        t2->next=t1->next;
                        delete t1;
                        cout<<"Member Deleted";
                        break;
                  }
                  t1=t1->next;
                  t2=t2->next;
            }
            if(t2==last)
            {
                cout<< "Member not found";
            }
      }

      void concat(Pinnacle p)
      {
            last->type='m';
            last->next=p.head;
            p.head->type='m';
            last=p.last;
      }
};

int main()
{
      int choice;
      Pinnacle p1,p2;
      while(choice!=9)
      {
        cout<<"\n*************MENU****************";
        cout<<"\n1.ADD MEMBER";
        cout<<"\n2.DISPLAY MEMBER";
        cout<<"\n3.CHANGE PRESIDENT";
        cout<<"\n4.CHANGE SECERATARY ";
        cout<<"\n5.DELETE PRESIDENT";
        cout<<"\n6.DELETE SCERSTARY";
        cout<<"\n7.DELETE MEMBER";
        cout<<"\n8.CONCATINATION OF LISTS ";
        cout<<"\n9.EXIT";
        cout<<"\n********************************";
        cout<<"\neENTER YOUR CHOICE? :";
        cin>>choice;
                    switch(choice)
                    {
                    case 1:p1.create();break;
                    case 2:p1.display();break;
                    case 3:p1.Change_President();break;
                    case 4:p1.Change_Sceratary();break;
                    case 5:p1.Delete_President();break;
                    case 6:p1.Delete_Sceratary();break;
                    case 7:p1.Delete_Member();break;
                    case 8:
                          int i=0;
                          while(i<6)
                          {
                                p2.create();
                                i++;
                          }
                          p1.concat(p2);
                          break;
            }
      }
}

