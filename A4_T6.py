print("Program starting.")
user_input = int(input("Insert a positive integer: "))
sequence = [user_input]  
step = 0

while user_input != 1:
    if user_input % 2 == 0:
        user_input = user_input // 2
    else:
        user_input = (user_input * 3) + 1
    sequence.append(user_input)
    step += 1

print(' -> '.join(str(num) for num in sequence))
print(f"Sequence had {step} total steps.\n")
print("Program ending.")