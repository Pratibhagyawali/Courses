import sys 

def readlines(PFilepath: str, Plines: list[str]) -> None:
    try:
        Filehandle = open(PFilepath, 'r', encoding= "utf-8")
        Line = Filehandle.readline()
        while Line != '':
              Plines.append(Line)
              Line = Filehandle.readline()
    except FileNotFoundError:
        print("Try another file")
        #except FileNotFoundError:
        #print("Try another file")
        #lets start the program from the beginning
    except Exception as err:
        print ("File found, but something else went wrong. Closing the program.")
        sys.exit(1)
    return None


def main() -> None:
    Lines: list[str] = []
    Filename = input ("Insert filename")
    readlines(Filename, Lines)
    for Line in Lines:
        print(Line)
    return None
main()

