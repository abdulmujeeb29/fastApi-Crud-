import pytest
from fastapi.testclient import TestClient
from main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base , Book
from schema import BookCreate

# Create a new test database engine and session factory
@pytest.fixture(scope="module")
def test_db():
    # Connect to the test database
    engine = create_engine("postgresql://postgres:thales@localhost/postgres")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    # Create test data
    book_data = {"title": "Test Book", "author": "Test Author", "year": 2024, "isbn": "1234567890"}
    db_book = Book(**book_data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    yield db
    # Teardown: close the database connection
    db.close()
    Base.metadata.drop_all(bind=engine)

# Define the test client for the FastAPI app
@pytest.fixture(scope="module")
def test_app(test_db):
    # Use the test database
    def override_get_db():
        yield test_db
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    # Teardown: remove the test database dependency override
    app.dependency_overrides.clear()

# Test cases for create_book endpoint
def test_create_book(test_app):
    response = test_app.post("/books/", json={"title": "New Test Book", "author": "New Test Author", "year": 2025, "isbn": "0987654321"})
    assert response.status_code == 200
    assert response.json()["title"] == "New Test Book"

# Test cases for read_book endpoint
def test_read_book(test_app):
    response = test_app.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

# Test cases for read_books endpoint
def test_read_books(test_app):
    response = test_app.get("/books/")
    assert response.status_code == 200
    



def test_update_book(test_app):
    # Create a new book
    response = test_app.post("/books/", json={"title": "Test Book", "author": "Test Author", "year": 2024, "isbn": "1234567890"})
    assert response.status_code == 200
    book_id = response.json()["id"]

    # Update the book
    response = test_app.put(f"/books/{book_id}", json={"title": "Updated Test Book", "author": "Updated Test Author", "year": 2025, "isbn": "0987654321"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Book"
    assert response.json()["author"] == "Updated Test Author"
    assert response.json()["year"] == 2025
    assert response.json()["isbn"] == "0987654321"

def test_delete_book(test_app):
    # Create a new book
    response = test_app.post("/books/", json={"title": "Test Book", "author": "Test Author", "year": 2024, "isbn": "1234567890"})
    assert response.status_code == 200
    book_id = response.json()["id"]

    # Delete the book
    response = test_app.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
    assert response.json()["author"] == "Test Author"
    assert response.json()["year"] == 2024
    assert response.json()["isbn"] == "1234567890"