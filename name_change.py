import os

def rename_files(directory, base_name):
    # Change the current working directory to the specified directory
    os.chdir(directory)
    
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Sort the files in case they need to be renamed in order
    files.sort()
    
    # Loop through each file and rename it
    for i, filename in enumerate(files, start=1):
        # Get the file extension
        extension = os.path.splitext(filename)[1]
        
        # Construct the new filename
        new_name = f"{i} {base_name}{extension}"
        
        # Rename the file
        os.rename(filename, new_name)
    
    print("Files have been renamed successfully.")

# Example usage
directory = "C:/Users/shadd/Music/vioce_clone_stock"
base_name = "wav"
rename_files(directory, base_name)


# "C:/Users/shadd/Music/vioce_clone_stock"