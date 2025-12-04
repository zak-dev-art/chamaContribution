from database import Session
from models import Meeting

def meetings_menu():
    session = Session()

    while True:
        print("\n--- MEETINGS MENU ---")
        print("1. Add Meeting")
        print("2. View Meetings")
        print("3. Delete Meeting")
        print("4. Back")
        choice = input("Choice: ")

        if choice == "1":
            agenda = input("Agenda: ")
            meeting = Meeting(agenda=agenda)
            session.add(meeting)
            session.commit()
            print("Meeting added.")

        elif choice == "2":
            meetings = session.query(Meeting).all()
            for m in meetings:
                print(m)

        elif choice == "3":
            meeting_id = int(input("Meeting ID: "))
            meeting = session.query(Meeting).get(meeting_id)
            if meeting:
                session.delete(meeting)
                session.commit()
                print("Meeting deleted.")
            else:
                print("Not found.")

        elif choice == "4":
            break
