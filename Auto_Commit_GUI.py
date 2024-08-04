import sys
import os
import subprocess
import re
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox, QLabel


class GitCommitBot(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the GUI components
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git Commit Bot')

        # Create layout
        layout = QVBoxLayout()

        # Repo Path
        self.repoPathEdit = QLineEdit(self)
        self.repoPathEdit.setPlaceholderText('Repository Path')
        layout.addWidget(self.repoPathEdit)

        # Browse Button
        self.browseButton = QPushButton('Browse', self)
        self.browseButton.clicked.connect(self.browseRepoPath)
        layout.addWidget(self.browseButton)

        # File Name
        self.fileNameEdit = QLineEdit(self)
        self.fileNameEdit.setPlaceholderText('File Name (e.g., script.py)')
        layout.addWidget(self.fileNameEdit)

        # GitHub Username
        self.githubUsernameEdit = QLineEdit(self)
        self.githubUsernameEdit.setPlaceholderText('GitHub Username')
        layout.addWidget(self.githubUsernameEdit)

        # GitHub Token
        self.githubTokenEdit = QLineEdit(self)
        self.githubTokenEdit.setPlaceholderText('GitHub Token')
        self.githubTokenEdit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.githubTokenEdit)

        # Tutorial Button
        self.tutorialButton = QPushButton('Tutorial on GitHub Token', self)
        self.tutorialButton.clicked.connect(self.showTutorial)
        layout.addWidget(self.tutorialButton)

        # Run Button
        self.runButton = QPushButton('Run', self)
        self.runButton.clicked.connect(self.commit_bot)
        layout.addWidget(self.runButton)

        # Set layout
        self.setLayout(layout)

    def browseRepoPath(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Repository Path')
        if path:
            self.repoPathEdit.setText(path)

    def showTutorial(self):
        QMessageBox.information(self, 'GitHub Token Tutorial',
                                'To generate a GitHub token, visit:\n'
                                'https://github.com/settings/tokens\n'
                                '1. Click "Generate new token".\n'
                                '2. Provide a note and select scopes.\n'
                                '3. Click "Generate token".\n'
                                '4. Copy the token and paste it here.')

    def commit_bot(self):
        repo_path = self.repoPathEdit.text().strip()
        file_name = self.fileNameEdit.text().strip()
        github_username = self.githubUsernameEdit.text().strip()
        github_token = self.githubTokenEdit.text().strip()

        if not repo_path or not file_name or not github_username or not github_token:
            QMessageBox.warning(self, 'Input Error', 'Please provide all required fields.')
            return

        if not file_name.endswith('.py'):
            file_name += '.py'

        def sanitize_filename(filename):
            return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', filename)

        def write_file(file_path, content):
            with open(file_path, 'w') as f:
                f.write(content)

        def check_git_status():
            try:
                result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, check=True)
                return result.stdout.strip()
            except subprocess.CalledProcessError as e:
                QMessageBox.critical(self, "Error", f"Error checking Git status: {e}")
                return None

        def make_commit():
            os.chdir(repo_path)

            # Define placeholder content
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            code = f"""\
# Author: Hamed Gharghi
# Date: {timestamp}
# Description: This script is an auto-generated placeholder.

print("This is an auto-generated Python script.")
"""
            file_path = os.path.join(repo_path, file_name)

            # Write placeholder code to file
            write_file(file_path, code)

            # Check for unstaged changes
            status = check_git_status()
            if status:
                if status:
                    # Offer to stash changes
                    reply = QMessageBox.question(self, "Unstaged Changes",
                                                 "You have unstaged changes. Do you want to stash them and proceed?",
                                                 QMessageBox.Yes | QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        subprocess.run(['git', 'stash'], check=True)

                try:
                    # Pull changes from the remote repository
                    subprocess.run(['git', 'pull', '--rebase'], check=True)

                    # Add all changes to git (including untracked files)
                    subprocess.run(['git', 'add', '--all'], check=True)

                    # Commit changes
                    commit_message = f'Automated commit: Added {file_name} with a placeholder content'
                    subprocess.run(['git', 'commit', '-m', commit_message], check=True)

                    # Configure Git to use token for this repository
                    subprocess.run(['git', 'remote', 'set-url', 'origin',
                                    f'https://{github_username}:{github_token}@github.com/{github_username}/Daily-Python.git'], check=True)

                    # Push changes to GitHub
                    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
                    QMessageBox.information(self, "Success", "Commit and push successful!")
                except subprocess.CalledProcessError as e:
                    QMessageBox.critical(self, "Error", f"Error during git operations: {e}")
                finally:
                    # If changes were stashed, pop them
                    if status:
                        subprocess.run(['git', 'stash', 'pop'], check=True)

        # Run the commit bot process
        make_commit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GitCommitBot()
    ex.show()
    sys.exit(app.exec_())
