import os


def get_subdirs(directory):
    # print("Running...")
    print("Running...", {directory})
    previous_path = []
    path_list = []
    
    try:
        if directory == '/' or directory == 'C:/':
            previous_path.append(directory)
            path_list.append(directory)
        else:
            previous_path.append(directory+'/')
            path_list.append(directory+'/')
        os.chdir(directory)
    except FileNotFoundError:
        return
    except NotADirectoryError:
        return
    except PermissionError:
        return
    except OSError:
        print(f'The filename, directory name, or volume label syntax is incorrect: "{directory}"')
        return

    try:
        for item in os.listdir():
            if not os.path.isdir(item):
                continue
    ##        if item.startswith('.'):
    ##            continue
            subdirs = get_subdirs(item)

            if subdirs == None:
                continue

            if len(subdirs) > 0:
                for x in subdirs:
                    new = f'{previous_path[-1]}' + f'{x}'
                    path_list.append(new)
    except PermissionError:
        pass


    previous_path.pop(0)
    os.chdir('..')

    cleaned_path_list = []
    for item in path_list:
        cleaned_path_list.append(item.rstrip('/'))
    
    return cleaned_path_list


def dir_search(mydir, cleaned_path_list):
    flag = False

    try:
        for item in cleaned_path_list:
            if mydir in item:
                if item.find(mydir) != -1:
                    flag = True
                    print(f'Search results for "{mydir}" found in: ', item)
    except TypeError:
        pass

    if flag == False:
        print(f'No search results found for "{mydir}"')


directory = input("Enter path to search in. Example: ('./example/example_path'): ")
if directory.endswith(':'):
    directory = directory+'/'


mydir = input("Enter directory to search for: ")
path_list = get_subdirs(directory)
# print('PATH_LIST: ', path_list)
dir_search(mydir, path_list)

