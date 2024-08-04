
# Auto-Commit Bot

![Python version](https://img.shields.io/badge/python-3.6%2B-blue) ![GitHub license](https://img.shields.io/github/license/Hamed-Gharghi/Auto-Commit-Bot) ![](https://komarev.com/ghpvc/?username=Hamed-Gharghi&color=green&style=flat-square)

## Description

**Auto-Commit Bot** is a Python script designed to automate the process of generating Python scripts, committing them to a GitHub repository, and pushing the changes. This bot can be scheduled to run periodically (e.g., every 24 hours) and will automatically handle file creation, git operations, and pushing changes to GitHub.

## Features

- **Automated File Generation:** Creates Python scripts with a comment header including the author name, date, and description.
- **Git Operations:** Automatically adds, commits, and pushes changes to your GitHub repository.
- **Scheduled Execution:** Runs the bot periodically using a sleep timer.

## Badges

- **CI Workflow Status:** ![GitHub Actions](https://img.shields.io/github/workflow/status/Hamed-Gharghi/Auto-Commit-Bot/CI)

## Tags

- **Automation**
- **GitHub Actions**
- **Python Scripts**
- **Code Commit**
- **Automated Git Operations**
- **Scheduled Tasks**
- **Programming**

## Python Version

- **Python 3.6 or higher** is required to run this script.

## Getting Started

To use the Auto-Commit Bot, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Hamed-Gharghi/Auto-Commit-Bot.git
   cd Auto-Commit-Bot
   ```

2. **Configure the Script:**
   - Open `Auto_Commit.py` and update the following placeholders:
     - `path_to_your_repository`: Local path to your Git repository.
     - `your_github_username`: Your GitHub username.
     - `your_github_token`: Your GitHub token.
     - `your_repository_name`: The name of your GitHub repository.

3. **Install Required Packages:**
   Ensure you have Python installed. No external packages are required for this script.

4. **Run the Script:**
   Execute the script to start the auto-commit process.
   ```sh
   python Auto_Commit.py
   ```

5. **Schedule the Script:**
   Use a scheduler like `cron` on Unix-based systems or Task Scheduler on Windows to run the script at your desired interval (e.g., every 24 hours).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improvements or want to contribute, please fork the repository and submit a pull request. All contributions are welcome!

## Contact

- **Author:** Hamed Gharghi
- **Email:** [Hamedgharghi1@gmail.com](mailto:Hamedgharghi1@gmail.com)
- **GitHub:** [Hamed-Gharghi](https://github.com/Hamed-Gharghi)

