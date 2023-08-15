import json
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
contacts_file_path = os.path.join(script_directory, 'contacts.txt')

contacts = []

def save_contacts():
    with open(contacts_file_path, 'w') as file:
        json.dump(contacts, file)

def load_contacts():
    try:
        with open(contacts_file_path, 'r') as file:
            content = file.read()
            print("File content:", content)  # Add this line for debugging
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return []
    
def main():
    global contacts
    contacts = load_contacts()

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

def view_contact():
    for index, contact in enumerate(contacts):
        print(f"Index: {index}, Contact: {contact}")

def add_contact():
    contact = {
        'name': input('Enter name: '),
        'phone': input('Enter phone: '),
        'email': input('Enter email: ')
    }

    contacts.append(contact)
    print('Contact added successfully!')

def edit_contact():
    view_contact()
    index = int(input("Enter the index of the contact you want to edit: "))
    if 0 <= index < len(contacts):
        field = input('Enter the field you want to edit (name/phone/email): ')
        new_value = input('Enter the new value: ')
        contacts[index][field] = new_value
        print('Contact edited successfully!')
    else:
        print('Invalid index!')

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
