from pathlib import Path

def discover_notes(notes_root: str):
    root = Path(notes_root)
    note_records = []

    for file in root.rglob("*.md"):
        note_record = {
            "path": str(file.relative_to(root)),
            "filename": file.name,
            "slug": file.stem,
            "category": file.parent.name
        }
        note_records.append(note_record)
    return note_records

def main():
    notes = discover_notes("data/content/notes")

    for note in notes:
        print(note)

if __name__ == "__main__":
    main()


