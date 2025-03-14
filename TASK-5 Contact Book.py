class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name : {self.name}, Phone : {self.phone}, Email : {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contacts(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No Contacts available.")
        else:
            for contact in self.contacts:
                print(contact)
    
    def search_contact(self, query):
        found = False
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")
    
    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = input("Enter new phone : ")
                contact.email = input("Enter new email : ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")
    
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option : ")

        if choice == "1":
            name = input("Enter Name : ")
            phone = input("Enter Phone Number : ")
            email = input("Enter Email : ")
            contact = Contact(name, phone, email)
            contact_book.add_contacts(contact)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search : ")
            contact_book.search_contact(query)

        elif choice == "4":
            name = input("Enter name to update : ")
            contact_book.update_contact(name)

        elif choice == "5":
            name = input("Enter name to delete : ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Book...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
