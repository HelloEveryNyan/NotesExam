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
                
    self.notes.append(note)
    self.save_notes()

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(f"{note['id']}. {note['title']} - {note['timestamp']}")

if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nOptions:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            app.add_note(title, body)
            print("Note added successfully.")

        elif choice == '2':
            print("\nAll Notes:")
            app.view_notes()

        elif choice == '3':
            print("Exiting the Notes App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")