Contact Management System (Flask + SQLite)

This is a simple contact manager web application developed using Python, Flask, and SQLite.
It was built as part of a task for the Software Developer position at Gokul Infocare.

✨ Features:
- Add new contacts
- View all saved contacts
- Update existing contact details
- Delete contacts
- Flash messages for user feedback
- Validates email format and prevents duplicates

📋 Each contact includes:
- First Name
- Last Name
- Email Address
- Phone Number
- Address

🛠️ Technology Stack:
- Python 3
- Flask (Web Framework)
- Flask-SQLAlchemy (ORM)
- SQLite (Database)
- HTML + Bootstrap (Frontend Styling)

💾 How to Run:

1. Install Python if not already installed.
2. Install the required packages:
   pip install -r requirements.txt

3. Create the database:
   Run Python shell and execute:
   >>> from app import db
   >>> db.create_all()
   >>> exit()

4. Start the Flask server:
   python app.py

5. Open your browser and visit:
   http://localhost:5000/

📁 Project Structure:
- app.py: Main Flask application
- templates/: HTML files (index.html, add.html, update.html)
- contacts.db: SQLite database file (auto-created)
- requirements.txt: Python dependencies
- README.txt: Project instructions

👩‍💻 Developer:
Likhitha

📅 Date:
July 2025

📌 Note:
This project is submitted as Task 1 for the selection process at Gokul Infocare.
