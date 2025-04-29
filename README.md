#  Library Management System

-  **Question 1**: MySQL Database Design with constraints and relationships
-  **Question 2**: A full CRUD API using FastAPI + MySQL
-  BONUS: Basic HTML frontend to test category operations

---

##  QUESTION 1: Database Design (MySQL)

###  Objective:
Design and implement a full-featured relational database with:
- Proper constraints (PK, FK, NOT NULL, UNIQUE)
- Logical relationships (1-1, 1-M, M-M where needed)
- Sample data

---

###  Use Case Chosen:
**Library Management System**

We manage:
-  Categories of books
-  Authors
-  Books
-  Members
-  Loans (who borrowed which book, and when)

---

###  Tables & Constraints:

- `categories(category_id PK, name UNIQUE NOT NULL)`
- `authors(author_id PK, name NOT NULL)`
- `books(book_id PK, title, isbn UNIQUE, FK to category_id, FK to author_id)`
- `members(member_id PK, full_name, email UNIQUE)`
- `loans(loan_id PK, book_id FK, member_id FK, loan_date, return_date)`

---

###  Relationships

- 1–M: Categories → Books
- 1–M: Authors → Books
- 1–M: Members → Loans
- 1–M: Books → Loans

---

###  SQL Script File

 **library_db_dump.sql**  
Contains:
- `DROP` + `CREATE TABLE` statements
- Foreign key constraints
- Sample `INSERT INTO` rows (e.g., categories)

---

###  How to Import the DB

mysql -u root -p
CREATE DATABASE library_db;
exit
mysql -u root -p library_db < library_db_dump.sql

#  Library Management CRUD API

**Question 2** 

Implementation of a **CRUD API** using **FastAPI (Python)** and **MySQL**. It includes:

- A clean, relational MySQL database schema
- Full CRUD operations for categories (and extendable to other entities)
- A basic HTML frontend for testing
- A complete SQL script and full project setup instructions

---

##  Objective

> **Create a working CRUD API using MySQL and a programming language**

- Programming Language: **Python + FastAPI**  
- DB Engine: **MySQL 8.x**  
- ORM: **SQLAlchemy**  
- API: **CRUD operations for library categories**  
- Validation: **Pydantic**  
- Frontend: **(Optional)** HTML interface for testing  
- SQL Script: Included as `library_db_dump.sql`  

---

##  Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Backend API  | FastAPI (Python)     |
| ORM          | SQLAlchemy           |
| DB Connector | mysql-connector-python |
| DB Server    | MySQL 8              |
| Dev Server   | Uvicorn              |
| Frontend     | HTML + JS (Optional) |

---

##  Database Schema

| Table      | Description                        |
|------------|------------------------------------|
| categories | Stores book categories             |
| authors    | Stores authors                     |
| books      | Stores books with FK to authors, categories |
| members    | Library members                    |
| loans      | Tracks book loans to members       |

 All foreign keys, constraints, and sample data are included in: library_db_dump.sql


---

##  FULL SETUP INSTRUCTIONS — RUN LOCALLY

###  STEP 1: Clone the repository


git clone https://github.com/ochiengtim/library_api.git
cd library_api


STEP 2: Set up a virtual environment (recommended)

python -m venv venv
Windows (PowerShell): .\venv\Scripts\Activate.ps1
Windows (CMD): .\venv\Scripts\activate


STEP 3: Install Python dependencies

pip install -r requirements.txt

STEP 4: Create the MySQL database

CREATE DATABASE library_db;
Or from CMD:
mysql -u root -p
CREATE DATABASE library_db;
exit

STEP 5: Import the schema and sample data

mysql -u root -p library_db < library_db_dump.sql

STEP 6: Verify the database URL in app/db.py

# app/db.py
DATABASE_URL = "mysql+mysqlconnector://root:your_mysql_password@localhost:3306/library_db"

STEP 7: Run the FastAPI application

python -m app.main

Output should say:

Uvicorn running on http://127.0.0.1:8000

STEP 8: Open the API documentation
Open in your browser:

http://127.0.0.1:8000/docs

 Sample CRUD Endpoints
| Method | Endpoint | Description               |
|--------|----------|---------------------------|
| GET    | `/categories/`       | Fetch all categories        |
| POST   | `/categories/`       | Create a new category       |
| PUT    | `/categories/{id}`   | Update a category by ID     |
| DELETE | `/categories/{id}`   | Delete a category by ID     |

OPTIONAL: Run the HTML frontend
Navigate to the frontend folder and run a simple HTTP server:

cd frontend
python -m http.server 5500

Open in your browser:
http://127.0.0.1:5500/index.html

##  ERD

This ERD visualizes the relationship between categories, authors, books, members, and loans.

 [View ERD on dbdiagram.io](https://dbdiagram.io/d/681122a01ca52373f5df3652)

Or refer to the image below:

[ERD](<img width="602" alt="Screenshot 2025-04-29 221505" src="https://github.com/user-attachments/assets/40377309-e577-473a-a352-1d5daa90bc41" />)

<img width="602" alt="image" src="https://github.com/user-attachments/assets/e6766ff7-385f-45aa-87eb-0340d4c75d6e" />


