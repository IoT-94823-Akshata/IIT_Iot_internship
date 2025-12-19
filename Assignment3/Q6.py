def add(n1 , n2):
    return n1 + n2
def sub(n1 , n2):
    return n1 - n2
def div(n1 , n2):
    return n1 / n2
def mul(n1 , n2):
    return n1 * n2

print(""" 1. Addition\n
          2 .Sub\n
          3.Mul\n
          4.Div\n""")

ch = int(input(f"choose the option : "))

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))

if(ch==1):
    print(n1 ,"+",n2,"=",add(n1 , n2))
elif(ch==2):
    print(n1,"-",n2,"=", sub(n1,n2))
elif(ch==3):
    print(n1,"/",n2,"=",div(n1,n2))
elif(ch==4):
    print(n1,"*",n2,"=", mul(n1,n2))
else:
    print("Enter valid option")