from database import Session
from models import Member

def members_menu():
    session = Session()

    while True:
        print("\n--- MEMBERS MENU ---")
        print("1. Add Member")
        print("2. View Members")
        print("3. Delete Member")
        print("4. Back")
        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            new_member = Member(name=name, phone=phone)
            session.add(new_member)
            session.commit()
            print("Member added.")

        elif choice == "2":
            members = session.query(Member).all()
            for m in members:
                print(m)

        elif choice == "3":
            member_id = int(input("Member ID: "))
            member = session.query(Member).get(member_id)
            if member:
                session.delete(member)
                session.commit()
                print("Member deleted.")
            else:
                print("Member not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")
