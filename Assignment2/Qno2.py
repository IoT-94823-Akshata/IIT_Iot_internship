Number = int(input("Enter five digits number :"))

if(Number <0 or Number > 99999):
    print(" Enter valid number ")
    exit()

temp = Number
rev = 0

while(Number > 0):
    dig = Number %10
    rev = rev *10+dig
    Number = Number//10
if(temp == rev):
        print("The number is palindrome")
else:
        print ("The number is not palindrome")




