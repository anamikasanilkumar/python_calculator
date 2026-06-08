def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a/b
while True:
 print("-----CALCULATOR-----")
 print("--show menu-- ")
 print("1.Add")
 print("2.Subtract")
 print("3.Multiply")
 print("4.divide")
 print("5.Exit")
 choice=int(input("Enter your choice:"))
 if choice==5:
    break
 number1=float(input("enter first number:"))
 number2=float(input("enter the second number:"))

 if choice==1:
    print("Answer:",add(number1,number2))
 elif choice==2:
    print("Answer:",subtract(number1,number2))
 elif choice==3:
    print("Answer:",multiply(number1,number2))
 elif choice==4:
    if number2==0:
       print("cannot by divide by zero")
    else:
     print("Answer:",divide(number1,number2))
 else:
    print("Invalid choice")



