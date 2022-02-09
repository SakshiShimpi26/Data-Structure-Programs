"""Write a Python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Merge Sort and display top five scores."""

def insertion_sort(lst1):
  n=len(lst1)-1
  newList=[]
  for k in range(1,len(lst1)):
    temp=lst1[k]
    j=k-1
    while(lst1[j]<temp and j>=0):
      lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
      j=j-1
    lst1[j+1]=temp
  print("Output of Insertion Sort:",lst1)

def merge_sort(lst1):
    if len(lst1) > 1:
        middleOfList = len(lst1) // 2
        leftList = lst1[:middleOfList]
        rightList = lst1[middleOfList:]
        merge_sort(leftList)
        merge_sort(rightList)
        i =0;j =0;k =0
        while i < len(leftList) and j < len(rightList):
            if leftList[i]<rightList[j]:
              lst1[k] = leftList[i]
              i=i+1
            else:
                lst1[k] = rightList[j]
                j=j+1
            k=k+1
        while i < len(leftList):
            lst1[k] = leftList[i]
            i=i+1
            k=k+1
        while j < len(rightList):
            lst1[k]=rightList[j]
            j=j+1
            k=k+1

n = int(input("Enter the Number of subject's mark you want to store:"))
lst1=[];
for i in range(n):
  roll=eval(input("Enter Second Year Marks:"))
  lst1.append(roll)
insertion_sort(lst1)
merge_sort(lst1)
print("Output of Merge Sort:",lst1)
n=len(lst1)-1
print("Top 5 Scores are:")
if n<=5:
    while n >=0:
        print(lst1[n]) 
        n=n-1
else:
    while n>=len(lst1)-5:
        print(lst1[n])
        n=n-1
