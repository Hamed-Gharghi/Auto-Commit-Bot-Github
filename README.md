# Auto-Commit Bot

![Python version](https://img.shields.io/badge/python-3.6%2B-blue) ![GitHub license](https://img.shields.io/github/license/Hamed-Gharghi/Auto-Commit-Bot-Github) ![GitHub stars](https://img.shields.io/github/stars/Hamed-Gharghi/Auto-Commit-Bot-Github?style=social) ![](https://komarev.com/ghpvc/?username=Hamed-Gharghi&color=green&style=flat-square) ![CI Workflow Status](https://img.shields.io/github/workflow/status/Hamed-Gharghi/Auto-Commit-Bot-Github/CI) ![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)

## Overview

**Auto-Commit Bot** is a Python-based tool designed to automate the process of generating, committing, and pushing changes to a GitHub repository. Ideal for developers and teams who need to ensure their repositories stay updated with minimal manual intervention. This bot can be scheduled to run at regular intervals, such as every 24 hours, to handle file creation and git operations automatically.

### Key Features

- **Automated File Generation**: Create Python scripts with autogenerated headers including author information, date, and description.
- **Seamless Git Operations**: Automate adding, committing, and pushing changes to your GitHub repository.
- **Scheduled Execution**: Set up a sleep timer to run the bot at specified intervals for ongoing automation.
- **GUI Application**: A user-friendly graphical interface for configuring and running the bot without needing to edit code manually.
- **Standalone Executable**: An easy-to-use Windows executable that includes all necessary modules and dependencies.

## Badges

- **Build Status**: ![Build Status](https://img.shields.io/github/workflow/status/Hamed-Gharghi/Auto-Commit-Bot-Github/CI)
- **Version**: ![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)
- **License**: ![License](https://img.shields.io/github/license/Hamed-Gharghi/Auto-Commit-Bot-Github)

## Tags

- **Automation**
- **GitHub Actions**
- **Python Scripts**
- **Code Commit**
- **Automated Git Operations**
- **Scheduled Tasks**
- **Programming**
- **GUI Application**

## Python Version

- **Python 3.6 or higher** is required to run the script. Ensure your Python environment meets this requirement.

## Getting Started

Follow these steps to set up and use the Auto-Commit Bot:

### Clone the Repository

```sh
git clone https://github.com/Hamed-Gharghi/Auto-Commit-Bot-Github.git
cd Auto-Commit-Bot-Github
```

### Configuration

#### For Python Script

1. Open `Auto_Commit.py` and update the following placeholders:
   - `path_to_your_repository`: Specify the local path to your Git repository.
   - `your_github_username`: Enter your GitHub username.
   - `your_github_token`: Generate and enter your GitHub token.
   - `your_repository_name`: Provide the name of your GitHub repository.

2. **Run the Script**:
   ```sh
   python Auto_Commit.py
   ```

3. **Schedule the Script**:
   Use a scheduler such as `cron` on Unix-based systems or Task Scheduler on Windows to automate script execution at your desired interval (e.g., every 24 hours).

#### For GUI Application

1. **Download the Executable**:
   Download the Windows executable from the [Releases](https://github.com/Hamed-Gharghi/Auto-Commit-Bot-Github/releases) page.

2. **Run the Executable**:
   - Double-click `Auto_Commit_GUI.exe` to launch the application.
   - Enter the repository path, GitHub username, GitHub token, file name, and sleep time.
   - Click "Start Auto Commit Bot" to begin automation.
   - Click "Stop Auto Commit Bot" to halt the process.

3. **Configure the GUI**:
   - **Browse Repository**: Use the "Browse" button to select your Git repository directory.
   - **GitHub Token Tutorial**: Click the "How to get GitHub Token?" button for detailed instructions on obtaining a GitHub Personal Access Token.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

We welcome contributions to enhance the Auto-Commit Bot. If you have suggestions or want to contribute, please fork the repository, make your changes, and submit a pull request. Your contributions are greatly appreciated!

## Contact

- **Author**: Hamed Gharghi
- **Email**: [Hamedgharghi1@gmail.com](mailto:Hamedgharghi1@gmail.com)
- **GitHub Profile**: [Hamed-Gharghi](https://github.com/Hamed-Gharghi)

## Additional Resources

- **GitHub Personal Access Token Tutorial**: For information on generating a GitHub Personal Access Token, refer to the [GitHub Documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
- **PyInstaller Documentation**: For details on how to package Python applications, visit the [PyInstaller Documentation](https://www.pyinstaller.org/).

---

Thank you for using the Auto-Commit Bot! If you have any questions or feedback, feel free to reach out through the contact details provided above.
