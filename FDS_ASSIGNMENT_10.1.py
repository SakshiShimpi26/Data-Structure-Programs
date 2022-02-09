"""Write a Python program to store roll numbers for students who attended training program
in sorted order. Write function for searching whether a particular student attended
training program or not,using binary search and Fibonacci search."""

def binary_Search(lst1,item):
  lower=0
  upper=len(lst1)-1
  mid1=(lower+upper)/2
  mid=int(mid1)
  while(lower<=upper):
    mid1=(lower+upper)/2
    mid=int(mid1)
    if (item == lst1[mid]):
        break
    elif item>lst1[mid]:
      lower=mid+1
    else:
      upper=mid-1
  
  if lst1[mid]==item:
    print()
    print("***************************************************************")
    print("###########By BINARY SEARCH####################################")
    print("Roll no ",item," has attended the Training")
    print("***************************************************************")
  else:
    print()
    print("***************************************************************")
    print("###########By BINARY SEARCH####################################")
    print("Roll no ",item," has not attended the Training")
    print("***************************************************************")

def Fibonacci_Search(lst1,item):
    Element2 = 0  
    Element1 = 1  
    Element = Element2+Element1 
    offset = -1
    n = len(lst1)
    while (Element < n):
	    Element2 = Element1
	    Element1 = Element
	    Element= Element2 + Element1
 
    while (Element > 1):
      i = min(offset+Element2, n-1)
      if (lst1[i] < item):
          Element = Element1
          Element1 = Element2
          Element2 = Element - Element1
          offset = i
      elif (lst1[i] > item):
          Element  = Element2
          Element1 = Element1 - Element2
          Element2 = Element - Element
      else:
         print()
         print("******************************************************************")
         print("###########By Fibonacci SEARCH####################################")
         print("Roll no ",item," has attended the Training")
         print("***************************************************************")
         break;
      print()
      print("******************************************************************")
      print("###########By Fibonacci SEARCH####################################")   
      print("Roll no ",item," has not attended the Training")
      print("******************************************************************")
      
while True:  
    print("$$$$$$$$$$$$MENU$$$$$$$$$$$$$")
    print("1.Binary Search")
    print("2.Fibonacci Search")
    print("3.Exit")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    choice=int(input("Enter your Choice"))
    if choice==1:
        n = int(input("Enter No of students whose roll nos. you want to store:"));
        lst1=[];
        for i in range(n):
          roll=eval(input("Enter Roll Numbers of Students in Ascending Order:"))
          lst1.append(roll);
        print(lst1)
        item=eval(input("Enter the Roll no You want to search:"))
        binary_Search(lst1,item)
    if choice==2:
        n = int(input("Enter No of students whose roll nos. you want to store:"));
        lst1=[];
        for i in range(n):
          roll=eval(input("Enter Roll Numbers of Students:"))
          lst1.append(roll);
        print(lst1)
        item=eval(input("Enter the Roll no You want to search:"))
        Fibonacci_Search(lst1,item)
    if choice==3:
        print("Thank You")
        break
