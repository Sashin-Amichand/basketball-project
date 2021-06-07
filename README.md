# basketball-project
This website is created using Flask, a Python Web app framework, so if you wish to configure/edit the website you must run the flask.py file via a flask cmd.
HTML files are in templates, CSS and Image folders are in Static. OR if you simply wish to view it, click this link:
-----------------------------------------------------------------------------------------------------------
To edit/configure make sure to run the requirments.txt in a virtual env and then install it, or else it will install on your pc. 

Steps to creating a virtual env in powershell:

0. Install python
1. Inside the basketball-project folder you downloaded from this repo, open a powershell prompt
2. python -m venv basketballproject
4. basketballproject/Scripts/activate
5. pip install -r requirements.txt
(Optional set development mode: $env:FLASK_ENV="development")
7. $env:FLASK_APP="indexFlask"
8. flask run (to start the website, ctrl + c to stop it and then rerun it in order to see any changes.)
9. When done in the virtual env just type deactive and to reactivate follow steps 3-5.
-----------------------------------------------------------------------------------------------------------
