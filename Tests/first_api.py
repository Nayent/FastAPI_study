from typing import List, Optional
from fastapi import FastAPI

app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


@app.get("/")
async def get_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def get_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 1

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    
    BOOKS[f'book_{current_book_id + 1}'] = {
        'title': book_title,
        'author': book_author
    }

    return BOOKS[f'book_{current_book_id + 1}']


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_inf = {
        'title': book_title,
        'author': book_author
    }

    if book_name in BOOKS:
        BOOKS[book_name] = book_inf
        return BOOKS[book_name]
    else:
        return {'message': 'Book does not exist!'}


@app.delete("/")
async def delete_book(book_name: str):
    if book_name in BOOKS:
        del BOOKS[book_name]
        return {'message': f'Book {book_name} deleted.'}
    else:
        return {'message': 'Book does not exist!'}