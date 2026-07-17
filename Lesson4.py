#Basic if/else statement

# age = int(input("Enter your age: "))
# section_pass = input("Do you have a vip ticket (yes or no): ").lower()

# if age >= 18 and section_pass == "yes":
#     print("You have access to VIP setion")
# elif age >= 18:
#     print("You have access to the general section")
# else:
#     print("Access denied !!!")



#Lists | Mutable

# students = ["John", "Mary", "Peter", "Jane"]
# students[2]
# students[-1]
# students.append("Mike")
# students.insert(2, "Lucy")
# students.remove("Mike")
# students.pop(2)
# print(len(students))
# print(students)



#Dictionaries | Stores key-value pairs | a lookup table where every piece of data has a name

contact = {"name": "Amara", "phone": "071 234 5678"}
print(contact["name"])
print(contact.get("Address"))  # get() method returns None if the key does not exist instead of throwing an error
print(contact.keys())
print(contact.values())
print(contact.items())