def main():
    contacts = {
        "Ravi": "9876543210",
        "Anita": "9123456780",
        "Tinku": "9826262662",
    }

    print("All contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

    search_name = input("Enter a name to search: ")

    if search_name in contacts:
        print(f"Phone number for {search_name}: {contacts[search_name]}")
    else:
        print("Contact not found")


if __name__ == "__main__":
    main()

