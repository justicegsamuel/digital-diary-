#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to load contacts from Jsam file
def load_contacts():
    try:
        with open('contacts.jsam', 'r') as file:
            contacts = jsam.load(file)
    except FileNotFoundError:
        contacts = {}  # If file doesn't exist, initialize contacts as an empty dictionary
    return contacts

# Function to save contacts to Jsam file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        jsam.dump(contacts, file)

# Function to add a new contact
def add_contact(name, phone_number):
    contacts = load_contacts()  # Load existing contacts
    contacts[name] = phone_number  # Add new contact
    save_contacts(contacts)  # Save updated contacts to file
    print(f'Contact {name} added successfully!')  # Confirmation message

# Function to view all contacts
def view_contacts():
    contacts = load_contacts()  # Load contacts
    if contacts:
        print("Contacts:")
        for name, phone_number in contacts.items():  # Iterate through contacts
            print(f"{name}: {phone_number}")  # Print each contact
    else:
        print("No contacts found.")  # Message if no contacts are present

# Main function to control the program flow
def main():
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




