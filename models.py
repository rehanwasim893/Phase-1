"""
Data models for the Todo application.
"""

from datetime import datetime
from typing import Optional


class Todo:
    """
    Represents a todo item with id, title, description, and completion status.
    """

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Todo instance.

        Args:
            id (int): Unique identifier for the todo
            title (str): Title of the todo (required)
            description (str): Optional description of the todo
            completed (bool): Completion status (default: False)
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or whitespace-only")

        # Allow ID 0 for auto-assignment by storage layer
        if id < 0:
            raise ValueError("ID cannot be negative")

        self.id = id
        self.title = title.strip()
        self.description = description.strip()
        self.completed = completed
        self.created_date = datetime.now()

    def __str__(self):
        """String representation of the todo."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self):
        """Detailed string representation of the todo."""
        return f"Todo(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def validate_title(self, title: str) -> bool:
        """
        Validate that the title is not empty or whitespace-only.

        Args:
            title (str): Title to validate

        Returns:
            bool: True if title is valid, False otherwise
        """
        return title is not None and bool(title.strip())