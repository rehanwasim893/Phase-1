"""
In-memory storage for the Todo application.
"""

from typing import Dict, List, Optional
from models import Todo


class InMemoryStorage:
    """
    In-memory storage implementation using a dictionary to store todos.
    """

    def __init__(self):
        """Initialize the storage with an empty dictionary and ID counter."""
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def add(self, todo: Todo) -> Todo:
        """
        Add a new todo to storage.

        Args:
            todo (Todo): Todo object to add

        Returns:
            Todo: The added Todo object
        """
        # If ID is 0 or negative, assign the next available ID
        if todo.id <= 0:
            todo.id = self._next_id
            self._next_id += 1

        self._todos[todo.id] = todo
        return todo

    def get_all(self) -> List[Todo]:
        """
        Retrieve all todos from storage.

        Returns:
            List[Todo]: List of all Todo objects
        """
        return list(self._todos.values())

    def get_by_id(self, id: int) -> Optional[Todo]:
        """
        Retrieve a specific todo by its ID.

        Args:
            id (int): ID of the todo to retrieve

        Returns:
            Optional[Todo]: The Todo object if found, None otherwise
        """
        return self._todos.get(id)

    def update(self, id: int, **kwargs) -> Optional[Todo]:
        """
        Update an existing todo.

        Args:
            id (int): ID of the todo to update
            **kwargs: Fields to update (title, description, completed)

        Returns:
            Optional[Todo]: Updated Todo object if found, None otherwise
        """
        if id not in self._todos:
            return None

        todo = self._todos[id]

        # Update fields if provided
        if 'title' in kwargs:
            if kwargs['title'] and kwargs['title'].strip():
                todo.title = kwargs['title'].strip()
            else:
                raise ValueError("Title cannot be empty or whitespace-only")

        if 'description' in kwargs:
            todo.description = kwargs['description'].strip() if kwargs['description'] else ""

        if 'completed' in kwargs:
            todo.completed = kwargs['completed']

        return todo

    def delete(self, id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            id (int): ID of the todo to delete

        Returns:
            bool: True if deletion was successful, False if todo not found
        """
        if id not in self._todos:
            return False

        del self._todos[id]
        return True

    def get_storage_size(self) -> int:
        """
        Get the count of todos currently in storage.

        Returns:
            int: Number of todos in storage
        """
        return len(self._todos)

    def clear_storage(self) -> None:
        """
        Remove all todos from storage (for testing/reset purposes).
        """
        self._todos.clear()
        self._next_id = 1