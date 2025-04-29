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

```bash
mysql -u root -p
CREATE DATABASE library_db;
exit
mysql -u root -p library_db < library_db_dump.sql

