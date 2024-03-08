Developer's Local Machine (Windows):
Pre-requisites:
Python
Visual Studio Code
Git
PostgreSQL with PgAdmin

Create a root folder for the project.
Ex.: HealthcareSystem

Recommended folder structure:
HealthcareSystem
|
+-- env
|
+-- hmosystem
    |
    +-- __pycache__
    +-- __init_.py
    +-- asgi.py
    +-- settings.py
    +-- urls.py
    +-- wsgi.py
    +-- folder1_app
    +-- folder2_app
    +-- folder3_app
    +-- manage.py
    +-- readme.txt
    +-- requirements.txt

Brief explanation:
HealthcareSystem is the root folder. While env is the virtual environment. The hmosystem folder is for the project.
folder1_app, folder2_app and so on are the app folders which contains the necessary files for each respective modules.

Create the folder structure:
1. Open VS Code.

2. File > Open folder...

3. Locate your recently created root folder and click open.

4. Inside the root folder, create a virtual environment named 'env'. Run python -m venv env or py -m venv env
    If there is a permission issue, execute this:
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

5. Create folder hmosystem and run the command: cd hmosystem
6. git init -b main
7. git add .
8. Your Github account must be a collaborator of the hmosystem repository
9. git remote add origin git@github.com:Gitbuster22/hmosystem.git
10. ssh-keygen -t ed25519 -C "your@email.com"
11. The location of the ssh key (.pub file) will be shown. Locate the file, open, and copy the said key. Paste the ssh key to your github account.
12. git fetch --all
13. git pull origin main
14. git checkout -b dev
15. git pull origin dev
16. pip install -r requirements.txt
    if having error of 'pip not found', add pip to environment variables, restart the unit and run the command again.