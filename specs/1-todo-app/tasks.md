# Tasks: Todo In-Memory Python Console Application

## Feature Overview
A simple in-memory todo console application designed for beginner Python developers and students learning CLI apps and clean code. The application provides basic todo management functionality through a command-line interface without requiring any external databases or frameworks.

## Implementation Strategy
- **MVP First**: Implement User Story 1 (Add Todo) as the minimum viable product
- **Incremental Delivery**: Build each user story as a complete, independently testable increment
- **Clean Architecture**: Maintain clear separation between CLI, service, and model layers
- **PEP8 Compliant**: Follow Python coding standards throughout implementation

## Dependencies
- Python 3.13+
- UV package manager
- Standard Python libraries only

## User Stories Priority Order
1. **US1**: Add new todo with title and optional description
2. **US2**: View all todos with status and details
3. **US3**: Update existing todo title and/or description
4. **US4**: Delete a specific todo by identifier
5. **US5**: Mark a todo as complete/incomplete

## Phase 1: Setup
**Goal**: Establish project structure and foundational components

- [X] T001 Create project directory structure with src/ folder
- [X] T002 Initialize project with UV package manager
- [X] T003 [P] Create models.py file for data models
- [X] T004 [P] Create storage.py file for in-memory storage
- [X] T005 [P] Create service.py file for business logic
- [X] T006 [P] Create cli.py file for user interface
- [X] T007 [P] Create main.py file as application entry point
- [X] T008 Create README.md with project documentation

## Phase 2: Foundational Components
**Goal**: Implement core components that all user stories depend on

- [X] T009 Define Todo data model class in models.py with id, title, description, completed attributes
- [X] T010 Implement Todo model validation methods for title and ID constraints
- [X] T011 Create in-memory storage class in storage.py with list/dict for todos
- [X] T012 Implement storage methods: add, get_all, get_by_id, update, delete
- [X] T013 Create TodoService class in service.py with core operations
- [X] T014 Implement service validation for input parameters
- [X] T015 Set up basic CLI menu structure in cli.py with option display
- [X] T016 Create main application loop in main.py with menu navigation

## Phase 3: [US1] Add New Todo
**Goal**: Enable users to add new todos with title and optional description

**Independent Test Criteria**: User can add a new todo with a valid title and optional description, see confirmation, and verify it appears in the todo list.

- [X] T017 [US1] Implement add_todo method in TodoService with validation
- [X] T018 [US1] Implement storage add method with auto-incrementing ID
- [X] T019 [US1] Create handle_add_todo_flow in cli.py with user input prompts
- [X] T020 [US1] Add "Add Todo" option to main menu in cli.py
- [X] T021 [US1] Implement input validation for title (non-empty requirement)
- [X] T022 [US1] Add error handling for invalid input in CLI layer
- [X] T023 [US1] Test add functionality with valid title and description
- [X] T024 [US1] Test add functionality with empty title (should fail validation)

## Phase 4: [US2] View All Todos
**Goal**: Enable users to view all todos with their status and details

**Independent Test Criteria**: User can view all todos with their ID, title, description, and completion status in a clear, readable format.

- [X] T025 [US2] Implement get_all_todos method in TodoService
- [X] T026 [US2] Implement get_all method in storage layer
- [X] T027 [US2] Create handle_view_todos_flow in cli.py with display formatting
- [X] T028 [US2] Add "View Todos" option to main menu in cli.py
- [X] T029 [US2] Implement display formatting for todos with clear status indicators
- [X] T030 [US2] Add handling for empty todo list scenario
- [X] T031 [US2] Test view functionality with multiple todos (mixed completion status)
- [X] T032 [US2] Test view functionality with empty todo list

## Phase 5: [US3] Update Existing Todo
**Goal**: Enable users to update the title and/or description of existing todos

**Independent Test Criteria**: User can select an existing todo by ID and update its title and/or description while preserving other attributes.

- [X] T033 [US3] Implement update_todo method in TodoService with validation
- [X] T034 [US3] Implement update method in storage layer
- [X] T035 [US3] Create handle_update_todo_flow in cli.py with selection and update prompts
- [X] T036 [US3] Add "Update Todo" option to main menu in cli.py
- [X] T037 [US3] Implement validation to prevent empty titles after update
- [X] T038 [US3] Add error handling for non-existent todo IDs
- [X] T039 [US3] Test update functionality with valid changes
- [X] T040 [US3] Test update functionality with invalid ID (should fail gracefully)

## Phase 6: [US4] Delete Todo
**Goal**: Enable users to delete specific todos by identifier

**Independent Test Criteria**: User can select a todo by ID and remove it from the system with confirmation.

- [X] T041 [US4] Implement delete_todo method in TodoService
- [X] T042 [US4] Implement delete method in storage layer
- [X] T043 [US4] Create handle_delete_todo_flow in cli.py with confirmation prompts
- [X] T044 [US4] Add "Delete Todo" option to main menu in cli.py
- [X] T045 [US4] Implement confirmation mechanism to prevent accidental deletions
- [X] T046 [US4] Add error handling for non-existent todo IDs
- [X] T047 [US4] Test delete functionality with valid ID
- [X] T048 [US4] Test delete functionality with invalid ID (should fail gracefully)

## Phase 7: [US5] Mark Complete/Incomplete
**Goal**: Enable users to toggle the completion status of todos

**Independent Test Criteria**: User can select a todo by ID and toggle its completion status between complete and incomplete.

- [X] T049 [US5] Implement mark_complete method in TodoService
- [X] T050 [US5] Implement update method in storage layer for status changes
- [X] T051 [US5] Create handle_mark_complete_flow in cli.py with status toggle prompts
- [X] T052 [US5] Add "Mark Complete/Incomplete" option to main menu in cli.py
- [X] T053 [US5] Implement logic to toggle completion status
- [X] T054 [US5] Add error handling for non-existent todo IDs
- [X] T055 [US5] Test mark complete functionality
- [X] T056 [US5] Test mark incomplete functionality

## Phase 8: Polish & Cross-Cutting Concerns
**Goal**: Enhance the application with error handling, validation, and user experience improvements

- [X] T057 Implement comprehensive error handling across all layers
- [X] T058 Add input sanitization and validation throughout CLI layer
- [X] T059 Improve error messages to be user-friendly
- [X] T060 Add graceful handling of edge cases (empty lists, invalid input)
- [X] T061 Implement consistent formatting for all CLI output
- [X] T062 Add application exit confirmation
- [X] T063 Conduct full integration testing of all features
- [X] T064 Perform PEP8 compliance check and fix any issues
- [X] T065 Update README.md with usage instructions and feature documentation
- [X] T066 Test complete user workflows from start to finish

## Parallel Execution Opportunities
- **Tasks T003-T007**: All module files can be created in parallel during setup phase
- **Service and storage development**: Can be developed in parallel after models are defined
- **Individual user story implementations**: Each US can be developed independently after foundational components are in place

## MVP Scope (Minimum Viable Product)
- Tasks T001-T024: Setup, foundational components, and add todo functionality
- This enables the core use case of adding todos and forms the basis for all other features