"""Write a Python program to store roll numbers for students who attended training program
in random order. Write function for searching whether a particular student attended
training program or not,using linear search and sentinel search."""

def Linear_Search(lst1,item):
  loc=0
  while(loc<n and lst1[loc]!=item):
    loc=loc+1
  
  if loc==n:
    print("******************************************************************")
    print("###########By Linear SEARCH####################################")
    print("Roll no ",item," has not attended the Training")
    print("******************************************************************")
  else:
    print("******************************************************************")
    print("###########By Linear SEARCH####################################")
    print("Roll no ",item," has attended the Training")
    print("******************************************************************")

def Sentinel_Search(lst1, item):
    size = len(lst1)
    lst1.append(item)
    count= 0
    while(lst1[count] != item):
        count=count+1
    if(count== size):
         print()
         print("******************************************************************")
         print("###########By Sentinel SEARCH####################################")
         print("Roll no ",item," has not attended the Training")
         print("******************************************************************")
    else:
         print("******************************************************************")
         print("###########By Sentinel SEARCH####################################")
         print("Roll no ",item," has attended the Training")
         print("******************************************************************")

while True:
    n = int(input("Enter No of students whose roll nos. you want to store:"));
    lst1=[];
    for i in range(n):
      roll=eval(input("Enter Roll Numbers of Students:"))
      lst1.append(roll);
    print(lst1)
    item=eval(input("Enter the Roll no You want to search:"))

    print("$$$$$$$$MENU$$$$$$$$$$")
    print("1.Linear Search")
    print("2.Sentinel Search")
    print("3.Exit")
    print("Enter Your Choice")
    print("$$$$$$$$$$$$$$$$$$$$$$")
    choice=int(input())

    if choice==1:
        Linear_Search(lst1,item)
    elif choice==2:
        Sentinel_Search(lst1,item)
    else:
        print("Thank You!!!!")
        break
