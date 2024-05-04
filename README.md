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
   git clone https://github.com/your_username/your_repository.git

2. Navigate to the project directory:
   ```bash 
   mkdir your_repo
   cd your_ repo

3. Install and activate virtual environment
   ```bash
   pipenv install
   pipenv shell

4. install all dependencies used
   ```bash
   pip install -r requirements.txt

5. After creating your Postgres database instance , migrate the migrations to your database.
   '''bash
   alembic upgrade head 
