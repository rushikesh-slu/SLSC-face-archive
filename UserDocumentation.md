# User Documentation - SLSC Face Tagging Project Setup

## About the Project
The SLSC Photo Archive Face project aims to identify and tag people from the images uploaded by the client or user. Once the face detection and tagging are completed, the organized results are stored in a database, readily available for access. The client utilizes the photo tagging interface to sort photos with respect to students, helping them track each student's progress.

## Components
The project consists of the following components:
- **Frontend**: Responsible for the user interface and interaction with the users.
- **Backend**: Handles the processing of images, face detection, and database operations.
- **Pre-training**: The project involves pre-training models for face detection and recognition.
- **CI/CD Integration**: Ensures continuous integration and deployment.

## Requirements
Make sure you have the following software installed on your system before setting up the project:
- Python
- Node
- Angular
- Node package manager (npm)
- Git
- Visual Studio Code

## Installation Instructions
1. **Install Node**:
   - Download and install Node.js from the official website: [Node.js](https://nodejs.org/)

2. **Install VSCode**:
   - Download and install Visual Studio Code from the official website: [VSCode](https://code.visualstudio.com/)

3. **Cloning and Deploying the Project Locally**:
   - Clone the project repository using the following Git command:
     ```
     git clone https://github.com/rushikesh-slu/SLSC-face-archive.git
     ```
   - After cloning, open the project in VSCode editor.
   - Navigate to the frontend folder using the following commands:
     ```
     cd SLSC-face-archive
     cd frontend
     cd SLSCFaceTagging
     ```
   - Install Angular JS and node packages using the following commands:
     ```
     npm install -g @angular/cli
     npm install
     ```
   - Run the application locally:
     ```
     ng serve
     ```

4. **Setting Up the Backend**:
   - Move to the backend directory using the following command:
     ```
     cd backend
     ```
   - Install required Python packages using the requirements.txt file:
     ```
     pip install -r requirements.txt
     ```
   - Run the backend application:
     ```
     python main.py
     ```
   - The application will be up and running at http://localhost:8080.
  
5. **License Information**
    Apache and MIT License best suites our project.

6. **Security considerations**
   - Atleast two people from the collaborations should review the code changes to merge it with main branch.

## Useful Git Commands
Here are some useful Git commands to interact with the project repository:
1. `git clone <repository_url>`: Clone the project repository to your local machine.
2. `git pull`: Fetch and merge changes from the remote repository to the local branch.
3. `git checkout -b <name_of_branch>`: Create and switch to a new branch with the given name.
4. `git add <filename>`: Stage changes of a specific file for the next commit.
5. `git commit -m "Commit message"`: Commit staged changes with a descriptive commit message.
6. `git push`: Push committed changes to the remote repository.
