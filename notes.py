import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self, notes_file='notes.json'):
        self.notes_file = notes_file
        self.notes = self.load_notes()