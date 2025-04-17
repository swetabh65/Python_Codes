import os
import shutil
import datetime

def backupfile_alongwith_timestamp(src_folder, dest_folder):
    for file_name in os.listdir(src_folder):
        src = os.path.join(src_folder, file_name)
        dest = os.path.join(dest_folder, file_name)
        
        
    if not os.path.isdir(src_folder):
        print(f"Error: Source directory '{src_folder}' does not exist.")
        return

    if not os.path.isdir(dest_folder):
        print(f"Error: Destination directory '{dest_folder}' does not exist.")
        return
        
    if os.path.isfile(dest):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            new_dest = os.path.join(dest_folder, timestamp + " - " + file_name)
            shutil.copy(src, new_dest)
            
    else:
            shutil.copy(src, dest)
            


if __name__ == "__main__":
    src_folder = r"C:\SwetabhData\DevOps_HeroVired\Python\Python_Assignment\Assignment Check"
    dest_folder = r"C:\SwetabhData\DevOps_HeroVired\Python\Python_Assignment\Backup"
    
    backupfile_alongwith_timestamp(src_folder, dest_folder)
    print(f"Backup has been taken successfully to the path '{dest_folder}'")