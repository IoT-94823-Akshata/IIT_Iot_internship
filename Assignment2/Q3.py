Number = int(input("Enter the number: "))
if (Number == 1):
    print("The number is neither prime or composite number")
    exit()
if (Number == 2):
    print("The number is prime number")
else :
    div = 2
    prime = True
    while (div < Number):
       if( Number%div == 0):
          prime = False
          break
       div+=1

    if(prime):
        print("The number is prime")

    else:
        print("The number is composite")