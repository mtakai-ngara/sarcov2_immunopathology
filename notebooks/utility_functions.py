import os, re



def get_list_of_specific_file_type(directory, file_pattern):
    '''Returns a list of certain file types given a directory and a pattern matching the file e.g its extension'''
    all_files = get_all_files_in_directory(directory);
    pattern=re.compile(file_pattern)
    specific_file_list = [];
    for current_file in all_files:
        if pattern.search(string=current_file)==None : continue
        specific_file_list.append(current_file)
    return specific_file_list

def get_all_files_in_directory(directory):
    '''Returns a list of all files plus their full directory path's  in root plus the intermediate directories '''
    all_dirs = []
    all_files = []
    for (root, dirs, filenames) in os.walk(directory):
        all_dirs.append(root)
    for d in all_dirs:
        [all_files.append(d + '/' + f) for f in os.listdir(d)]
    return all_files

def safe_mkdir(path):
    '''Makes directory in safe manner and if the intermediary folders are missing, creates them too'''
    if not os.path.exists(path):
        os.makedirs(path,mode=0o777);
    else:
        print('Directory already exists')
        pass
    pass


