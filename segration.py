import os
import shutil

from_dir = "C:/Users/sahil/OneDrive/Desktop/Home"
to_dir = "C:/Users/sahil/OneDrive/Desktop/Destination"

list_of_files = os.listdir(from_dir)

print("List of files in the source directory:")
for file_name in list_of_files:
    print(file_name)

for file_name in list_of_files:
    file_ext = os.path.splitext(file_name)[1]
    
    from_file = os.path.join(from_dir, file_name)
    to_file = os.path.join(to_dir, file_name)
    
    shutil.move(from_file, to_file)

print("All files have been moved to the destination directory.")
