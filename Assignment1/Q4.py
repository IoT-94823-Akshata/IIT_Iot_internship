Number1 = float(input("Enter the value of first number : "))
Number2 = float(input("Enter the value of second number : "))

print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division ")

ch = int(input("\nEnter your choice: "))
match ch:
    case 1 :print(f"The sum of the two number is {Number1 + Number2}")

    case 2 :print(f"The Subtraction of the two number is {Number1 - Number2}")

    case 3 :print(f"The Multiplication of the two number is {Number1 * Number2}")

    case 4 :print(f"The Division of the two number is {Number1 / Number2}")

    case _ :print(f"Enter the valid option")
    