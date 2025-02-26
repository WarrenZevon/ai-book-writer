import json
import os
from pathlib import Path
from .data_models import Book, Chapter

class BookManager:
    def __init__(self):
        self.current_book = None
        self.data_dir = Path("data/book_outlines")
        
    def create_book(self, title, author):
        self.current_book = Book(title=title, author=author)
        return self.current_book
    
    def add_chapter(self, title, summary="", notes=None):
        if not self.current_book:
            raise ValueError("No book is currently open")
        
        chapter = Chapter(
            title=title,
            summary=summary,
            notes=notes or []
        )
        self.current_book.chapters.append(chapter)
        return chapter
    
    def save_book(self):
        if not self.current_book:
            raise ValueError("No book is currently open")
        
        self.data_dir.mkdir(parents=True, exist_ok=True)
        file_path = self.data_dir / f"{self.current_book.title.lower().replace(' ', '_')}.json"
        
        with open(file_path, 'w') as f:
            json.dump(self.current_book.to_dict(), f, indent=4)
    
    def load_book(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.current_book = Book.from_dict(data)
        return self.current_book