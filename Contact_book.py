contacts = [
    {"name": "Randy", "phone": "0774876234", "email": "randy@mail.com"},
    {"name": "Lisa", "phone": "0772987453", "email": "lisa@mail.com"},
    {"name": "Rob", "phone": "0774543765", "email": "rob@mail.com"},
    {"name": "Alex", "phone": "0777867234", "email": "alex@mail.com"}
    
    ]

def add_contacts(name,phone,email):
    contacts.append({"name": name, "phone": phone, "email": email})

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            return
    print("Contact not found")

def view_contact():
    if not contacts:
        print("No contacts saved.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


while True:
    print("\n1. Add 2. Search 3. Delete 4. View 5. Exit")
    choice = input("Choose an action: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contacts(name,phone,email)
    elif choice == "2":
        name = input("Name to search: ")
        result = search_contact(name)
        print(result if result else "Not found")
    elif choice == "3":
        name = input("Name to delete: ")
        delete_contact(name)
    elif choice == "4":
        view_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else: 
        print("Invalid choice try again.")


