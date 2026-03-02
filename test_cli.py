#!/usr/bin/env python3
"""
Simple test script to verify the Todo application components work correctly.
"""

from storage import InMemoryStorage
from service import TodoService
from cli import TodoCLI

def test_application():
    print("Testing the Todo application components...\n")

    # Initialize the storage
    storage = InMemoryStorage()
    print("[OK] Storage initialized")

    # Initialize the service with the storage
    service = TodoService(storage)
    print("[OK] Service initialized")

    # Initialize the CLI with the service
    cli = TodoCLI(service)
    print("[OK] CLI initialized")

    # Test adding a todo
    todo = service.add_todo("Test todo", "This is a test")
    print(f"[OK] Added todo: {todo.title} with ID {todo.id}")

    # Test getting all todos
    todos = service.get_all_todos()
    print(f"[OK] Retrieved {len(todos)} todos")

    # Test updating the todo
    updated_todo = service.update_todo(todo.id, title="Updated test todo")
    print(f"[OK] Updated todo: {updated_todo.title}")

    # Test marking as complete
    completed_todo = service.mark_complete(todo.id, True)
    print(f"[OK] Marked todo as {'complete' if completed_todo.completed else 'incomplete'}")

    # Test listing todos
    cli.handle_view_todos_flow()

    print("\n[SUCCESS] All components are working correctly!")

if __name__ == "__main__":
    test_application()