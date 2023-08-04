# Release Notes – SLSC Face Tagging
Date: August 4, 2023

## Features of SLSC Face Tagging
The SLSC Photo Archive Face project is designed to identify and tag people from the images uploaded by the client or user. Once the detected faces are tagged, the organized results are stored in a readily accessible database. The client can then sort photos with respect to students, helping them keep track of each student's progress.

## Components of the Project
The main components of our project include:
- Frontend: Image upload, person-gallery, and home components.
- Backend: Database integration and actual logic for retrieving all the persons and identifying unique ones among them.
- Pre-trained: Face classification, detecting faces, and classifying them as known or unknown based on pre-trained data. Resizing the images and saving them to the Database and UI.
- Build: Continuous CI/CD integration to perform builds and run several tests.

## Latest Added Features
- Pre-trained: Classifying the images as known or unknown based on the pre-trained data.

## Bug Fixes
- Fixed: Resizing the images displayed on the UI to fit the screen.
- Fixed: Correctly classifying the faces in the image as known or unknown.

## Known Issues
- [Issue #11](https://github.com/rushikesh-slu/SLSC-face-archive/issues/11) - Closed
- [Issue #33](https://github.com/rushikesh-slu/SLSC-face-archive/issues/33) - Closed
- [Issue #14](https://github.com/rushikesh-slu/SLSC-face-archive/issues/14) - Closed
- [Issue #4](https://github.com/rushikesh-slu/SLSC-face-archive/issues/4) - Closed

## Outcome of the Project till Date
We were able to identify the faces in the images and classify them as known or unknown, displaying them on the UI. For now, we have used only a few sample input images. Moving on, we plan to train our model on a much larger dataset.

## Future Implementations
Our future implementations include training our model to work perfectly with a huge amount of data and designing a complete UI Web application for the Saint Louis Science Center.

## Technologies Used
- Angular (Frontend)
- Python Flask (Backend)
- Git

## My Contributions
I have added UI components, namely person-gallery and home components, and performed research on pre-trained models and licensing our project. Here is the link to my contribution: [Adding_Person_Gallery_Features by Manaswini1208 · Pull Request #35](https://github.com/rushikesh-slu/SLSC-face-archive/pull/35).

## How to Clone and Run?
1. Clone the GitHub repository: `git clone https://github.com/rushikesh-slu/SLSC-face-archive.git`
2. Open the cloned repository in VS Code editor.
3. The `main.yml` file in the GitHub workflows folder contains continuous CI/CD integration. Several jobs have been built to install dependencies, test using pytest, execute releases, and zip them.
4. Moving on to the Frontend folder, which contains the UI application. Angular JS was used to create our user interface. So, initially, we must install Angular with the command `npm install -g @angular/cli`. Once Angular is installed, we can use `npm install` to install all of the dependencies. This will obtain all the essential node modules.
5. We have two components in the FrontEnd Face Tagging folder: image-upload and person-gallery. When an image with a group of individuals is uploaded from the UI, the first component displays an image upload button, while the second retrieves all the individual images from the backend.
6. In the backend `csvmanager.py`, we need to specify the path of our database file, and we are good to run our project using the command `npm start` in the terminal. This will open the application in the localhost, displaying all images of individual faces on UI.
