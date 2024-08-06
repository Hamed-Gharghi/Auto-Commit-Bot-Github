"""
Author: Hamed Gharghi
Date: 2024-08-06
Description: This script is a PyQt5 application that provides a user interface for an auto-commit bot.
The bot automatically commits changes to a GitHub repository at regular intervals.
Features include setting repository path, GitHub credentials, file name, and sleep time. It also
includes a tutorial for obtaining a GitHub Personal Access Token and supports starting and stopping
the bot.
"""

import sys
import os
import subprocess
from datetime import datetime
import time
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QSpinBox, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMutex, QMutexLocker
from PyQt5.QtGui import QPalette, QColor, QIcon


# Function to sanitize filenames
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', filename)


# Function to write file content
def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


# Worker thread to handle the Git operations
class CommitThread(QThread):
    log_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, repo_path, github_username, github_token, file_name, sleep_time):
        super().__init__()
        self.repo_path = repo_path
        self.github_username = github_username
        self.github_token = github_token
        self.file_name = file_name
        self.sleep_time = sleep_time
        self._running = True
        self.mutex = QMutex()

    def run(self):
        while self.is_running():
            self.make_commit()
            self.log_signal.emit(f"Commit made at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            for _ in range(self.sleep_time * 60):
                time.sleep(1)
                if not self.is_running():
                    self.log_signal.emit("Auto Commit Bot stopped.")
                    self.finished_signal.emit()
                    return

        self.finished_signal.emit()

    def make_commit(self):
        os.chdir(self.repo_path)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        code = f"""\
# Author: {self.github_username}
# Date: {timestamp}
# Description: This script is an auto-generated placeholder.

print("This is an auto-generated Python script.")
"""
        file_path = os.path.join(self.repo_path, self.file_name)
        write_file(file_path, code)

        subprocess.run(['git', 'add', self.file_name], check=True)
        commit_message = f'Automated commit: Added {self.file_name} with a placeholder content'
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)

    def stop(self):
        with QMutexLocker(self.mutex):
            self._running = False

    def is_running(self):
        with QMutexLocker(self.mutex):
            return self._running


