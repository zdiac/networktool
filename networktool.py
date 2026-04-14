logg = []  # Lista som ska lagra loggmeddelanden


def validate_ip(ip):
    delar = ip.split(".")

    if len(delar) != 4:
        print("Ogiltig IP-adress: fel antal delar.")
        return
    
    for del_ in delar:
        if not del_.isdigit():
            print("Ogiltig IP-adress: alla delar måste vara siffror.")
            return
        
        nummer = int(del_)
        if nummer < 0 or  nummer > 255:
            print("Ogiltig IP-adress: varje del måste vara 0-255.")
            return
        
    print("IP-adressen är giltig!")


def validate_port(port):
    logg.apend(f"Validerade port: {port}")

    if not port.isdigit()
        print("Ogiltigt portnummer: måste vara en siffra")
        return
    
    nummer = int(port)

    if nummer < 0 or nummer > 65535:
        print("Ogiltigt portnummer: måste vara mellan 0 och 65535")
        return
    
    print("Portnumret är giltigt!")



def main():
    while True:
        print("\n--- NetworkTool ---")
        print("1. Validera IP-adress")
        print("2. Validera portnummer")
        print("3. Visa logg")
        print("4. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            ip = input("Ange en IP-adress: ")
            validate_ip(ip)
            logg.append(f"Validerade IP: {ip}")
                
        elif choice == "2":
            port = input("Ange ett portnummer: ")
            validate_port(port)  
            logg.append(f"Validerade port: {port}") 

        elif choice == "3":
            print("\n--- Logg ----")
            for entry in logg:
                print(entry)    

        elif choice =="4":
            print("Avslutar programmet...")
            break

        else:
            print("Funktionen är inte implementerad ännu.")


if __name__ == "__main__":
    main()