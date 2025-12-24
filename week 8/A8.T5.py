from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            username = askValue("username")
            password = askValue("password")
            if login(username, password):
                print("Login successful!")
                userMenu(username)
            else:
                print("Login failed.")
        elif choice == 2:
            username = askValue("username")
            password = askValue("password")
            register(username, password)
            print("User-registration: completed!")
        elif choice == 0:
            print("Exiting: program.")
            break
        else:
            print("Invalid choice.")

def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()

        if choice == 1:
            profile = viewProfile(PUsername)
            print(profile)
        elif choice == 2:
            new_pw = askValue("new password")
            change_password(PUsername, new_pw)
            print("Password changed.")
        elif choice == 0:
            print("Logout successful.")
            break
        else:
            print("Invalid choice.")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def askValue(prompt: str) -> str:
    return input(f"Insert {prompt}: ")

if __name__ == "__main__":
    main()