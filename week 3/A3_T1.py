print("Program starting.")
print("Insert two integers.")
first = int(input("Insert first integer: "))
second = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if first == second:
    print("Integers are the same")
else:
    if first > second:
        print("First integer is greater.")
    else:
        print("Second integer is greater.")
print("\nAdding integers together")
sum = first + second
print(f"{first} + {second} = {sum}")
print("\nChecking the parity of the sum...")
Remainder = sum % 2
if (Remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")