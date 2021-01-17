import zipfile
import tarfile,fnmatch,os
def unzip():
    rootPath = r"C:\Users\13033\Downloads"
    pattern = '*.tgz'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))
            tarfile.open(os.path.join(root, filename)).extractall(os.path.join(root, filename.split(".")[0]))


unzip()