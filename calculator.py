num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))


print(f"Addition: {round(num1 + num2,2)}")
print(f"Subtraction: {round(num1 - num2, 2)}")
print(f"Multiplication: {round(num1 * num2, 2)}")
if num2 == 0:
    print("Error! Number cannot be 0.")
else:
    print(f"Division: {round(num1 / num2, 2)}")
    print(f"Floor division: {round(num1 // num2, 2)}")
    print(f"Modulus: {round(num1 % num2, 2)}")


