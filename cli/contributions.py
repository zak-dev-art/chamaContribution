from database import Session
from models import Contribution, Member, Meeting

def contributions_menu():
    session = Session()

    while True:
        print("\n--- CONTRIBUTIONS MENU ---")
        print("1. Add Contribution")
        print("2. View All Contributions")
        print("3. Back")
        choice = input("Choice: ")

        if choice == "1":
            member_id = int(input("Member ID: "))
            meeting_id = int(input("Meeting ID: "))
            amount = float(input("Amount: "))

            contribution = Contribution(
                member_id=member_id,
                meeting_id=meeting_id,
                amount=amount
            )

            session.add(contribution)
            session.commit()
            print("Contribution recorded.")

        elif choice == "2":
            contribs = session.query(Contribution).all()
            for c in contribs:
                print(f"{c.id} | Member: {c.member.name} | Meeting: {c.meeting.agenda} | Amount: {c.amount}")

        elif choice == "3":
            break
