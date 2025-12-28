def main() -> None:
    print("Program starting.")
    print("This program can read a file.")

    filename = input("Insert filename: ")

    try:
        filehandle = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Error: File not found.")
        print("Program ending.")
        return

    print(f'#### START "{filename}" ####')

    for line in filehandle:
        print(line, end="")   
    print(f'\n#### END "{filename}" ####')

    filehandle.close()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
