import json
import os

# This is the path to the contacts.txt file in the same directory as this script
script_directory = os.path.dirname(os.path.abspath(__file__))
contacts_file_path = os.path.join(script_directory, 'contacts.txt')

contacts = []

# This function will save the contacts list to the contacts.txt file
def save_contacts():
    with open(contacts_file_path, 'w') as file: # Open the file in write mode
        json.dump(contacts, file)

# This function will load the contacts list from the contacts.txt file
def load_contacts():
    try:
        with open(contacts_file_path, 'r') as file: # Open the file in read mode
            content = file.read() # Read the file content
            print("File content:", content)  # Add this line for debugging
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return []

# This is the main function that will be executed when the script is run
def main():
    global contacts # This will allow us to access the contacts list from inside the main function
    contacts = load_contacts() # Load the contacts list from the contacts.txt file

    while True:
        print('Contact Book')
        print('1. View Contact')
        print('2. Add Contact')
        print('3. Edit Contact')
        print('4. Delete Contact')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            view_contact()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            save_contacts()
            print('Thank you for using Contact Book')
            break
        else:
            print('Invalid Choice! Please select a valid choice.')

# This function will print all the contacts in the contacts list
def view_contact():
    for index, contact in enumerate(contacts):
        print(f"Index: {index}, Contact: {contact}")

# This function will add a new contact to the contacts list
def add_contact():
    contact = {
        'name': input('Enter name: '),
        'phone': input('Enter phone: '),
        'email': input('Enter email: ')
    }

    contacts.append(contact) # Add the new contact to the contacts list
    print('Contact added successfully!')

# This function will edit an existing contact in the contacts list
def edit_contact():
    view_contact()
    index = int(input("Enter the index of the contact you want to edit: ")) # Ask the user to enter the index of the contact they want to edit
    if 0 <= index < len(contacts): # Check if the index is valid
        field = input('Enter the field you want to edit (name/phone/email): ')
        new_value = input('Enter the new value: ')
        contacts[index][field] = new_value # Update the contact with the new value
        print('Contact edited successfully!')
    else:
        print('Invalid index!')

# This function will delete an existing contact from the contacts list
def delete_contact():
    view_contact()
    index = int(input("Enter the index of the contact you want to delete: "))
    if 0 <= index < len(contacts):
        del contacts[index]
        print('Contact deleted successfully!')
    else:
        print('Invalid index!')

if __name__ == '__main__':
    main()
