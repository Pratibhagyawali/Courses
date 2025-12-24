print("Program starting.\n")
print("Check multiplicative persistence.")
user_number = input("Insert an integer: ")

steps = 0

while len(user_number) > 1:
    digits_list = [int(d) for d in user_number]
    result = 1
    for d in digits_list:
        result *= d
    print(f"{' * '.join(str(d) for d in digits_list)} = {result}")
    user_number = str(result)
    steps += 1
print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")