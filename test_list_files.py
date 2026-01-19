from pathlib import Path
from openpyxl import Workbook

#current_directory = Path(".")  # current directory
directory_path = Path.home()

wb = Workbook()
ws= wb.active
#function for length

files = []
for file in directory_path.rglob("*"):
    if file.is_file():
        try:
            files.append({
                "Name": file.name,
                "Length": file.stat().st_size,
                "Fullname": str(file.resolve())
            })
        except (PermissionError, FileNotFoundError):
            pass  # skip inaccessible files

# Sort by file size (descending)
files_sorted = sorted(files, key=lambda x: x["Length"], reverse=True)

# Get top 20
top_20 = files_sorted[:20]

# Display
def result_value():
    for f in top_20:
        resultvalue = str(f"{f['Name']}\t{f['Length']}\t{f['Fullname']}")
        ws.append([resultvalue])
    return resultvalue

ws.append([result_value()])
wb.save("result1.xlsx")
