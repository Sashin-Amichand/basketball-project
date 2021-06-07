# basketball-project
This website is created using Flask, a Python Web app framework, so if you wish to configure/edit the website you must run the flask.py file via a flask cmd.
HTML files are in templates, CSS and Image folders are in Static. OR if you simply wish to view it, click this link:
-----------------------------------------------------------------------------------------------------------
To edit/configure make sure to run the requirments.txt in a virtual env and then install it, or else it will install on your pc. 

Steps to creating virtual env in powershell:

0. Install python
1. Inside the basketball-project open a powershell prompt
2. python -m venv basketballproject
3. basketballproject/Scripts/activate
4. $env:FLASK_APP="indexFlask"
5. flask run (to start the website, ctrl + c to stop it and then rerun it in order to see any changes.)
6. When done in the virtual env just type deactive and to reactivate follow steps 3-5.
-----------------------------------------------------------------------------------------------------------
