from pathlib import Path

# ===== USER INPUT =====
search_type = input("Search type (1 = exact, 2 = partial): ").strip()
target = input("Enter file or directory name or keyword: ").strip()
start_path = input("Enter directory path (press Enter for current): ").strip()

if not start_path:
    start_path = "."

stop_after_first = input("Stop after first match? (y/n): ").strip().lower() == 'y'

found = False

# ===== SEARCH =====
for path in Path(start_path).rglob("*"):  # search all files & dirs
    name = path.name
    match = False
    if search_type == "1" and name == target:
        match = True
    elif search_type == "2" and target.lower() in name.lower():
        match = True

    if match:
        type_name = "Directory" if path.is_dir() else "File"
        print(f"{type_name} found:", path)
        found = True
        if stop_after_first:
            break

# ===== RESULT =====
if not found:
    print("No file or directory found.")
else:
    print("\nSearch complete.")