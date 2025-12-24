MIN_TEMP = -200
MAX_TEMP = 200


def collectCelsius() -> float:
    """
    This is the doctring.

    This function collects temperature information.
    """
    try:
         Celsius  = float(input("Insert Celsius"))
    except Exception:
          raise Exception ("Something wrong")
    
    if (Celsius < MIN_TEMP) or (Celsius > MAX_TEMP):
            raise Exception (f"Out of range: {Celsius}")
 
    return Celsius
   
    

def main() -> None:
        try:
            Celsius = collectCelsius()
            print(f"You got {Celsius} degrees from the 'sensor'")
        except Exception as err:
            print (err)
        return None
main() 

