# first = input("First name: ")
# last = input("Last name: ")
# bio = input("Bio message: ").strip()
# # length_of_bio = len(bio)
# username = f"{first[0]}{last.lower()}".lower()

# print(f"Full name: {first.title()} {last.title()}")
# print(username)
# print(f"Bio: {bio}")
# bio = bio.replace("I am", "I'm")
# print(f"Formatted bio: {bio}")
# print(f"Character count: {len(bio)}")

first = input("First name: ")
last = input("Last name: ")
bio_message = input("Enter bio: ")

username = first.lower()[0] + last.lower()

print(f"{first.title()}" +" "+ f"{last.title()}")
print("Username:" + username)
bio = bio_message.strip()
bio_len = len(bio)
bio.replace("I am", "I'm")
print(bio)
print(f"Bio Character Count: {bio_len}")

