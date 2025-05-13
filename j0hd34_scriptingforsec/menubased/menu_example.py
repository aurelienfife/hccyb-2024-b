# Menu-based app - console
# 4 options - each one should point to a function
# 1 - Tea  2 - Coffee  3 - Beer  4 - Quit

def menu():

    # We'll need that later
    choice = ""

    # Main while loop
    while choice != "4":
        # Offer the choices
        print('''Welcome to the pointless program:
1 - Tea
2 - Coffee
3 - Beer
4 - Quit''')

        choice = input("Make your selection: ")

        # switch / case
        match choice:
            case "1":
                print("Tea function will run")
            case "2":
                print("Coffee function will run")
            case "3":
                print("Beer function will run")
            case "4":
                print("Bye.")
            case _:                 # Any other value
                print("Invalid choice, try again.")



def main():
    # Add authentication code later

    menu()

if __name__ == "__main__":
    main()
