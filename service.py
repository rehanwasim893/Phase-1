"""
Business logic layer for the Todo application.
"""

from typing import List, Optional
from models import Todo
from storage import InMemoryStorage


class TodoService:
    """
    Service layer that handles business logic for todo operations.
    """

    def __init__(self, storage: InMemoryStorage):
        """
        Initialize the service with a storage backend.

        Args:
            storage (InMemoryStorage): Storage backend to use
        """
        self.storage = storage

    def add_todo(self, title: str, description: str = "") -> Todo:
        """
        Add a new todo with the provided title and optional description.

        Args:
            title (str): Required title for the new todo (min 1 non-whitespace char)
            description (str, optional): Optional description for the new todo

        Returns:
            Todo: Todo object with assigned ID and completion status set to False

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or whitespace-only")

        # Create a new Todo with 0 as ID to indicate auto-assignment (storage will assign next available ID)
        new_todo = Todo(id=0, title=title.strip(), description=description.strip() if description else "")
        return self.storage.add(new_todo)

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todo items currently in the system.

        Returns:
            List[Todo]: List of all Todo objects in storage, may be empty
        """
        return self.storage.get_all()

    def get_todo_by_id(self, id: int) -> Optional[Todo]:
        """
        Retrieve a specific todo item by its ID.

        Args:
            id (int): Unique identifier of the todo to retrieve (positive integer)

        Returns:
            Optional[Todo]: Todo object matching the provided ID, None if not found

        Raises:
            ValueError: If ID does not exist in storage
        """
        todo = self.storage.get_by_id(id)
        if todo is None:
            raise ValueError(f"Todo with ID {id} does not exist in storage")
        return todo

    def update_todo(self, id: int, title: str = None, description: str = None) -> Optional[Todo]:
        """
        Update an existing todo item's title and/or description.

        Args:
            id (int): Unique identifier of the todo to update
            title (str, optional): New title for the todo (if provided)
            description (str, optional): New description for the todo (if provided)

        Returns:
            Optional[Todo]: Updated Todo object, None if todo not found

        Raises:
            ValueError: If ID does not exist or if provided title is empty
        """
        # Check if the todo exists
        existing_todo = self.storage.get_by_id(id)
        if existing_todo is None:
            raise ValueError(f"Todo with ID {id} does not exist in storage")

        # Prepare update data
        update_data = {}
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty or whitespace-only")
            update_data['title'] = title.strip()

        if description is not None:
            update_data['description'] = description.strip() if description else ""

        # Perform the update
        return self.storage.update(id, **update_data)

    def delete_todo(self, id: int) -> bool:
        """
        Remove a todo item from the system by its ID.

        Args:
            id (int): Unique identifier of the todo to delete

        Returns:
            bool: True if todo was successfully deleted, False if ID did not exist
        """
        return self.storage.delete(id)

    def mark_complete(self, id: int, completed: bool = True) -> Optional[Todo]:
        """
        Update the completion status of a todo item.

        Args:
            id (int): Unique identifier of the todo to update
            completed (bool): New completion status (defaults to True)

        Returns:
            Optional[Todo]: Updated Todo object with new completion status, None if not found

        Raises:
            ValueError: If ID does not exist in storage
        """
        # Check if the todo exists
        existing_todo = self.storage.get_by_id(id)
        if existing_todo is None:
            raise ValueError(f"Todo with ID {id} does not exist in storage")

        # Update the completion status
        return self.storage.update(id, completed=completed)