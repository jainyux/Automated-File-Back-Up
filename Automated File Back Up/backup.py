import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\mjainy\OneDrive - Digicorner\Pictures\Time cards"
destination_dir = r"C:\Users\mjainy\OneDrive - Digicorner\Desktop\Python1\Back Up"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")
schedule.every().day.at("14:43").do(lambda: copy_folder_to_directory(source_dir, destination_dir))       


while True:
    schedule.run_pending()
    time.sleep(60)