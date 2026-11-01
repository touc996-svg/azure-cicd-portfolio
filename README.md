# Azure CI/CD Portfolio

## Project Overview
This project demonstrates a basic Continuous Integration (CI) pipeline using Python and GitHub Actions.

The goal is to automate code testing whenever changes are pushed to the repository or a pull request is created.

## Technologies Used
- Python 3.12
- GitHub Actions
- Git
- GitHub
- Unit Testing

## How It Works
1. A developer pushes code to the main branch.
2. GitHub Actions automatically starts the CI workflow.
3. The workflow sets up Python 3.12.
4. Automated unit tests run using Python's unittest framework.
5. GitHub reports whether the tests passed or failed.

## Project Structure
```text
azure-cicd-portfolio/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── test_app.py
└── README.md
