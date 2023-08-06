# Developer Guide for Angular-Flask Application

## Introduction
This developer guide provides comprehensive information about setting up and developing an application that uses Angular for the frontend and Python Flask for the back end. Please follow the instructions below to contribute to the project.

## Getting Started

### Prerequisites
Here are the requirements you need to install on your machine before you can start developing:

1. [Node.js](https://nodejs.org/en/download/) and npm (Node Package Manager) - required for Angular.
2. [Python](https://www.python.org/downloads/) - required for Flask.
3. [Git](https://git-scm.com/downloads) - for version control.

### Project Structure
The project has two main directories: `frontend` and `backend`. `frontend` contains Angular related files while `backend` contains Flask related files.

### Cloning the Repository

Clone the repository using git:

```bash
git clone https://github.com/rushikesh-slu/SLSC-face-archive.git
cd SLSC-face-archive
```
## Setting up the Frontend (Angular)

To set up the Angular part of the project, follow the steps below:

1. **Navigate to the frontend directory**: Open your terminal and use the following command to change your current working directory to the 'frontend' directory:
   ```bash
   cd frontend
   
Install Angular CLI globally. Use the following command to install Angular CLI globally:
```bash

npm install -g @angular/cli
```
Install the required packages: All the required packages for your project are listed in the 'package.json' file. To install these packages, use the following command:
```bash
npm install
```
Run the Angular application: Now that you have installed all the required packages, you can start the Angular application using the following command:
```bash
ng serve
```
After running this command, the Angular development server starts.
Open your web browser and visit http://localhost:4200 to see the running Angular application.


## Setting up the Backend (Flask)

Follow the steps below to set up the Flask part of the project:

1. **Navigate to the backend directory**: From your terminal, change your current working directory to the 'backend' directory:
   ```bash
   cd ../backend
    ```
Create a virtual environment: It's recommended to create and use a virtual environment in Python to avoid package dependencies issues. You can create a virtual environment using virtualenv or venv, among others. Activate the virtual environment before moving on to the next steps.

Install the required Python packages:

```bash
pip install -r requirements.txt
```
Run the Flask application:

```bash
python main.py
```
After running this command, the Flask development server starts.

The backend API will be live at http://localhost:5000.

## Development Process

Follow these steps for development:
Update your main branch: Make sure you're on the `main` branch and it's up-to-date with `origin/main`:
   ```bash
   git checkout main
   git pull origin main
  ```
Create a new branch for your feature or bug fix: Use the following commands to create and switch to a new branch:
```bash
git checkout -b your-feature-name
```
Make your changes and commit them: After making your changes, stage and commit them with a meaningful message:
```bash
git add .
git commit -m "Your meaningful commit message"
```
Push your changes to your branch on GitHub: Use the following command to push your changes:
```bash
git push origin your-feature-name
```

Open a Pull Request on GitHub towards the main branch.




