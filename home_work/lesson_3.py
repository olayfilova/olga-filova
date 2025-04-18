import json
from abc import ABC, abstractmethod
from typing import List, Iterator
from pydantic import BaseModel, field_validator, ValidationError
from functools import wraps


class BookModel(BaseModel):
    id: int
    title: str
    author: str
    year: int
    type: str = "book"

    # @field_validator('year')
    # @classmethod
    # def validate_year(self, value):
    #     if value < 0 or value > 2025:
    #         raise ValueError("Please, enter an appropriate year")
    #     return value


class Publication(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass


class Book(Publication):
    def __init__(self, model: BookModel):
        self._model = model

    def get_info(self) -> str:
        return f"Book: {self._model.title} (ID: {self._model.id}) Author: {self._model.author} Year: {self._model.year}"

    @property
    def title(self):
        return self._model.title

    @property
    def author(self):
        return self._model.author

    @property
    def id(self):
        return self._model.id


class Magazine(Book):
    def get_info(self) -> str:
        return f" Magazine: {self._model.title} (ID: {self._model.id}) Author: {self._model.author} Year: {self._model.year}"


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('library.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f"[LOG] Action:{func.__name__} Obj:{args[1].title}")
        return result

    return wrapper


def check_exists(func):
    @wraps(func)
    def wrapper(self, item):
        if item not in self._books:
            print(f"Book '{item.title}' is not found.")
            return
        return func(self, item)

    return wrapper


class FileManager:
    def __init__(self, filepath, library):
        self.filepath = filepath
        self.library = library

    def __enter__(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                max_id = 0
                for item in data:
                    model = BookModel(**item)
                    max_id = max(max_id, model.id)
                    if model.type == "magazine":
                        publication = Magazine(model)
                    else:
                        publication = Book(model)
                    self.library.add_book(publication)
                self.library._next_id = max_id + 1
        except FileNotFoundError:
            print("File not found - creating a new one.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = [
            {
                "id": b._model.id,
                "title": b._model.title,
                "author": b._model.author,
                "year": b._model.year,
                "type": "magazine" if isinstance(b, Magazine) else "book"
            }
            for b in self.library._books
        ]
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class Library:
    def __init__(self):
        self._books: List[Publication] = []
        self._next_id = 1

    def __iter__(self) -> Iterator[Publication]:
        return iter(self._books)

    @log_action
    def add_book(self, book: Publication):  # book:Publication
        if not hasattr(book._model, 'id'):
            book._model.id = self._next_id
            self._next_id += 1
        self._books.append(book)

    @check_exists
    def remove_book(self, book: Publication):  # book: Publication
        self._books.remove(book)

    def list_by_author(self, author: str):
        return [book for book in self._books if book.author.lower() == author.lower()]

    def get_by_id(self, book_id: int) -> Publication | None:
        for book in self._books:
            if book.id == book_id:
                return book
        return None

    def show_all(self):
        if not self._books:
            print("Library is empty")
            return
        for book in self._books:
            print(book.get_info())


if __name__ == "__main__":
    library = Library()

    book1 = Book(BookModel(id=1, title="Python Basics", author="John Smith", year=2020))
    book2 = Magazine(BookModel(id=2, title="Science Today", author="Maria Garcia", year=2021))
    book3 = Book(BookModel(id=3, title="Advanced Python", author="John Smith", year=2022))
    book4 = Book(BookModel(id=4, title="Data Structures", author="Alice Johnson", year=2023))

    # Adding books to library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    print("All books:")
    library.show_all()

    # Search by author
    author_name = "John Smith"
    print(f"\nBooks by {author_name}:")
    for book in library.list_by_author(author_name):
        print(book.get_info())

    # Get book by ID
    book_id = 2
    print(f"\nFinding book with ID {book_id}:")
    if found_book := library.get_by_id(book_id):
        print(found_book.get_info())
    else:
        print(f"No book found with ID {book_id}")

    # Save to JSON file
    with FileManager("books.json", library):
        pass

    # Remove a book by ID
    book_to_remove = library.get_by_id(1)
    if book_to_remove:
        library.remove_book(book_to_remove)

    print("\nAfter removing a book:")
    library.show_all()

    # Load from JSON file to a new library
    new_library = Library()
    with FileManager("books.json", new_library):
        print("\nLoaded from file:")
        new_library.show_all()
