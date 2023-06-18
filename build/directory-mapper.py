import os

def print_tree(root_dir, padding='', print_files=False, file=None):
    # Write the root directory to the text file
    file.write(padding[:-1] + '+--' + os.path.basename(root_dir) + '/\n')

    # Get the list of files and directories in the current directory
    files = []
    dirs = []
    for file in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, file)):
            files.append(file)
        elif os.path.isdir(os.path.join(root_dir, file)):
            dirs.append(file)

    # Write the files in the current directory to the text file
    if print_files:
        for file in files:
            file.write(padding + '   |--' + file + '\n')

    # Recursively write the subdirectories to the text file
    for dir in dirs:
        print_tree(os.path.join(root_dir, dir), padding + '   |', print_files, file)

# Prompt the user to enter the network shared folder path
folder_path = input('Enter the network shared folder path: ')

# Check if the folder path exists
if not os.path.exists(folder_path):
    print(f'The folder path {folder_path} does not exist.')
else:
    # Display a message while the script is running
    print('Mapping folder... do not open the text file')

    # Open a text file for writing the list of folders, subfolders, and files
    with open('file_list.txt', 'w') as file:
        # Loop through all subdirectories and files in the folder
        for dirpath, dirnames, filenames in os.walk(folder_path):
            # Get the relative path of the current directory
            rel_path = os.path.relpath(dirpath, folder_path)

            # Count the number of subdirectories in the relative path
            depth = rel_path.count(os.sep)

            # Write the current directory path to the text file
            file.write(f'{"    " * depth}{os.path.basename(dirpath)}/\n')

            # Write the list of files to the text file
            for filename in filenames:
                file.write(f'{"    " * (depth + 1)}{filename}\n')

            # Print a progress message
            print(f'Processed {dirpath}')

        # Write the directory structure in the ASCII art format to the text file
        print_tree(folder_path, print_files=True, file=file)

    # Display a message when the script is finished
    print('The list of folders, subfolders, and files has been saved to file_list.txt.')

    # Auto-close the console window
    input('Press enter to exit.')