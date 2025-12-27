import os
import re

for root, dirs, files in os.walk("."):
    for file in files:
        old_path = os.path.join(root, file)
        new_file = re.sub(r"\d\d\.1", "easy", file)
        new_file = re.sub(r"\d\d\.2", "medium", new_file)
        new_file = re.sub(r"\d\d\.3", "hard", new_file)

        new_file = new_file.replace("_sol", "_solution")
        new_file = new_file.replace("_icon", "_screenshot-orig")

        new_path = os.path.join(root, new_file)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")
