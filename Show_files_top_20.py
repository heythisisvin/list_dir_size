from pathlib import Path

#current_directory = Path(".")  # current directory
directory_path = Path.home()

#function for length

files = []
for file in directory_path.rglob("*"):
    if file.is_file():
        try:
            files.append({
                "Name": file.name,
                "Length": file.stat().st_size / (1024*1024),
                "Fullname": str(file.resolve())
            })
        except (PermissionError, FileNotFoundError):
            pass  # skip inaccessible files

# Sort by file size (descending)
files_sorted = sorted(files, key=lambda x: x["Length"], reverse=True)

# Get top 20
top_20 = files_sorted[:20]

# Display
for f in top_20:
    print(f"{f['Name']}\t{f['Length']}\t{f['Fullname']}")