# Main window for the application
class AutoCommitBotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.apply_earthy_theme()  # Apply the Earthy theme
        self.setWindowIcon(QIcon('icon.png'))  # Set the application icon

    def init_ui(self):
        self.setWindowTitle('Auto Commit Bot')

        layout = QVBoxLayout()

        # Repository Path
        repo_layout = QHBoxLayout()
        self.repo_label = QLabel('Repository Path:')
        self.repo_path_edit = QLineEdit()
        self.repo_browse_button = QPushButton('Browse')
        self.repo_browse_button.clicked.connect(self.browse_repo)
        repo_layout.addWidget(self.repo_label)
        repo_layout.addWidget(self.repo_path_edit)
        repo_layout.addWidget(self.repo_browse_button)
        layout.addLayout(repo_layout)

        # GitHub Username
        username_layout = QHBoxLayout()
        self.username_label = QLabel('GitHub Username:')
        self.username_edit = QLineEdit()
        username_layout.addWidget(self.username_label)
        username_layout.addWidget(self.username_edit)
        layout.addLayout(username_layout)

        # GitHub Token
        token_layout = QHBoxLayout()
        self.token_label = QLabel('GitHub Token:')
        self.token_edit = QLineEdit()
        self.token_edit.setEchoMode(QLineEdit.Password)  # Hide the token
        self.token_help_button = QPushButton('How to get GitHub Token?')
        self.token_help_button.clicked.connect(self.show_token_tutorial)
        token_layout.addWidget(self.token_label)
        token_layout.addWidget(self.token_edit)
        token_layout.addWidget(self.token_help_button)
        layout.addLayout(token_layout)

        # File Name
        filename_layout = QHBoxLayout()
        self.filename_label = QLabel('File Name:')
        self.filename_edit = QLineEdit()
        filename_layout.addWidget(self.filename_label)
        filename_layout.addWidget(self.filename_edit)
        layout.addLayout(filename_layout)

        # Sleep Time
        sleep_layout = QHBoxLayout()
        self.sleep_label = QLabel('Sleep Time (minutes):')
        self.sleep_spinbox = QSpinBox()
        self.sleep_spinbox.setMinimum(1)  # Minimum of 1 minute
        self.sleep_spinbox.setMaximum(1440)  # Maximum of 1440 minutes (24 hours)
        self.sleep_spinbox.setValue(1440)  # Default to 1440 minutes (24 hours)
        sleep_layout.addWidget(self.sleep_label)
        sleep_layout.addWidget(self.sleep_spinbox)
        layout.addLayout(sleep_layout)

        # Start Button
        self.start_button = QPushButton('Start Auto Commit Bot')
        self.start_button.clicked.connect(self.start_commit_bot)
        layout.addWidget(self.start_button)

        # Stop Button
        self.stop_button = QPushButton('Stop Auto Commit Bot')
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_commit_bot)
        layout.addWidget(self.stop_button)

        # Log Label
        self.log_label = QLabel('')
        layout.addWidget(self.log_label)

        self.setLayout(layout)

    def browse_repo(self):
        repo_path = QFileDialog.getExistingDirectory(self, 'Select Repository Directory')
        if repo_path:
            self.repo_path_edit.setText(repo_path)

    def start_commit_bot(self):
        repo_path = self.repo_path_edit.text()
        github_username = self.username_edit.text()
        github_token = self.token_edit.text()
        file_name = self.filename_edit.text()
        sleep_time = self.sleep_spinbox.value()

        if not all([repo_path, github_username, github_token, file_name]):
            self.log_label.setText('Please fill in all fields.')
            return

        self.commit_thread = CommitThread(repo_path, github_username, github_token, file_name, sleep_time)
        self.commit_thread.log_signal.connect(self.update_log)
        self.commit_thread.finished_signal.connect(self.on_commit_thread_finished)
        self.commit_thread.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.log_label.setText('Auto Commit Bot started...')

    def stop_commit_bot(self):
        if self.commit_thread.isRunning():
            self.commit_thread.stop()
            self.log_label.setText('Stopping Auto Commit Bot...')

    def on_commit_thread_finished(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.log_label.setText('Auto Commit Bot stopped.')

    def update_log(self, message):
        self.log_label.setText(message)

    def show_token_tutorial(self):
        tutorial_message = (
            "How to get a GitHub Personal Access Token:\n\n"
            "1. Go to GitHub and log in to your account.\n"
            "2. Click on your profile picture in the top-right corner, then select 'Settings'.\n"
            "3. In the left sidebar, click on 'Developer settings'.\n"
            "4. Under 'Personal access tokens', click on 'Tokens (classic)'.\n"
            "5. Click 'Generate new token'.\n"
            "6. Select the scopes for the token. For this bot, 'repo' and 'workflow' are typically required.\n"
            "7. Click 'Generate token' at the bottom of the page.\n"
            "8. Copy the generated token and paste it into the GitHub Token field in this application."
        )
        QMessageBox.information(self, 'GitHub Token Tutorial', tutorial_message)

    def apply_earthy_theme(self):
        QApplication.setStyle("Fusion")
        palette = QPalette()

        # Set the palette for the background
        palette.setColor(QPalette.Window, QColor("#4e342e"))
        palette.setColor(QPalette.WindowText, QColor("#ffffff"))

        # Set the palette for the buttons
        palette.setColor(QPalette.Button, QColor("#795548"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Disabled, QPalette.Button, QColor("#6d4c41"))
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor("#ffffff"))

        # Set the palette for the line edits
        palette.setColor(QPalette.Base, QColor("#6d4c41"))
        palette.setColor(QPalette.Text, QColor("#ffffff"))
        palette.setColor(QPalette.Disabled, QPalette.Base, QColor("#5d4037"))
        palette.setColor(QPalette.Disabled, QPalette.Text, QColor("#bdbdbd"))

        # Set the palette for other widget text
        palette.setColor(QPalette.PlaceholderText, QColor("#d7ccc8"))

        # Apply the palette to the application
        QApplication.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutoCommitBotUI()
    window.show()
    sys.exit(app.exec_())
