import os
import shutil
import datetime
import time
from pathlib import Path

# Auto-detect YOUR folders
home = Path.home()
source_dir = home / "Pictures" / "Screenshots"
destination_dir = home / "Desktop" / "Backups"

BACKUP_TIME = "18:57"  # Change your time here

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        if not os.path.exists(source):
            print(f"Source not found: {source}")
            return
            
        shutil.copytree(source, dest_dir)
        print(f"[{datetime.datetime.now()}] Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"[{today}] Backup already exists: {dest_dir}")
    except Exception as e:
        print(f"Error: {e}")

os.makedirs(destination_dir, exist_ok=True)

print("--- Auto Backup Started (No schedule module) ---")
print(f"From: {source_dir}")
print(f"To: {destination_dir}")
print(f"Will backup daily at {BACKUP_TIME}")
print("Keep this window open...\n")

last_backup_date = None

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    today = now.date()

    # If current time matches backup time and we haven't backed up today
    if current_time == BACKUP_TIME and last_backup_date != today:
        print(f"\nTime matched! Starting backup at {current_time}...")
        copy_folder_to_directory(source_dir, destination_dir)
        last_backup_date = today
        print("Going back to sleep for today...\n")

    # Check every 30 seconds so we don't miss the minute
    time.sleep(30)