print("Program starting.")
print("Insert two integers.")
first_int = int(input("Insert first integer: "))
second_int = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if first_int == second_int:
    print("Integers are the same.")
elif first_int > second_int:
    print("First integer is greater.")
else:
    print("Second integer is greater.")
    print("\nAdding integers together")
sum_int = first_int + second_int
print(f"{first_int} + {second_int} = {sum_int}")
print("\nChecking the parity of the sum...")
if sum_int % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")