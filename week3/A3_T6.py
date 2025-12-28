
print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below. \n")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
menu_select=int(input("Your choice: "))
if menu_select==1:
 print("\nLength options:")
 print("1 - Meters to kilometers")
 print("2 - Kilometers to meters")
 print("0 - Exit")
 length_choice=int(input("Your choice: "))
 if length_choice==1:
  val_m=float(input("Insert meters: "))
  val_k=val_m/1000
  print(f"{val_m} m is {val_k} km")
 elif length_choice==2:
  val_k=float(input("Insert kilometers: "))
  val_m=val_k*1000
  print(f"{val_k} km is {val_m} m")
 elif length_choice==0:
  print("Exiting...")
 else:
  print("Unknown option.")
elif menu_select==2:
 print("\nWeight options:")
 print("1 - Grams to pounds")
 print("2 - Pounds to grams")
 print("0 - Exit")
 weight_choice=int(input("Your choice: "))
 if weight_choice==1:
  val_g=float(input("Insert grams: "))
  val_lb=round(val_g/453.6,1)
  print(f"{val_g} g is {val_lb} lb")
 elif weight_choice==2:
  val_lb=float(input("Insert pounds: "))
  val_g=round(val_lb*453.6,1)
  print(f"{val_lb} lb is {val_g} g")
 elif weight_choice==0:
  print("Exiting...")
 else:
  print("Unknown option.")
elif menu_select==0:
 print("Exiting...")
else:
 print("Unknown option.")