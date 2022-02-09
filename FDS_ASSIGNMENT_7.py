"""Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores of club."""

def Selection_Sort(lst1):
  length=len(lst1)
  for i in range(0,length):
    pos=i
    for j in range(i+1,length):
      if lst1[j]<lst1[pos]:
        pos=j
    lst1[i],lst1[pos]=lst1[pos],lst1[i]
  print("Selection Sort Output:",lst1)
  n=length-1
  print("Top 5 Scores are:")
  if n<=5:
    while n >=0:
      print(lst1[n]) 
      n=n-1
  else:
    while n>=length-5:
      print(lst1[n])
      n=n-1

def Bubble_Sort(lst1):
  length=len(lst1)
  for i in range(1,length):
    j=0
    while(j<length-i):
      if lst1[j]>lst1[j+1]:
        lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
      j=j+1
  print("Bubble Sort Output:",lst1)

n = int(input("Enter the Number of subject's mark you want to store:"));
lst1=[];
for i in range(n):
  roll=eval(input("Enter Second Year Marks:"))
  lst1.append(roll);
Bubble_Sort(lst1)
Selection_Sort(lst1)
