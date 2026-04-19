from pathlib import Path
import json

def discover_notes(notes_root: str):
    root = Path(notes_root)
    note_records = []

    for file in root.rglob("*.md"):
        note_record = {
            "path": file.relative_to(root).as_posix(),
            "filename": file.name,
            "slug": file.stem,
            "category": file.parent.name
        }
        note_records.append(note_record)

    return note_records

def write_notes_json(notes, output_path: str):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def main():
    notes = discover_notes("data/content/notes")
    write_notes_json(notes, "data/generated/all-notes.json")

    for note in notes:
        print(note)

if __name__ == "__main__":
    main()
