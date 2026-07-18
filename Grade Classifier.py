# full_name = input("Enter full name: ")
# grade1 = float(input("What are your marks for your first subject?: "))
# grade2 = float(input("What are your marks for your second subject?: "))
# grade3 = float(input("What are your marks for your third subject?: "))


# Total_grade = grade1 + grade2 + grade3
# average = Total_grade / 3



# # if grade1 and grade2 and grade3 >= 80:
# #     print("A")
# # elif grade1 and grade2 and grade3 >= 70-79:
# #     print("B")
# # elif grade1 and grade2 and grade3 >= 60-69:
# #     print("C")
# # elif grade1 and grade2 and grade3 >= 50-59:
# #     print("D")
# # else:
# #     print("F")
    
# # A >= 80
# # B >= 70-79
# # C >= 60-69
# # D >= 50-59
# # F >= 0-49

# if grade1 < 40:
#     print(f"Needs Intervention for grade: {grade1}")
# if grade2 < 40:
#     print(f"Needs Intervention for grade: {grade2}")
# if grade3 < 40:
#     print(f"Needs Intervention for grade: {grade3}")


# if average >= 80:
#     print("PASS")
# elif average >= 70: 
#     print("PASS")
# elif average >= 60:
#     print("PASS")
# elif average >= 50:
#     print("PASS")
# else:
#     print("FAIL")


# if average >= 50:
#     status = "PASS"
# else:
#     status = "FAIL"


# print("REPORT CARD")
# print(f"Fullname: {full_name}")
# print(f"Grade: {grade1}")
# print(f"Grade: {grade2}")
# print(f"Grade: {grade3}")
# print(f"Average: {average}")
# print(f"Grade Symbol: {letter_grade}")
# print(f"Status: {status}")



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
print(f"Grade: {final_grade}")
print(f"Status: {status}")
print(f"Needs intervention: {Intervention}")
