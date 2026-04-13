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
    main()
