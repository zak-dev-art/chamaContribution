from cli.meetings import (
    add_member,
    list_members,
    add_meeting,
    list_meetings,
    record_contribution,
    list_contributions,
    member_contribution_summary
)

def main_menu():
    while True:
        print("\n===== CHAMA CONTRIBUTION TRACKER =====")
        print("1. Add Member")
        print("2. View Members")
        print("3. Add Meeting")
        print("4. View Meetings")
        print("5. Record Contribution")
        print("6. View All Contributions")
        print("7. View Member Contribution Summary")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            add_member()

        elif choice == "2":
            list_members()

        elif choice == "3":
            add_meeting()

        elif choice == "4":
            list_meetings()

        elif choice == "5":
            record_contribution()

        elif choice == "6":
            list_contributions()

        elif choice == "7":
            member_contribution_summary()

        elif choice == "8":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main_menu()
