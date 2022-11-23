n=float(input("Enter the Number"))
n1=float(input("Enter the Number"))
choice=input("Enter the Choice")
if(choice=='+'):
    print("Sum is",n+n1)
elif(choice=='-'):
    print("subtraction is",n-n1)
elif(choice=='*'):
    print("multiplication is",n*n1)
elif(choice=='/'):
    print("division is",n/n1)
else:
    print("Invalid Choice")