Cal = "Welcome to the simple calculator"
print(Cal, "\n")

a = float(input("enter your first number : "))
b= float(input("enter your second number : "))

operator = input("Choose your operation(+, -, /, *) : ")

if(operator == "+"):
    print("\nRESULT\n", a+b, "\n")
elif(operator == "-"):
    print("\nRESULT\n", a-b, "\n")
elif(operator == "/"):
    if b == 0 :
         print("\nCannot divide by 0!!!\n")
    else :
        print("\nRESULT\n", a/b, "\n")
else:
	print("\nRESULT\n", a*b, "\n")
     