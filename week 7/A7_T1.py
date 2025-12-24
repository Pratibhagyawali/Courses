
def askPositiveInteger() -> int:
    positive_integer = -1
    Feed = input("Insert a positive integer (negative stops): ")
    if Feed.isnumeric():
      positive_integer = int(Feed)
    return positive_integer
    

def displayIntegers(integers: list[int]) -> None:
     if len(integers) == 0:
        print("No integers to display.")
     else:
       print(f"Displaying {len(integers)} integers:")
       print(f"-Index i (i)", end ="")
       print(f" => Ordinal (i+1) ", end ="")
       print (f"=> Value ", end ="")
     return None

def main():
    print("Program starting.")
    print("Collect positive integers.")
    positive_integers: list[int] = []
    Currentinteger = askPositiveInteger()
    print("Stopped collecting positive integers:")
    displayIntegers(positive_integers)

    return None

if __name__ == "__main__":
    main()

   





