import os
import shutil

print("Type the directory you would like to sort your files in\n")

user_dir_path = input("Directory:")
files = os.listdir(user_dir_path)

print("Categories for sorting:\n")
print("[1] pdf\n")
print("[2] jpg\n")
print("[3] png\n")
print("[4] svg\n")
print("[5] docx\n")
print("[6] pptx\n")
print("[7] All\n")

num = int(input("Select number: "))

ext = []
extensions = []

if num==1:
    extensions = [".pdf"]
if num==2:
    extensions = [".jpg"]
if num==3:
    extensions = [".png"]
if num==4:
    extensions = [".svg"]
if num==5:
    extensions = [".docx"]
if num==6:
    extensions = [".pptx"]
if num==7:
    extensions = [".jpg", ".docx", ".pdf", ".png", ".svg", ".docx", ".pptx"]

for extension in extensions:
    files_type = [file for file in files if os.path.splitext(file)[1] == extension]
    dir_path = user_dir_path+extension;
    print("\n\nCreated directory for "+dir_path+"\n")
    os.makedirs(dir_path)
    
    for file_type in files_type:
        file_path = user_dir_path+file_type;
        print(file_path)
        shutil.move(file_path, dir_path)