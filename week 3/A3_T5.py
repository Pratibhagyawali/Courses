print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    Celsius = float(input("Insert the amount of Celsius: "))
    temp_Fahrenheit = round((1.8 * Celsius) + 32, 1)
    print(f"{Celsius} °C equals to {temp_Fahrenheit} °F\n")

elif choice == 2:
    temp_Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = round((temp_Fahrenheit - 32) / 1.8, 1)
    print(f"{temp_Fahrenheit} °F equals to {Celsius} °C\n")

elif choice == 0:
    print("Exiting...\n")

else:
    print("Unknown option.\n")

print("Program ending.")
