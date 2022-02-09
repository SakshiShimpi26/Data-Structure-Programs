"""Write a Python program to store first year percentage of students in array.
Write function for sorting array of floating point numbers in ascending
order using quick sort and display top five scores."""


def divide(lst1, first, high):
    pivot = lst1[first]
    low = first + 1

    while True:
        while low <= high and lst1[high] >= pivot:
            high = high - 1
        while low <= high and lst1[low] <= pivot:
            low = low + 1
        if low <= high:
            lst1[low], lst1[high] = lst1[high], lst1[low]
        else:
            break
    lst1[first], lst1[high] = lst1[high], lst1[first]
    return high

def quick_sort(lst1, first, high):
    if first >= high:
        return
    p = divide(lst1, first, high)
    quick_sort(lst1, first, p-1)
    quick_sort(lst1, p+1, high)

n = int(input("Enter the Number of subject's mark you want to store:"))
lst1=[];
for i in range(n):
  roll=eval(input("Enter Second Year Marks:"))
  lst1.append(roll)
quick_sort(lst1, 0, len(lst1) - 1)
print("Output of Quick Sort:",lst1)

n=len(lst1)-1
print("Top 5 Scores are:")
if n<=5:
    while n >=0:
        print(lst1[n]) 
        n=n-1
else:
    while n>=len(lst1)-4:
        print(lst1[n])
        n=n-1

  

