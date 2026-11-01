Azure CI/CD Portfolio
Project Overview
This project demonstrates a basic Continuous Integration (CI) pipeline using Python and GitHub Actions.
The goal is to automate code testing whenever changes are pushed to the repository or a pull request is created.
Technologies Used
Python 3.12
GitHub Actions
Git
GitHub
Unit Testing
How It Works
A developer pushes code to the main branch.
GitHub Actions automatically starts the CI workflow.
The workflow sets up Python 3.12.
Automated unit tests run using Python’s unittest framework.
GitHub reports whether the tests passed or failed.
Project Structure
azure-cicd-portfolio/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── test_app.py
└── README.md
Run the Application
python app.py
Run the Tests
python -m unittest discover -s . -p "test_*.py" -v
CI Pipeline Status
The GitHub Actions workflow has successfully executed, and the automated tests have passed.
Project Purpose
This project demonstrates practical experience with automated testing, CI workflows, Python, and GitHub Actions as part of a cloud and DevOps portfolio.
Note: This project currently demonstrates CI automation through GitHub Actions. It does not represent an actual deployment to Microsoft Azure.
