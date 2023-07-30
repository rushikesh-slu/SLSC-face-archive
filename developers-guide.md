# Developer's guide for SLSC face Tagging archive

## INTRODUCTION

# Developer's Guide for SLSC Face Tagging Archive

This project is a GitHub Action that builds and deploys a face tagging archive for the SLSC Yes program. It uses Python, Sphinx, facenet-pytorch and GitHub Pages to create and host a HTML documentation site that contains the face images and metadata of the participants.

## Prerequisites

To run this project, you need:

- A GitHub account and a repository for your project
- A GitHub token with the `repo` and `packages` scopes
- Python 3.8 or higher installed on your machine
- Pip installed on your machine
- Flake8 and Pytest installed on your machine
- Sphinx installed on your machine
- A `requirements.txt` file that lists the Python dependencies for your project
- A `docs` folder that contains the source files for your documentation site
- A `main.yml` file that defines the workflow for your GitHub Action

## Installation and Configuration

To install and configure this project, you need to:

1. Fork or clone this repository to your own GitHub account.
2. Create a new branch for your changes.
3. Edit the `main.yml` file to suit your needs. You can change the name of the job, the triggers, the steps, and the parameters as you wish.
4. Edit the `docs` folder to add or modify the content of your documentation site. You can use markdown or reStructuredText files to write your documentation. You can also use images, tables, code blocks, and other features supported by Sphinx. You can refer to this [guide](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for more information on how to use reStructuredText with Sphinx.
5. Commit and push your changes to your branch.
6. Create a pull request to merge your branch to the main branch.

## Build, Run, and Test

To build, run, and test this project, you need to:

1. Open VS Code and open your project folder.
2. Run the `Python: Select Interpreter` command from the command palette (`Ctrl+Shift+P` on Windows or `Cmd+Shift+P` on Mac) and select Python 3.8 or higher.
3. Run the `Terminal: Create New Integrated Terminal` command from the command palette to open a new terminal in VS Code.
4. Run `pip install -r requirements.txt` in the terminal to install the Python dependencies for your project.
5. Run `flake8 .` in the terminal to check for syntax errors and code style violations in your project.
6. Run `pytest` in the terminal to run the tests for your project.
7. Run `sphinx-build -b html docs docs/build/html` in the terminal to build the HTML documentation site for your project.
8. Open the `docs/build/html/index.html` file in your browser to preview your documentation site.

## Contributing

To contribute to this project, you need to:

1. Follow the [GitHub flow](https://guides.github.com/introduction/flow/) workflow for collaborating on GitHub projects.
2. Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for writing Python code.
3. Write clear and concise commit messages and pull request descriptions.
4. Write unit tests for your code using Pytest.
5. Write documentation for your code using Sphinx.

## License and Acknowledgements

This project is licensed under the MIT License. See the [LICENSE](https://github.com/rushikesh-slu/SLSC-face-archive/pull/29) file for more details.

This project is based on the [zip-release](https://github.com/TheDoctor0/zip-release) action by TheDoctor0 and the [action-sphinx-docs-to-gh-pages](https://github.com/marketplace/actions/action-sphinx-docs-to-gh-pages)
