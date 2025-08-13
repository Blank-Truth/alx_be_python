def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice(i.e 1-4): ").strip()
        if choice == '1':
            item = input("Enter item you want to add").strip()
            shopping_list.append(item)
            print(shopping_list)
        elif choice == '2':
            item = input("Enter item you want to remove").strip()
            shopping_list.remove(item)
            print(shopping_list)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")

result = main()
print(result)