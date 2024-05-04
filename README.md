# FastAPI Application

## Overview

This is a FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for managing books. It is built using Python and PostgreSQL.

## Setup

### Requirements

- Python
- fastapi
- PostgreSQL

### Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/abdulmujeeb29/fastApi-Crud-.git

2. Navigate to the project directory:
   ```bash 
   
   cd fastApi-Crud-

3. Install and activate virtual environment
   ```bash
   pipenv install
   pipenv shell

4. install all dependencies used
   ```bash
   pip install -r requirements.txt

5. After creating your Postgres database instance , update the DATABASE_URL in database.py, with your database connection URL,
 ```bash
  DATABASE_URL = "postgresql://username:password@localhost/db_name"
 ```

6. Run database migrate to upgrade the schema of the database,
 ```bash
  alembic upgrade head
```

7. Start server
```bash
   unicorn main:app --reload
```
###Testing
To run unit tests, update DATABASE_URL  in the test.py to point yo your testing database .
```bash
   DATABASE_URL = "postgresql://username:password@localhost/test_db"
```
Note: Ensure you switch to your testing database when you want to test to avoid conflicts .

