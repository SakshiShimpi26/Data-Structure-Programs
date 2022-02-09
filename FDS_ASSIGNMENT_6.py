"""Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string"""

string = input("Enter a String:  ")
split=string.split(" ")

n=0
for i in range(len(split)):
  if (len(split[i])>n):
    n=len(split[i])
    word=split[i]
print("********************************************************************")
print("Word with Longest Length:",word)
print("********************************************************************")

count=0
char=input("\nEnter a Character whose frequency You want to check:  ")
for i in range(len(string)):
  if string[i]==char:
    count=count+1
print("Character ",char," occurs ",count," times in ",string)
print("********************************************************************")

reverse=""
for i in string:
  reverse=i+reverse
if string==reverse:
  print("\nString is Pallindrome")
  print("********************************************************************")
else:
  print("\nString is Not Pallindrome")
  print("********************************************************************")

print("Index of First Substring are:")
for i in range(len(split[0])):
  if split[i]=="":
    break
  else:
      print(i)
print("********************************************************************")

frequency = dict()
words = string.split()
for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1
print("Frequency of Each word is as follows:")
for i in frequency :
   print(frequency[i]," : ",i)
print("********************************************************************")
