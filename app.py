from cli.members import members_menu
from cli.meetings import meetings_menu
from cli.contributions import contributions_menu


def main():
    while True:
        print("\n=== CHAMA CONTRIBUTION TRACKER ===")
        print("1. Members")
        print("2. Meetings")
        print("3. Contributions")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            members_menu()
        elif choice == "2":
            meetings_menu()
        elif choice == "3":
            contributions_menu()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
