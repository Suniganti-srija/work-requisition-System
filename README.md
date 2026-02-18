🛠️ Work Requisition Management System

A web-based Work Requisition Management System built using Django that allows employees to submit, track, and manage internal work requests efficiently. The system provides role-based access control and streamlined approval workflows.

🚀 Features

User Registration & Authentication

Role-Based Access (Admin / Employee)

Create, Update, Delete Work Requests (CRUD)

Request Status Tracking (Pending / Approved / Rejected)

Dashboard for Admin Monitoring

Secure Form Validation

Database Integrity using Foreign Keys

Responsive UI

🏗️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: MySQL / SQLite

Version Control: Git & GitHub

📂 Project Structure
work-requisition-system/
│
├── requisition_app/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/work-requisition-system.git
cd work-requisition-system

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver


Open browser and go to:

http://127.0.0.1:8000/

🗄️ Database Design

Normalized relational schema

Foreign key relationships for request-user mapping

Indexed fields for optimized query performance

Maintained referential integrity

🔐 Security Features

Django Authentication System

CSRF Protection

Form Validation

Session Management

📊 Future Enhancements

Email Notifications

REST API Integration

Pagination

Deployment on Cloud (AWS / Heroku)

Role Expansion (Manager Level)

👩‍💻 Author

Your Name
Final Year B.Tech – Computer Science (Data Science)

📜 License

This project is for educational and demonstration purposes.


