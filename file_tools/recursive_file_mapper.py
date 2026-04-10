import os
import json
from pathlib import Path
from datetime import datetime

def get_file_info(path):
    try:
        stat = path.stat()
        return {
            "name": path.name,
            "path": str(path.resolve()),
            "type": "directory" if path.is_dir() else "file",
            "size": stat.st_size,
            "permissions": oct(stat.st_mode)[-3:],
            "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "hidden": path.name.startswith(".")
        }
    except Exception as e:
        return {
            "name": path.name,
            "error": str(e)
        }

def recursive_map(start_path):
    result = []

    for root, dirs, files in os.walk(start_path):
        root_path = Path(root)

        # Add directory itself
        result.append(get_file_info(root_path))

        # Add subdirectories
        for d in dirs:
            dir_path = root_path / d
            result.append(get_file_info(dir_path))

        # Add files
        for f in files:
            file_path = root_path / f
            result.append(get_file_info(file_path))

    return result

def save_to_json(data, output_file="file_map.json"):
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"[+] Saved results to {output_file}")
    except Exception as e:
        print(f"[!] Error saving JSON: {e}")

def main():
    print("=== Recursive File Mapper ===")

    start_path = input("Enter directory path (press Enter for current): ").strip()
    if not start_path:
        start_path = "."

    if not os.path.exists(start_path):
        print("[!] Path does not exist.")
        return

    print(f"[+] Scanning: {start_path} ...")

    data = recursive_map(start_path)

    print(f"[+] Total items found: {len(data)}")

    save_option = input("Save output to JSON? (y/n): ").lower()
    if save_option == "y":
        output_file = input("Enter output file name (default: file_map.json): ").strip()
        if not output_file:
            output_file = "file_map.json"
        save_to_json(data, output_file)

    # Quick preview
    print("\n--- Sample Output ---")
    for item in data[:10]:
        print(item)

if __name__ == "__main__":
    main()