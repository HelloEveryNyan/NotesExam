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

    def edit_note(self, note_id, title, body):
        if 1 <= note_id <= len(self.notes):
            self.notes[note_id - 1]['title'] = title
            self.notes[note_id - 1]['body'] = body
            self.notes[note_id - 1]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_notes()
        else:
            print("Invalid note ID.")

    def delete_note(self, note_id):
        if 1 <= note_id <= len(self.notes):
            del self.notes[note_id - 1]
            self.save_notes()
        else:
            print("Invalid note ID.")

if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nOptions:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")

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
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter updated title: ")
            body = input("Enter updated body: ")
            app.edit_note(note_id, title, body)
            print("Note edited successfully.")

        elif choice == '4':
            note_id = int(input("Enter note ID to delete: "))
            app.delete_note(note_id)
            print("Note deleted successfully.")

        elif choice == '5':
            print("Exiting the Notes App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
