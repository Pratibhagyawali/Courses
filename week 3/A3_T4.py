
print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

user_name=input("Before the menu, please insert your name: ")

print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
name_backwards=user_name[::-1]
name_length =len(user_name)
first_char=user_name[0]
menu_choice=int(input("Your choice: "))
if menu_choice==1:
 print(f"Welcome {user_name}! \n")
elif menu_choice==2:
 print(f'Your name backwards is "{name_backwards}"')
elif menu_choice==3:
 print(f"The first character in name \"{user_name}\" is \"{name_length}\" \n")
elif menu_choice==4:
 print(f"There are {first_char} characters in the name \"{user_name}\"")
 print(f" \"{user_name}\" \n")
elif menu_choice==0:
 print(f"Exiting ...\n")
else:
 print("Unknown option. \n")
print("Program ending.")
