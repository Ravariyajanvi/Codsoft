import os
import json
from typing import Dict, List

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
        self.load_contacts()

    def load_contacts(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.contacts = json.load(file)
        except Exception as e:
            print(f"Error loading contacts: {e}")

    def save_contacts(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
        except Exception as e:
            print(f"Error saving contacts: {e}")

    def add_contact(self, name: str, phone: str, email: str, address: str):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("\nContact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found!")
            return
        
        print("\n=== Contact List ===")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"\n{idx}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
            print("-" * 30)

    def search_contact(self, query: str) -> List[Dict]:
        query = query.lower()
        results = []
        for contact in self.contacts:
            if (query in contact['name'].lower() or 
                query in contact['phone']):
                results.append(contact)
        return results

    def update_contact(self, index: int, name: str, phone: str, email: str, address: str):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.save_contacts()
            print("\nContact updated successfully!")
        else:
            print("\nInvalid contact index!")

    def delete_contact(self, index: int):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            self.save_contacts()
            print(f"\nContact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("\nInvalid contact index!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    contact_book = ContactBook()
    
    while True:
        clear_screen()
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            name = input("\nEnter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("\nEnter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("\nSearch Results:")
                for contact in results:
                    print(f"\nName: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print(f"Address: {contact['address']}")
                    print("-" * 30)
            else:
                print("\nNo matching contacts found!")

        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("\nEnter the number of contact to update: ")) - 1
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_book.update_contact(index, name, phone, email, address)
            except ValueError:
                print("\nPlease enter a valid number!")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("\nEnter the number of contact to delete: ")) - 1
                contact_book.delete_contact(index)
            except ValueError:
                print("\nPlease enter a valid number!")

        elif choice == '6':
            print("\nThank you for using Contact Book!")
            break

        else:
            print("\nInvalid choice! Please try again.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()