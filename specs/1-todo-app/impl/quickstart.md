# Quickstart Guide: Todo In-Memory Python Console Application

## Prerequisites

- Python 3.13 or higher
- UV package manager installed
- Basic command-line interface knowledge

## Setup Instructions

### 1. Environment Preparation
```bash
# Verify Python version
python --version

# Install UV package manager if not already installed
pip install uv
```

### 2. Project Initialization
```bash
# Navigate to project directory
cd path/to/project

# Initialize the project with UV
uv init
```

### 3. Running the Application
```bash
# Run the application directly with UV
uv run main.py

# Or if you have a virtual environment set up
python main.py
```

## Project Structure
```
todo-app/
├── main.py                 # Application entry point and main loop
├── cli.py                  # Command-line interface handling
├── service.py              # Business logic layer
├── models.py               # Data models (Todo class)
├── storage.py              # In-memory storage implementation
└── README.md               # Project documentation
```

## Basic Usage

### Starting the Application
1. Execute `uv run main.py` in your terminal
2. The main menu will appear with available options
3. Follow the prompts to manage your todos

### Available Operations
- **Add Todo**: Create a new todo with title and optional description
- **View Todos**: Display all todos with their status
- **Update Todo**: Modify an existing todo's title or description
- **Delete Todo**: Remove a todo from the list
- **Mark Complete/Incomplete**: Toggle completion status of a todo
- **Exit**: Quit the application

### Example Workflow
```
Welcome to the Todo App!
Choose an option:
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Complete/Incomplete
6. Exit

Enter your choice: 1
Enter todo title: Buy groceries
Enter description (optional): Need to buy milk, bread, eggs
Todo added successfully with ID: 1

Enter your choice: 2
ID: 1 | Title: Buy groceries | Completed: False
     Description: Need to buy milk, bread, eggs

Enter your choice: 5
Enter todo ID to mark: 1
Mark as (1) Complete or (2) Incomplete?: 1
Todo 1 marked as complete
```

## Development Commands

### Running Tests
```bash
# Currently manual testing; automated tests to be added in future phases
```

### Checking Code Quality
```bash
# Verify PEP8 compliance
python -m pycodestyle *.py
```

## Troubleshooting

### Common Issues
- **Python version error**: Ensure Python 3.13+ is installed and in PATH
- **UV not found**: Install UV with `pip install uv`
- **Import errors**: Verify all modules are in the same directory

### Error Messages
- **"Invalid title"**: Ensure title is not empty or just whitespace
- **"Todo not found"**: Verify the ID exists in the current list
- **"Invalid choice"**: Enter a number corresponding to a menu option

## Next Steps
- Explore the codebase to understand the layered architecture
- Review the service contracts to understand API boundaries
- Modify the application to add new features while maintaining clean architecture