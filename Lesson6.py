#List | a list is and ordered collection of items held in a square bracket.

#Working list (Shopping cart)

# cart = ["Apple", "Eggs", "Milk"]
# print(cart[0])

# cart.append("Bread")
# print(cart)

# for item in cart:
#     print(item)


#Working with dictionaries

# student = {
#     "name": "Thabo",
#     "age": "25",
#     "course": "Intro to Python"
# }


# print(student["name"])
# print(student["age"])


#GRADE CLASSIFIER

full_name = input("Enter name: ")
grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

total_grades = grade1 + grade2 + grade3
average = total_grades / 3
print(f"Average: {round(average, 2)}")

if average > 80:
    print("A")
    final_grade = "A"
elif average >= 70:
    print("B")
    final_grade = "B"
elif average >= 60:
    print("C")
    final_grade = "C"
elif average >= 50:
    print("D")
    final_grade = "D"
elif average <50:
    print("F")
    final_grade = "F"

if average >= 50:
    print("PASS")
    status = "PASS"
else:
    print("FAIL")
    status = "FAIL"


if grade1 < 40:
    print(f"Needs intervention! Mark: {grade1}")
    Intervention = "Needs intervention! Mark: {grade1}"
if grade2 < 40:
    print(f"Needs intervention! Mark: {grade2}")
    Intervention = "Needs intervention! Mark: {grade2}"
if grade3 < 40:
    print(f"Needs intervention! Mark: {grade3}")
    Intervention = "Needs intervention! Mark: {grade3}"




print("REPORT CARD")
print(f"Ful Name: {full_name}")
print(f"First Grade: {grade1}")
print(f"Second Grade: {grade2}")
print(f"Third Grade: {grade3}")
print(f"Average: {round(average, 2)}")
#print(f"Grade: {final_grade}")
print(f"Status: {status}")
#print(f"Needs intervention: {Intervention}")
