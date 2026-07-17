# Arithmetic Operators:
# Addition:       +
# Subtraction:    -
# Multiplication: *
# Division:       /
# Floor Division: //  It drops the remainder/decimal
# Exponent:       **
# Modulus:        %   Gives the remainder and also checks if a number is even
# absolute value:  removes the negative sign: abs(-7) gives 7



# Calculating the tip

bill = float(input("Enter the bill: $"))
tip = 0.15  # written in decimal form

val_tip = bill * tip
total_cost = bill + val_tip 

print(f"Here is the tip: {val_tip}")
print(f"Here is the tip: {round(val_tip,2)} rounded")

print(f"Here is the total cost: {total_cost}")
print(f"Here is the total cost: $ {round(total_cost,2)} rounded")
