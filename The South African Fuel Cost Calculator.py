distance = float(input("How many kilometers do you want to drive?: "))
petrol_price = float(input("What is the current price for pretrol per litre?: "))

litres_needed = distance / 10
total_cost = litres_needed * petrol_price
rounded_final_cost = round(total_cost, 2)

print(f"Litres needed: {litres_needed}")
print(f"Total cost: {total_cost}")
print(f"Total cost: {rounded_final_cost} rounded")