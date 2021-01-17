import zipfile
import tarfile,fnmatch,os
def unzip():
    with zipfile.ZipFile("C://Users//13033//Downloads//kafka_2.13-2.7.0.tgz", 'r') as zip_ref:
      zip_ref.extractall("C://Users//13033//Desktop//Test")

unzip()