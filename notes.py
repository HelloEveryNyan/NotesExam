import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self, notes_file='notes.json'):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_notes(self):
        with open(self.notes_file, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, body):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'body': body,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }        