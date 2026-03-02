# Service Contracts: Todo In-Memory Python Console Application

## Todo Service Interface

### Core Operations

#### add_todo(title: str, description: str = "") -> Todo
**Purpose**: Creates a new todo item with the provided title and optional description
**Parameters**:
- `title` (str): Required title for the new todo (min 1 non-whitespace char)
- `description` (str, optional): Optional description for the new todo
**Returns**: Todo object with assigned ID and completion status set to False
**Exceptions**:
- `ValueError`: If title is empty or contains only whitespace
**Side Effects**: Increments internal ID counter, adds todo to storage

#### get_all_todos() -> List[Todo]
**Purpose**: Retrieves all todo items currently in the system
**Parameters**: None
**Returns**: List of all Todo objects in storage, may be empty
**Exceptions**: None
**Side Effects**: None

#### get_todo_by_id(id: int) -> Todo
**Purpose**: Retrieves a specific todo item by its ID
**Parameters**:
- `id` (int): Unique identifier of the todo to retrieve (positive integer)
**Returns**: Todo object matching the provided ID
**Exceptions**:
- `ValueError`: If ID does not exist in storage
**Side Effects**: None

#### update_todo(id: int, title: str = None, description: str = None) -> Todo
**Purpose**: Updates an existing todo item's title and/or description
**Parameters**:
- `id` (int): Unique identifier of the todo to update
- `title` (str, optional): New title for the todo (if provided)
- `description` (str, optional): New description for the todo (if provided)
**Returns**: Updated Todo object
**Exceptions**:
- `ValueError`: If ID does not exist or if provided title is empty
**Side Effects**: Modifies existing todo in storage

#### delete_todo(id: int) -> bool
**Purpose**: Removes a todo item from the system by its ID
**Parameters**:
- `id` (int): Unique identifier of the todo to delete
**Returns**: True if todo was successfully deleted, False if ID did not exist
**Exceptions**: None
**Side Effects**: Removes todo from storage, may affect ID sequence

#### mark_complete(id: int, completed: bool = True) -> Todo
**Purpose**: Updates the completion status of a todo item
**Parameters**:
- `id` (int): Unique identifier of the todo to update
- `completed` (bool): New completion status (defaults to True)
**Returns**: Updated Todo object with new completion status
**Exceptions**:
- `ValueError`: If ID does not exist in storage
**Side Effects**: Modifies completion status of existing todo

## Storage Interface

#### get_storage_size() -> int
**Purpose**: Returns the count of todos currently in storage
**Parameters**: None
**Returns**: Number of todos in storage
**Exceptions**: None
**Side Effects**: None

#### clear_storage() -> None
**Purpose**: Removes all todos from storage (for testing/reset purposes)
**Parameters**: None
**Returns**: None
**Exceptions**: None
**Side Effects**: Empties entire storage, resets ID counter

## CLI Interface

#### display_menu() -> None
**Purpose**: Shows the main menu options to the user
**Parameters**: None
**Returns**: None
**Exceptions**: None
**Side Effects**: Prints menu to console

#### get_user_choice() -> int
**Purpose**: Prompts user for menu selection and validates input
**Parameters**: None
**Returns**: Valid menu option number selected by user
**Exceptions**:
- `ValueError`: If user input cannot be converted to valid menu option
**Side Effects**: Reads input from console

#### handle_add_todo_flow() -> None
**Purpose**: Manages the user interaction flow for adding a new todo
**Parameters**: None
**Returns**: None
**Exceptions**: May propagate exceptions from service layer
**Side Effects**: Calls service.add_todo(), displays result to user

#### handle_view_todos_flow() -> None
**Purpose**: Manages the user interaction flow for viewing all todos
**Parameters**: None
**Returns**: None
**Exceptions**: May propagate exceptions from service layer
**Side Effects**: Calls service.get_all_todos(), displays results to user

#### handle_update_todo_flow() -> None
**Purpose**: Manages the user interaction flow for updating a todo
**Parameters**: None
**Returns**: None
**Exceptions**: May propagate exceptions from service layer
**Side Effects**: Calls service.update_todo(), displays result to user

#### handle_delete_todo_flow() -> None
**Purpose**: Manages the user interaction flow for deleting a todo
**Parameters**: None
**Returns**: None
**Exceptions**: May propagate exceptions from service layer
**Side Effects**: Calls service.delete_todo(), displays result to user

#### handle_mark_complete_flow() -> None
**Purpose**: Manages the user interaction flow for marking a todo complete/incomplete
**Parameters**: None
**Returns**: None
**Exceptions**: May propagate exceptions from service layer
**Side Effects**: Calls service.mark_complete(), displays result to user