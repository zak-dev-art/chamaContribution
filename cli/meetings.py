from db.models import Member, Meeting, Contribution, session
from datetime import datetime

# INPUT VALIDATION HELPERS

def get_int(prompt):
    """Ensure user enters a valid integer."""
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Invalid input. Enter a number.")

def get_float(prompt):
    """Ensure user enters a valid float."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid amount. Enter a number like 100 or 150.50.")

def get_nonempty_text(prompt):
    """Ensure user enters a non-empty string."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


# MEMBER FUNCTIONS

def add_member():
    name = get_nonempty_text("Enter member name: ")
    phone = get_nonempty_text("Enter phone number: ")

    try:
        member = Member.create(name=name, phone=phone)
        print(f"Member '{member.name}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_member():
    member_id = get_int("Enter Member ID to delete: ")
    member = Member.find_by_id(member_id)

    if member:
        member.delete()
        print("Member deleted successfully.")
    else:
        print("Member not found.")


def show_all_members():
    members = Member.get_all()
    if not members:
        print("No members found.")
        return

    for m in members:
        print(f"ID: {m.id} | Name: {m.name} | Phone: {m.phone} | Joined: {m.join_date}")


def find_member():
    name = get_nonempty_text("Enter member name to search: ")

    members = session.query(Member).filter(Member._name.like(f"%{name}%")).all()

    if not members:
        print("No matching members found.")
        return

    for m in members:
        print(f"ID: {m.id} | Name: {m.name} | Phone: {m.phone}")


def view_member_contributions():
    member_id = get_int("Enter Member ID: ")
    member = Member.find_by_id(member_id)

    if not member:
        print("Member not found.")
        return

    if not member.contributions:
        print("This member has no contributions yet.")
        return

    print(f"\nContributions for {member.name}:")
    for c in member.contributions:
        print(f"Amount: {c.amount} | Date: {c.timestamp} | Meeting ID: {c.meeting_id}")


# MEETING FUNCTIONS

def add_meeting():
    date_input = get_nonempty_text("Enter meeting date (YYYY-MM-DD): ")
    agenda = get_nonempty_text("Enter agenda: ")

    try:
        meeting_date = datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    meeting = Meeting.create(meeting_date=meeting_date, agenda=agenda)
    print("Meeting added successfully.")


def delete_meeting():
    meeting_id = get_int("Enter Meeting ID to delete: ")
    meeting = Meeting.find_by_id(meeting_id)

    if meeting:
        meeting.delete()
        print("Meeting deleted successfully.")
    else:
        print("Meeting not found.")


def show_all_meetings():
    meetings = Meeting.get_all()

    if not meetings:
        print("No meetings found.")
        return

    for m in meetings:
        print(f"ID: {m.id} | Date: {m.meeting_date} | Agenda: {m.agenda}")


def view_meeting_contributions():
    meeting_id = get_int("Enter Meeting ID: ")
    meeting = Meeting.find_by_id(meeting_id)

    if not meeting:
        print("Meeting not found.")
        return

    if not meeting.contributions:
        print("No contributions recorded for this meeting.")
        return

    print(f"\nContributions for Meeting on {meeting.meeting_date}:")
    for c in meeting.contributions:
        print(f"Member: {c.member.name} | Amount: {c.amount} | Timestamp: {c.timestamp}")


# CONTRIBUTION FUNCTIONS

def add_contribution():
    member_id = get_int("Enter Member ID: ")
    meeting_id = get_int("Enter Meeting ID: ")
    amount = get_float("Enter contribution amount: ")

    if not Member.find_by_id(member_id):
        print("Member does not exist.")
        return

    if not Meeting.find_by_id(meeting_id):
        print("Meeting does not exist.")
        return

    try:
        contribution = Contribution.create(
            member_id=member_id,
            meeting_id=meeting_id,
            amount=amount,
        )
        print("Contribution added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_contribution():
    contribution_id = get_int("Enter Contribution ID to delete: ")
    contribution = Contribution.find_by_id(contribution_id)

    if contribution:
        contribution.delete()
        print("Contribution deleted successfully.")
    else:
        print("Contribution not found.")


def show_all_contributions():
    contributions = Contribution.get_all()
    if not contributions:
        print("No contributions found.")
        return

    for c in contributions:
        print(f"ID: {c.id} | Member: {c.member.name} | Meeting: {c.meeting.date} | Amount: {c.amount}")


def contribution_summary():
    """Show total contributions per member."""
    members = Member.get_all()

    if not members:
        print("No members found.")
        return

    print("\n=== Contribution Summary ===")
    for member in members:
        total = sum([c.amount for c in member.contributions])
        print(f"{member.name}: KES {total}")
