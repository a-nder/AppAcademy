contacts = {
    "Lenny": "0774543965",
    "Trent": "0771231764",
    "Alex": "0778421752"
}

search_name = input("Enter name: ")

if search_name in contacts:
    number = contacts[search_name]
    print(f"Found! {search_name}'s number is {number}")
else:
    print("Contact not found.")