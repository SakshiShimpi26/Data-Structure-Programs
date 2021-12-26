def average_Calculate(lst):
  total=0
  for i in range (len(lst)):        
    total= total+lst[i]
  print("Average score of class is :",total/n)

def highest_lowest_score(lst):
  high=0
  for i in range(len(lst)):
    if lst[i]>high:
      high=lst[i]
  print("Highest score of class is:",high)

  minn=high
  for i in range(len(lst)):
    if lst[i]<minn and lst[i]!=-1:
      minn=lst[i]
  print("Lowest score of class is:",minn)

def absent_students(lst):
  count=0;
  for i in range(len(lst)):
    if lst[i]==-1:
      count=count+1;
  print("No of students absent for test are:",count)

def no_of_highest_marks(lst):
  hcount=0;
  for i in range(len(lst)):
    if lst[i]==30:
      hcount=hcount+1;
  print("No of students having the highest marks are:",hcount)

n = int(input("Enter No of students whose marks you want to store:"));
lst1=[];
for i in range(n):
  marks=eval(input("Enter Marks of Student for 'Fundamental of Data Sructures':"))
  lst1.append(marks);

average_Calculate(lst1)
highest_lowest_score(lst1)
no_of_highest_marks(lst1)
absent_students(lst1)
