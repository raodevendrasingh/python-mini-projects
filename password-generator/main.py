m_pass = input("Enter the master password: ")


def view():
    with open("passwords.txt", 'r') as fp:
        for line in fp.readlines():
            data = line.rstrip()
            u_name, u_pass = data.split("|")
            print("user: ", u_name,  "| pass: ", u_pass)


def add():
    u_name = input("Username: ")
    u_pass = input("Password: ")

    with open("passwords.txt", 'a') as fp:
        fp.write(u_name + " | " + u_pass + "\n")


while True:
    mode = input("Do you want to add or view passwords? [add/view/Q]: ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode!")
        continue
