import time

def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askPauseDuration() -> float:
    return float(input("Insert pause duration (s): "))

def main() -> None:
    print("Program starting.")
    pause_duration = 1.0  

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            pause_duration = askPauseDuration()

        elif choice == 2:
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.")

        elif choice == 0:
            print("Exiting program.")
            break

    print("Program ending.")

if __name__ == "__main__":
    main()
