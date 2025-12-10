from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, Book

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST/books
@app.post("/books/")
def create_book(title: str, author: str, year: int | None = None, db: Session = Depends(get_db)):
    new_book = Book(title=title, author=author, year=year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# GET/books
@app.get("/books/")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

# DELETE/books/{book_id}
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}

# PUT /books/{book_id}
@app.put("/books/{book_id}")
def update_book(book_id: int, title: str | None = None, author: str | None = None, year: int | None = None, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if title is not None:
        book.title = title
    if author is not None:
        book.author = author
    if year is not None:
        book.year = year

    db.commit()
    db.refresh(book)
    return book

# GET /books/search
@app.get("/books/search/")
def search_books(title: str | None = None, author: str | None = None, year: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)

    return query.all()
