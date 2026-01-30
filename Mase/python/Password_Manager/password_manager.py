master_pwd = input("Please enter your master password: ")

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Account Password: ")
    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")
    pass



while True:
    choice = input("Would you like to add a new password or view existing ones (add, view) or 'q' to quit: ")

    if choice == 'q' or choice == 'quit':
        print("Goodbye")
        break

    elif choice == 'view':
        view()
        pass
    elif choice == 'add':
        add()
        pass
    else:
        print("Invalid option")
        print("Please enter again")
        continue