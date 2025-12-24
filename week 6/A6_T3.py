def readfile(filename) -> str:
    Content = ""
    return Content

def writefile(filename, Content) -> None:
    print("Writing into file {}".format(filename))
    filehandle = open(filename, "w", encoding="utf-8")
    filehandle.write(Content)
    filehandle.close()

    return None

def main() -> None:
    print ("Program starting.")
    print ("This program can read a file.")
    filenamesource = input("Insert source filename: ")
    filenameDestination = input("Insert destination filename: ")
    Content = readfile(filenamesource)
    print ("File content ready in memory.")
    writefile(filenameDestination, Content)
    print("Copying operation complete.")
    print ("Program ending.")
    return None 


if __name__ == "__main__":
    main()




 

