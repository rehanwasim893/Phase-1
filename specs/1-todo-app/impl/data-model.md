# Data Model: Todo In-Memory Python Console Application

## Todo Entity

### Attributes
- **id** (int): Unique identifier for each todo item
  - Type: Integer
  - Constraints: Positive integer, auto-generated
  - Required: Yes
  - Description: Sequential identifier assigned when todo is created

- **title** (str): Title of the todo item
  - Type: String
  - Constraints: Minimum 1 character, not empty or whitespace-only
  - Required: Yes
  - Description: Main description of the task to be completed

- **description** (str, optional): Additional details about the todo
  - Type: String
  - Constraints: Optional field, can be empty
  - Required: No
  - Description: Extended information about the task

- **completed** (bool): Completion status of the todo
  - Type: Boolean
  - Constraints: True (completed) or False (incomplete)
  - Required: Yes
  - Default Value: False
  - Description: Indicates whether the task has been completed

## Validation Rules

### Title Validation
- Must not be empty
- Must not contain only whitespace characters
- Must be at least 1 non-whitespace character
- Maximum length: 255 characters (to prevent excessively long titles)

### ID Validation
- Must be a positive integer
- Auto-generated when new todo is created
- Must be unique within the system
- Cannot be modified after creation

### Completed Status Validation
- Must be a boolean value (True or False)
- Only valid values are True (completed) or False (incomplete)

## State Transitions

### Completion States
- **Initial State**: `completed = False`
  - Set when a new todo is created
  - Represents an incomplete task

- **Transition 1**: `incomplete` → `complete`
  - Trigger: User marks todo as complete
  - Action: Set `completed = True`
  - Result: Todo is marked as completed

- **Transition 2**: `complete` → `incomplete`
  - Trigger: User marks todo as incomplete
  - Action: Set `completed = False`
  - Result: Todo is marked as incomplete again

## Relationships

### Within System
- Each Todo entity exists independently
- No direct relationships between different Todo items
- All Todos are stored in a single collection (list/dictionary)

## Data Lifecycle

### Creation
1. User provides title and optional description
2. System validates title (not empty)
3. System assigns auto-incremented ID
4. System sets completed status to False
5. Todo is added to storage

### Retrieval
1. System provides access to all todos or specific todo by ID
2. Data is retrieved from in-memory storage
3. No transformation required for display

### Update
1. User specifies ID of todo to update
2. System validates ID exists
3. System allows updating title and description (not ID or creation status)
4. System maintains completion status unless explicitly changed

### Deletion
1. User specifies ID of todo to delete
2. System validates ID exists
3. System removes todo from storage
4. Operation is irreversible

## Constraints

### Data Integrity
- ID uniqueness: Each todo must have a unique ID
- Title non-empty: Title must contain at least one non-whitespace character
- Type safety: All attributes must maintain their defined types

### Performance
- In-memory storage: All operations should be efficient
- No external dependencies: All data operations use built-in Python structures