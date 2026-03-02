"""
Command-line interface for the Todo application.
"""

from typing import Optional
from service import TodoService
from models import Todo


class TodoCLI:
    """
    Command-line interface for interacting with the Todo application.
    """

    def __init__(self, service: TodoService):
        """
        Initialize the CLI with a Todo service.

        Args:
            service (TodoService): The service to use for todo operations
        """
        self.service = service

    def display_menu(self) -> None:
        """
        Show the main menu options to the user.
        """
        print("\n" + "="*40)
        print("         TODO APPLICATION MENU")
        print("="*40)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Complete/Incomplete")
        print("6. Exit")
        print("="*40)

    def get_user_choice(self) -> int:
        """
        Prompt user for menu selection and validate input.

        Returns:
            int: Valid menu option number selected by user

        Raises:
            ValueError: If user input cannot be converted to valid menu option
        """
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                raise ValueError("Choice must be between 1 and 6")
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError("Please enter a valid number")
            else:
                raise e

    def handle_add_todo_flow(self) -> None:
        """
        Manage the user interaction flow for adding a new todo.
        """
        print("\n--- Add New Todo ---")
        try:
            title = input("Enter todo title: ").strip()

            if not title:
                print("ERROR: Title cannot be empty!")
                return

            description = input("Enter description (optional, press Enter to skip): ").strip()

            todo = self.service.add_todo(title=title, description=description)
            print(f"✅ Todo added successfully with ID: {todo.id}")

        except ValueError as e:
            print(f"ERROR: {e}")

    def handle_view_todos_flow(self) -> None:
        """
        Manage the user interaction flow for viewing all todos.
        """
        print("\n--- View All Todos ---")
        try:
            todos = self.service.get_all_todos()

            if not todos:
                print("No todos found.")
                return

            print(f"\nFound {len(todos)} todo(s):\n")
            for todo in todos:
                status = "[COMPLETED]" if todo.completed else "[PENDING]"
                print(f"ID: {todo.id} | {status} | Title: {todo.title}")
                if todo.description:
                    print(f"     Description: {todo.description}")
                print("-" * 50)

        except Exception as e:
            print(f"ERROR: {e}")

    def handle_update_todo_flow(self) -> None:
        """
        Manage the user interaction flow for updating a todo.
        """
        print("\n--- Update Todo ---")
        try:
            if not self.service.get_all_todos():
                print("No todos available to update.")
                return

            self.display_todos_list()

            todo_id = int(input("Enter the ID of the todo to update: "))

            # Get the current todo to show existing values
            current_todo = self.service.get_todo_by_id(todo_id)
            print(f"Current title: {current_todo.title}")
            if current_todo.description:
                print(f"Current description: {current_todo.description}")

            new_title = input(f"Enter new title (press Enter to keep '{current_todo.title}'): ").strip()
            new_description = input(f"Enter new description (press Enter to keep current): ").strip()

            # Use current values if user pressed Enter without typing
            if not new_title:
                new_title = current_todo.title
            if new_description == "":
                new_description = current_todo.description

            updated_todo = self.service.update_todo(
                id=todo_id,
                title=new_title,
                description=new_description
            )
            print(f"✅ Todo {updated_todo.id} updated successfully!")

        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"ERROR: {e}")

    def handle_delete_todo_flow(self) -> None:
        """
        Manage the user interaction flow for deleting a todo.
        """
        print("\n--- Delete Todo ---")
        try:
            if not self.service.get_all_todos():
                print("No todos available to delete.")
                return

            self.display_todos_list()

            todo_id = int(input("Enter the ID of the todo to delete: "))

            # Confirm deletion
            try:
                todo_to_delete = self.service.get_todo_by_id(todo_id)
                confirm = input(f"Are you sure you want to delete '{todo_to_delete.title}'? (y/N): ").lower()

                if confirm != 'y':
                    print("Deletion cancelled.")
                    return
            except ValueError:
                print(f"ERROR: Todo with ID {todo_id} does not exist!")
                return

            success = self.service.delete_todo(todo_id)
            if success:
                print(f"✅ Todo {todo_id} deleted successfully!")
            else:
                print(f"ERROR: Failed to delete todo with ID {todo_id}")

        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"ERROR: {e}")

    def handle_mark_complete_flow(self) -> None:
        """
        Manage the user interaction flow for marking a todo complete/incomplete.
        """
        print("\n--- Mark Complete/Incomplete ---")
        try:
            if not self.service.get_all_todos():
                print("No todos available to mark.")
                return

            self.display_todos_list()

            todo_id = int(input("Enter the ID of the todo to mark: "))

            current_todo = self.service.get_todo_by_id(todo_id)
            current_status = "completed" if current_todo.completed else "incomplete"

            print(f"Current status: {current_status}")
            new_status_input = input("Mark as (1) Complete or (2) Incomplete? (1/2): ").strip()

            if new_status_input == "1":
                new_status = True
                status_text = "complete"
            elif new_status_input == "2":
                new_status = False
                status_text = "incomplete"
            else:
                print("ERROR: Invalid choice. Please enter 1 for Complete or 2 for Incomplete.")
                return

            updated_todo = self.service.mark_complete(todo_id, new_status)
            print(f"✅ Todo {updated_todo.id} marked as {status_text}!")

        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"ERROR: {e}")

    def display_todos_list(self) -> None:
        """
        Helper method to display a simple list of todos with IDs.
        """
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos found.")
            return

        print(f"\nCurrent todos ({len(todos)} total):")
        for todo in todos:
            status = "[DONE]" if todo.completed else "[TODO]"
            print(f"  {status} ID: {todo.id} - {todo.title}")

    def run(self) -> None:
        """
        Main CLI loop to run the application.
        """
        print("Welcome to the Todo Application!")

        while True:
            try:
                self.display_menu()
                choice = self.get_user_choice()

                if choice == 1:
                    self.handle_add_todo_flow()
                elif choice == 2:
                    self.handle_view_todos_flow()
                elif choice == 3:
                    self.handle_update_todo_flow()
                elif choice == 4:
                    self.handle_delete_todo_flow()
                elif choice == 5:
                    self.handle_mark_complete_flow()
                elif choice == 6:
                    print("Thank you for using the Todo Application. Goodbye!")
                    break
                else:
                    print("ERROR: Invalid choice. Please select a number between 1 and 6.")

            except ValueError as e:
                print(f"ERROR: Input Error: {e}")
            except KeyboardInterrupt:
                print("\nApplication interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"ERROR: Unexpected Error: {e}")