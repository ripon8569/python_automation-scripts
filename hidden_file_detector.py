import os
from pathlib import Path

def is_hidden(filepath):
    name = filepath.name

    # Linux / macOS: hidden files start with '.'
    if name.startswith('.'):
        return True

    # Windows: check file attributes
    try:
        import ctypes
        attrs = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))
        return attrs != -1 and (attrs & 2)  # FILE_ATTRIBUTE_HIDDEN = 2
    except:
        return False

def find_hidden_files(start_path):
    hidden_files = []
    hidden_dirs = []

    for root, dirs, files in os.walk(start_path):
        root_path = Path(root)

        # Check directories
        for d in dirs:
            dir_path = root_path / d
            if is_hidden(dir_path):
                hidden_dirs.append(dir_path)

        # Check files
        for f in files:
            file_path = root_path / f
            if is_hidden(file_path):
                hidden_files.append(file_path)

    return hidden_files, hidden_dirs


if __name__ == "__main__":
    start_path = input("Enter directory path (press Enter for current): ").strip()
    if not start_path:
        start_path = "."

    start_path = Path(start_path)

    if not start_path.exists():
        print("Invalid path!")
        exit()

    print(f"\nScanning: {start_path.resolve()}\n")

    files, dirs = find_hidden_files(start_path)

    print("=== Hidden Files ===")
    for f in files:
        print(f)

    print("\n=== Hidden Directories ===")
    for d in dirs:
        print(d)

    print(f"\nTotal Hidden Files: {len(files)}")
    print(f"Total Hidden Directories: {len(dirs)}")