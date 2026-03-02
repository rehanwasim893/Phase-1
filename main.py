#!/usr/bin/env python3
"""
Entry point for the Todo application.
"""

from storage import InMemoryStorage
from service import TodoService
from cli import TodoCLI


def main():
    """
    Main application entry point.
    Initializes components and starts the CLI.
    """
    # Initialize the storage
    storage = InMemoryStorage()

    # Initialize the service with the storage
    service = TodoService(storage)

    # Initialize the CLI with the service
    cli = TodoCLI(service)

    # Start the application
    cli.run()


if __name__ == "__main__":
    main()