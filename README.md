# Python Environment Setup with Flask

This guide will help you set up a Python environment, install Flask, and clone the repository to get started on your project.

## Prerequisites

Before proceeding, make sure you have the following installed on your system:

- **Python 3.x**  
  You can check if Python is installed by running:
  ```bash
  python --version
  ```
- Git
Ensure you have Git installed by running:
  ```bash
  git --version
  ```

## Clone the Repository
Start by cloning the repository to your local machine. Replace the URL with the actual repository URL.
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
## Set Up and activate the Python Virtual Environment
Set up a virtual environment with name flaskEnv:
```bash
python -m venv flaskEnv
```
Activate the Virtual Environment

Windows:
```bash
flaskEnv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
After activation, your terminal prompt should change to show the name of the virtual environment (e.g., (flaskEnv)).

## Install Required Packages
With the virtual environment activated, install the required Python packages by running:
```bash
pip install flask
pip install requests
```

## Running the Flask Application
Once Flask is installed, you can run the Flask application. If your Flask app is in a file called app.py, use this command to start the server:
```bash
python app.py
```
By default, Flask runs on http://127.0.0.1:5000.

## Deactivating the Virtual Environment
When you're done working in the virtual environment, you can deactivate it by simply running:
```bash
deactivate
```

