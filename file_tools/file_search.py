import os
from pathlib import Path

# ===== USER INPUT =====
search_type = input("Search type (1 = exact, 2 = partial): ").strip()
target = input("Enter file name or keyword: ").strip()
start_path = input("Enter directory path (press Enter for current): ").strip()

# Default path
if not start_path:
    start_path = "."

found = False

print("\nSearching...\n")

# ===== USING os.walk =====
for root, dirs, files in os.walk(start_path):
    for file in files:
        if (search_type == "1" and file == target) or \
           (search_type == "2" and target.lower() in file.lower()):
            
            print("Found (os):", os.path.join(root, file))
            found = True

# # ===== USING pathlib =====
# print("\nUsing pathlib...\n")

# if search_type == "1":
#     paths = Path(start_path).rglob(target)
# else:
#     paths = Path(start_path).rglob("*")

# for path in paths:
#     if search_type == "1" or (search_type == "2" and target.lower() in path.name.lower()):
#         print("Found (pathlib):", path)
#         found = True

# # ===== RESULT =====
# if not found:
#     print("No file found.")
# else:
#     print("\nSearch complete.")

