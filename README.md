# SLSC-Photo-archive-face-tagging-achievers
Initiative to try developing a open source community photo face tagging software for Youth Exploring Science program

# Project SLSC Photo Archive Face Tagging

## Client Profile

Youth Exploring Science (YES) program is created to help underserved students in St. Louis area. Students participate in YES program to gain skills in Science, Technology, Engineering, Arts and Mathematics fields. High school students will gain real-world skills, career readiness training through YES program. Students in the YES program also promote the importance of STEAM-related careers.

## Project Brief
The SLSC Photo Archive Face project is to Identify and Tag people from the images client or user uploads, next once the detected faces tagging is completed we need to store the organized result in a database readily available to access, the client with the help of photo tagging interface would like to sort photos with respect to student which helps them to keep track of each students progress.

## 
* Data(All the photos with their name tags),
* As an admin, They can upload, edit and delete the images and tag them with their respective names.
* Preprocess data.
* Train a model/ Adapt a pre-trained model to fit our data.
* Build UI/ Integrate with existing UI.



## CI/CD steps



### Workflow Steps
Checkout Repository

This step uses the actions/checkout action to fetch the project repository.

### Set up Python 3.8

This step utilizes the actions/setup-python action to set up the Python 3.8 environment for subsequent steps.


### Install Dependencies

This step ensures the required dependencies are installed.
It begins by upgrading pip to the latest version.
If a requirements.txt file is present, it installs the packages specified within it using pip.


### Lint with Flake8

This step performs code linting using Flake8, a popular Python linter.
It installs Flake8 and checks for Python syntax errors or undefined names in the project files.
The selected Flake8 error codes (E9, F63, F7, F82) specify the types of issues to be detected.
The linting results include a count of issues, source code snippets, and overall statistics.


### Test with Pytest

This step installs the pytest framework.
It runs the project tests using the pytest command.
Any test failures or errors will be reported in the workflow output.


### Zip Release

This step utilizes a custom action, TheDoctor0/zip-release, to create a ZIP archive of the project files.
The resulting archive is named "slsc-face-archive.zip".


### Create Release

This step employs the actions/create-release action to create a new release on GitHub.
The release is tagged with the run number of the workflow.
The release name is set as "Release {run_number}" for clarity.
The release is not marked as a draft and is not a pre-release.


### Upload Release Asset

This step uses the actions/upload-release-asset action to upload the ZIP archive as a release asset.
The asset is associated with the newly created release.

