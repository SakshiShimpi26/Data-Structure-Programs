"""Write the python program that computes the net amount of a bank account based
transaction log from console input. The transaction log format is shown as
D 100 W 200(withdraw is not allowed is balance is going to be negative, write
functions for withdraw and deposite)D means deposite and W means withdraw."""

netAmount=0

def deposit(value1):
  global netAmount
  netAmount=netAmount+value1
  print("Deposite Successfull")

def withdraw(value2):
  global netAmount
  if(netAmount-value2<0):
    print("Error: Withdraw can't be done. Not sufficient balance")
  else:
    netAmount=netAmount-value2
    print("Withdraw Successfull")

lst=[]
amount=0
while True:
  print("$$$$$$$MENU$$$$$$$")
  print("1.Transaction")
  print("2.Check Balance")
  print("3.Exit")
  print("Enter a choice")
  choice=int(input())

  if choice==1:
    string1 = (input("Enter the Transaction:"))
    lst=string1.split(" ")
    if(lst[0]=="D" or lst[0]=="d"):
      amount=int(lst[1])
      deposit(amount)
    elif(lst[0]=="W" or lst[0]=="w"):
      amount=int(lst[1])
      withdraw(amount)
    else:
      pass
  elif choice==2:
    print("Balance is :",netAmount)
  elif choice==3:
    print("Thank You!!!!!")
    break
  else:
    pass
