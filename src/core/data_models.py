from typing import List, Dict
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Chapter:
    title: str
    summary: str = ""
    notes: List[str] = field(default_factory=list)
    content: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "summary": self.summary,
            "notes": self.notes,
            "content": self.content
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Chapter':
        return cls(
            title=data["title"],
            summary=data["summary"],
            notes=data["notes"],
            content=data["content"]
        )

@dataclass
class Book:
    title: str
    author: str
    chapters: List[Chapter] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "author": self.author,
            "chapters": [chapter.to_dict() for chapter in self.chapters],
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        book = cls(
            title=data["title"],
            author=data["author"],
            created_at=data["created_at"]
        )
        book.chapters = [Chapter.from_dict(ch) for ch in data["chapters"]]
        return book