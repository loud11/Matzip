from os import walk

def get_file_path(): # get file pathes and return pathes
    f = []
    all_file_path = []
    input_mypath = input("enter path : ")
    input_mypath.replace("\\","/")
    for (dirpath, dirnames, filenames) in walk(input_mypath):
        f.extend(filenames)
        print(dirpath , dirnames , filenames)
        for files in filenames:
            all_file_path.append(dirpath+files)

        print("loop dist")
    return all_file_path
