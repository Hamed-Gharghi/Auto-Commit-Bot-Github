import os
import subprocess
from datetime import datetime
import time
import re

# Author: Hamed Gharghi
# Date: 2024-08-04
# Description: This script automatically commits and pushes a placeholder Python script to a GitHub repository every 24 hours.

# Configuration
REPO_PATH = 'D:\\Code\\Python\\Daily-Python\\Daily-Python'
FILE_NAME = 'auto_generated_script.py'
GITHUB_USERNAME = 'Hamed-Gharghi'
GITHUB_TOKEN = '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'  # Use your actual token

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', filename)

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def make_commit():
    os.chdir(REPO_PATH)

    # Define placeholder content
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = f"""\
# Author: Hamed Gharghi
# Date: {timestamp}
# Description: This script is an auto-generated placeholder.

print("This is an auto-generated Python script.")
"""
    file_path = os.path.join(REPO_PATH, FILE_NAME)

    # Write placeholder code to file
    write_file(file_path, code)

    try:
        # Add changes to git
        subprocess.run(['git', 'add', FILE_NAME], check=True)

        # Commit changes
        commit_message = f'Automated commit: Added {FILE_NAME} with a placeholder content'
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        # Configure Git to use token for this repository
        subprocess.run(['git', 'remote', 'set-url', 'origin',
                        f'https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/Hamed-Gharghi/Daily-Python.git'], check=True)

        # Push changes to GitHub
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

if __name__ == "__main__":
    while True:
        os.system("cls")
        make_commit()
        time.sleep(60)  # Sleep for 24 hours

