from pathlib import Path
import json
import yaml

def discover_notes(notes_root: str):
    root = Path(notes_root)
    note_records = []

    for file in root.rglob("*.md"):
        relative_path = file.relative_to(root).as_posix()

        try:
            full_data = file.read_text(encoding="utf-8")
            parts = full_data.split("---", 2)

            if len(parts) < 3:
                raise ValueError(f"Invalid frontmatter in {relative_path}: expected opening and closing --- markers")

            # Ignore Part[0] as thats the empty space before the first ---
            raw_metadata = parts[1].strip()
            content = parts[2].strip()

            # YAML parsing
            yaml_string = raw_metadata
            loaded_metadata = yaml.safe_load(yaml_string)

            if not isinstance(loaded_metadata, dict):
                raise ValueError(f"Invalid frontmatter in {relative_path}: frontmatter is not formatted as dictionary")

            required_fields = ["id", "title", "date", "category", "tags", "summary", "status"]
            for k in required_fields:
                if k not in loaded_metadata.keys():
                    raise ValueError(f"Invalid frontmatter in {relative_path}: missing field {k}")

            # ---
            # example:
            # id: derivative-intuition
            # title: "Derivatives: From Average Change to Instantaneous Change"
            # date: 2026-04-16
            # category: calculus
            # tags: [derivatives, limits, rate-of-change]
            # summary: "Understanding derivatives as the transition from average change to instnataneous change"
            # status: draft
            # ---

            note_record = {
                "path": relative_path,
                "filename": file.name,
                "slug": file.stem,
                "id": loaded_metadata['id'],
                "title": loaded_metadata['title'],
                "date": str(loaded_metadata['date']),
                "category": loaded_metadata['category'],
                "tags": loaded_metadata['tags'],
                "summary": loaded_metadata['summary'],
                "status": loaded_metadata['status'],
                "content": content
            }

            note_records.append(note_record)

        except ValueError as e:
            print("discover_notes encountered an error..." + str(e))

    return note_records

def write_notes_json(notes, output_path: str):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def main():
    notes = discover_notes("data/content/notes")
    write_notes_json(notes, "data/generated/all-notes.json")

    # for note in notes:
    #     print(note)

if __name__ == "__main__":
    main()
