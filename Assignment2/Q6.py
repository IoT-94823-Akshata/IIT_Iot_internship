print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch = int(input("\nEnter your choice : "))

Number1 = float(input("Enter value of Number1 :"))
Number2 = float(input("Enetr value of Number2 :"))
match ch:
    case 1 : print(f"The Addition of two numbers is : {Number1 + Number2}")

    case 2 : print(f"The subtraction of two numbers is : {Number1 - Number2}")

    case 3 : print(f"The Multiplication of two numbers is : {Number1 * Number2}")

    case 4 : print(f"The Division of two numbers is : {Number1 - Number2}")

    case _ : print("Enter valid option")