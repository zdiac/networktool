logg = []  # Lista som ska lagra loggmeddelanden

def main():
    while True:
        print("\n--- NetworkTool ---")
        print("1. Validera IP-adress")
        print("2. Validera portnummer")
        print("3. Visa logg")
        print("4. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "4":
            print("Avslutar programmet...")
            break
        else:
            print("Funktionen är inte implementerad ännu.")

if __name__ == "__main__":
    def validate_ip(ip):
        pass

def validate_port(port):
    pass
    main()
if choice == "1":
    ip = input("Ange en ip-adress: ")
    validate_ip(ip)
    print("Validerar IP-adress...")