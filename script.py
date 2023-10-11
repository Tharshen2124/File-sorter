import os
import shutil

#! Searching for files based on extensions
# dir_path = "/Users/LENOVO/Downloads"
# extension = ".pdf"
# files = os.listdir(dir_path)
# pdf_files = [file for file in files if os.path.splitext(file)[1] == extension]
# print(pdf_files)

#! adding files to other directories
shutil.move("/Users/LENOVO/Downloads/Barcamp_poster.jpg", "/Users/LENOVO/Documents")

#! create folders to store files
# path = "/Users/LENOVO/Downloads/jamie"
# os.makedirs(path)