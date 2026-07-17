f_name = input("First name: ")
l_name = input("last name: ")
full_name = (f_name +" " + l_name)
age_y = int(input("Age: "))
age_m = age_y*12
fav_number = float(input("Favourite number:"))
fav_number = round(fav_number, 2)

print(f"Welcome {full_name}!")
print(full_name.upper())
print(full_name.title())
print(f"Your age in months is {age_m} months")

print(fav_number)
print(type(f_name))
print(type(l_name))
print(type(age_y))
print(type(fav_number))

