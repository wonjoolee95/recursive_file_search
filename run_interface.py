


from pathlib import Path
import shutil

INTRO = '''
This program will do some interesting things,
    primarily searching & modifying files
    and folders of your computer.

Given a root directory, this program finds all files that:
    1. Match the name exactly
    2. End in a particular extension
    3. Exceed the given size in bytes
    

First, you need to provide a correct & valid
    root path to a directory.
    
    In Windows system, such directory will
    look something like: C:\Desktop or C:\Program Files

    In Mac, such directory will
    look something like: /Users/Won_Lee/Desktop

Plese enter your desired working root directory: 
'''

FIRST_MENU = '''
   How do you like to look for your files?
       1. Matching exact name
         (extension must be included; i.e. practice.txt)
       2. Ending in a particular extension
       3. Exceeding a specific size
       4. QUIT

   Choose and enter 1, 2, 3, or 4: '''

SECOND_MENU = '''
   What do you want to do with these files?
       1. Read the file (only for .txt files)
       2. Create a duplicate
       3. Touch the file
         (update the last modified timestamp)

   Choose and enter 1, 2, or 3: '''


def search_name(file_name: str, root_path: 'Path', data: list) -> list:
    '''
    runs a loop through the given root path recursively to find the
    matching name file
    '''
    for file in root_path.iterdir():
        if file.is_dir() == True:
            search_name(file_name, file, data)
        else:
            if file.name == file_name:
                data.append(file)
    return data
            

def search_extension(file_extension: str, root_path: 'Path', data: list) -> list:
    '''
    runs a loop through the given root path recursively to find the
    matching file extension
    '''
    for file in root_path.iterdir():
        if file.is_dir() == True:
            search_extension(file_extension, file, data)
        else:
            if file.suffix == file_extension:
                data.append(file)
    return data

def search_size(file_size: str, root_path: 'Path', data: list) -> list:
    '''
    runs a loop through the given root path recursively to find files
    that have greater size than the given size
    '''
    for file in root_path.iterdir():
        if file.is_dir() == True:
            search_size(file_size, file, data)
        else:
            if file.stat().st_size > int(file_size):
                data.append(file)
    return data

def read_file(file: 'Path') -> str:
    '''
    returns the first line of the text file
    '''
    text_file = file.open('r')
    return text_file.readline()[:-1]

def duplicate_file(file: 'Path') -> None:
    '''
    creates a .dup copy of the given file
    '''
    shutil.copy(str(file), str(file) + '.dup')
    
def touch_file(file: 'Path') -> None:
    '''
    "touches" the file (updates last modified time)
    '''
    file.touch(exist_ok = True)


def file_actions(file_paths: 'list of Path objects') -> None:
    '''
    given a list of file paths,
    performs "interesting" actions according to the given command
    '''
    if len(file_paths) == 0:
        print()
        print('   No such files were found.')
        print()
    else:
        print()
        print('   Following files were found:')
        for i in file_paths:
            print('     ' + str(i))
        print()
        command = input(SECOND_MENU)
        if command == '1':
            for file in file_paths:
                try:
                    print(file)
                    print(read_file(file))
                except:
                    print('   Error; the file could not be opened\n'
                          '   the files must be .txt files to be read')
                    print()
        elif command == '2':
            for file in file_paths:
                duplicate_file(file)
            print('   Duplicate(s) successfully created!')
            print()
        elif command == '3':
            for file in file_paths:
                touch_file(file)
            print('   File(s) successfully touched!')
            print()
        else:
            print('   Error; invalid command.')
            print()
            file_actions(file_paths)
                
                

def file_operations(root_path: 'Path') -> None:
    '''
    given a root path, calls appropriate functions to search for files
    '''
    print('   Your current root directory: ' + str(root_path))
    print(FIRST_MENU)
    data = []
    command = input('   ').split()
    if command[0] == '4':
        confirm = input('   You are about the quit the program.\n'
                        '   Are you sure? (yes/no): ')
        print()
        while confirm.lower().strip() not in ['yes', 'no']:
            confirm = input('   You are about the quit the program.\n'
                            '   Are you sure? (yes/no): ')
            print()
        if confirm.lower().strip() == 'no':
            file_operations(root_path)
    else:
        if command[0] == '1':
            print()
            file_name = input('   You selected the option to find files that\n'
                              '   matches a name exactly.\n'
                              '     Enter the name of the file: ')
            file_paths = search_name(file_name, root_path, data)
        elif command[0] == '2':
            file_ext = input('   You selected the option to find files that\n'
                             '   end in a particular extension.\n'
                             '     Enter the extension: ')
            if file_ext[0] == '.':
                file_paths = search_extension(file_ext, root_path, data)
            else:
                file_paths = search_extension('.' + file_ext, root_path, data)
        elif command[0] == '3':
            file_size = input('   You selected the option to ifnd files that\n'
                              '   exceed a certain size.\n'
                              '     Enter the size (only with numbers, in KB): ')
            file_paths = search_size(file_size, root_path, data)

        

        else:
            print('   Error; invalid command\n'
                  '   Please enter 1, 2, or 3.')
            print()
            file_operations(root_path)

        
        file_actions(file_paths)
        file_operations(root_path)
        
    
def ask_for_path() -> 'Path':
    '''
    asks for file and coverts the string to a Path object
    '''
    path = Path(input('    Path: '))
    return path

def run_user_interface() -> None:
    '''
    starts the program
    '''
    print(INTRO)
    while True:
        root_path = ask_for_path()
        if root_path.exists() == False:
            print()
            print(
                ' Error; invalid directory.\n'
                ' Please enter a valid directory: ')
            print()
        else:
            print()
            print('Root directory successfully set up!')
            print()
            break
    file_operations(root_path)
            


if __name__ == '__main__':
    run_user_interface()
    
