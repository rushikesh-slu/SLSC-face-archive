# Introduction
Welcome to your guide on how to set up this project.
## Setup

### Requirements
- Python
- Node

Clone the repository using git:

```bash
git clone https://github.com/rushikesh-slu/SLSC-face-archive.git
cd SLSC-face-archive
```

## Running the application

Open your terminal or command line interface and navigate to your frontend directory:

```bash
cd frontend/SLSCFaceTagging
```

Build frontend
```bash
npm install
ng build
```

Open your terminal or command line interface and navigate to your  backend directory:

```bash
cd backend
```
Once you're in the backend directory, create and activate a Python virtual environment. This step helps to keep our project clean and avoid package dependency issues.

Now, let's install the required Python packages. Install them by running:

```bash

pip install -r requirements.txt
```
Great, you're all set! Start the Flask application by running:

```bash
python main.py
```
Application is now up and running at http://localhost:5000.
