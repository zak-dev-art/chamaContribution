# CHAMA CONTRIBUTION TRACKER

The CHAMA Contribution Tracker is a command-line application designed to help local Kenyan savings groups (chamas) manage their members, meetings, and contribution records in a simple and efficient way.
It provides a lightweight digital system for tracking annual, monthly, or weekly contributions using an easy-to-navigate CLI menu.

## Project Overview

Many chama groups operate manually using notebooks, WhatsApp notes, or memory.
This CLI project provides a structured, safe, and accessible way to:

Register members
Record meeting sessions
Track contributions made during each meeting
View contribution summaries
Maintain a clean database that persists between sessions

The system uses Python, SQLAlchemy ORM, and SQLite to manage data.

## Technologies Used

Python 3
SQLAlchemy ORM
SQLite (chama_tracker.db)
Pipenv (for virtual environment & dependencies)

## Project Structure

.
├── app.py # CLI entry point
├── README.md
├── chama_tracker.db # SQLite database
├── cli/
│ ├── members.py  
│ ├── models.py # SQLAlchemy models (Member, Meeting, Contribution)
│ └── contributions.py # Optional test data
└── database.py

## Key Features

1. Member Management
   Add new members
   View all members
   Find a member by ID
   Delete a member
   View contributions made by a specific member

2. Meeting Management
   Schedule a meeting
   View meeting records
   Delete a meeting
   View contributions made in a specific meeting

3. Contribution Tracking
   Record a member’s contribution for a meeting
   Validate member & meeting existence
   Prevent invalid inputs

4. Data Persistence
   All data is stored safely in an SQLite database
   SQLAlchemy ORM handles relationships and constraints

5. Clean CLI Menu
   Simple
   Beginner-friendly
   Error-handled

## Database Design

Database Name
chama_tracker.db

Tables (3 total)

1. Members Table
   Stores personal information for each chama participant.

2. Meetings Table
   Records each meeting session and its agenda.

3. Contributions Table
   Links members to meetings and stores contribution amounts.

## Entity Relationships

One Member → Many Contributions
One Meeting → Many Contributions

This means each contribution belongs to exactly one member and one meeting.

## Installation Instructions

1. Clone the project
   git clone <your-repo-url>
   cd chama-contribution-tracker

2. Install dependencies using Pipenv
   pipenv install
   pipenv shell

3. Run the application
   python app.py

4. Database creation

Tables are automatically generated using:
Base.metadata.create_all(engine)

## How to Test the Application

Test through the CLI

Run:
python app.py

Test all menu options:

Add members
Add meetings
Add contributions
Test invalid inputs
Delete items
View summaries
View database directly (optional)
sqlite3 chama_tracker.db
.tables
SELECT \* FROM members;

## Example CLI Menu

============================
CHAMA CONTRIBUTION TRACKER
============================

1. Manage Members
2. Manage Meetings
3. Record Contribution
4. View Contribution Summaries
5. Exit

## Folder/Module Breakdown

db/database.py

Creates SQLite engine
Creates session factory
Defines SQLAlchemy Base
db/models.py

Defines all 3 models:
Member
Meeting
Contribution
Defines relationships
Includes validation using property methods

## Future Improvements

Export reports to CSV

Add login/authentication

Add payment reminders

Generate graphs of contributions

Build a web version using Flask

# Deveoper : Zakayo Kagunda
