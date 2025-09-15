def show_option():
    print("\n contact Menu")
    print("a. Add contact")
    print("d. Delete contact")
    print("v. view contact")
    print("q. Quit")

def show_contacts(contacts):
    print("Sn.\tName\t\tphone")
    i = 1
    for contact in contacts:
        (name,phone) = contact
        print (f"{i}.\t{name}\t\t{phone}")
        i += 1

def add_contact(contacts):
    phone = input("Enter your phone number: ")
    name = input("Enter your name: ")
    contact =(name,phone)
    contacts.append(contact)

    return contacts
def delete_contact(contacts):
    index = int(input("Enter the index of the contact to delete:  "))
    del contacts[index -1]
    return contacts

def main(contacts = [("Strish" , "123"),("Rita" , "321")]):
    while True:
        show_option()
        option = input("Enter choice(v/a/d/q- to quit): ")

        if option =="v":
         print("\n----------------view contact----------")
         print("\nviewing contact:  ")
         show_contacts(contacts)

        if option == "a":
            print("\n-------------Add contact-----------")
            contacts = add_contact(contacts)
            print("contact saved!..")
        if option == "d":
            print("\n-------------delete contact-----------")
            contacts = delete_contact(contacts)

        if option =="q":
            break

        input("\nPress Enter key.....")
    print("---------GoodBye---------")

main()