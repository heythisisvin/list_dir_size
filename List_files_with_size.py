import os
from pathlib import Path
#punta sa directory c
#list lahat ng files kasama file size
#sort the top 50 big size
#show the the result of the paths

p = Path.home()
list_files1 = Path(p)
#for list_file_iterate in list_files:
#    print(list_file_iterate)

for item_path in list_files1.rglob("*"):
    print(item_path)

print(p)

