from difflib import Differ
import os

file_folder1 ="C:/Users/24547/Git/nelnet-cisco-ivr/FMS_Velocity_IVR_Java_ph/src/com/fms/velocity/auth"
file_folder_2 = "C:/Users/24547\Git/nelnet-cisco-ivr/FMS_Velocity_IVR_Java/src/com/fms/velocity/auth"

for filename in os.listdir(file_folder1):
    file1 = os.path.join(file_folder1, filename)
    file2 = os.path.join(file_folder_2, filename)
    fileNameSplit = filename.split(".")
    print(file1)
    print(file2)
    if os.path.exists(file2):
        with open(file1) as file_1, open(file2) as file_2:
            differ = Differ()
            for line in differ.compare(file_1.readlines(), file_2.readlines()):
                #apped the diff to a file
                if line.startswith('-'):
                    with open(f"diff/{fileNameSplit[0]}_diff.txt", "a") as diff_file:
                        diff_file.write(line)
                
    else:
        print(f"{file2} does not exist, skipping...")

    """
    Code	Meaning
    ‘-‘     line unique to sequence 1
    ‘+’     line unique to sequence 2
    ‘ ‘     line common to both sequences
    ‘?’     line not present in either input sequence   
    """
