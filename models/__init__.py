#!/usr/bin/python3
"""
This module initializes the file storage system by creating an instance of FileStorage
and reloading any existing data from the file system into the application.
"""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage to handle data persistence.
storage = FileStorage()

# Load existing data from storage into the application.
storage.reload()