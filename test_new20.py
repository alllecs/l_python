import os
import os.path
import shutil

print(os.getcwd()) #what is this directory
print(os.listdir("name_directory")) #what is in directory

print(os.path.exists("file.py")) #does the file exist True of False
print(os.path.exists("name_directory")) #does the file exist True of False

print(os.path.isfile("files.py")) 
print(os.path.isfile("name_directory"))

print(os.path.isdir("files.py")) 
print(os.path.isdir("name_directory"))

print(os.path.abdpath("files.py")) #absolute path

os.chdir("name_directory") #change dir

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)

shutil.copy("tests/test1.txt", "tests/test2.txt") #copy files
shutil.copytree("tests", "tests/tests2") #copy dir

