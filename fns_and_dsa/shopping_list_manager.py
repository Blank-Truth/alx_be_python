shopping_list = []

def display_menu():
    while True:
        choice = input("Enter your choice(i.e 1-4): ")
        if choice == "1":
            item = input("Enter item you want to add").strip()
            shopping_list.append(item)
            print(shopping_list)
        elif choice == "2":
            item = input("Enter item you want to remove").strip()
            shopping_list.remove(item)
            print(shopping_list)
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")

result = display_menu()
print(result)