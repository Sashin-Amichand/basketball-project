# basketball-project
This website is created using Flask, a Python Web Framework, so if you wish to configure/edit the website you must run the flask.py file via a flask cmd.
HTML files are in templates, CSS and Image folders are in Static. OR if you simply wish to view it, click this link: https://sa-basketball.herokuapp.com/
--------------------------------------------------------------------------------------------------------------------------------------------------------------
To edit/configure make sure to run the requirments.txt in a virtual env and then install it, or else it will install locally on your PC. 

Steps to creating a virtual enviroment in powershell:

0. Install python
1. Inside the basketball-project folder you downloaded from this repo, open a powershell prompt
2. python -m venv basketballproject
4. basketballproject/Scripts/activate (Make sure executionpolicy is unrestricted/remote signed else it won't run. To do so, open powershell in admin mode and enter: set-executionpolicy remotesigned. To put it back in restricted mode simply change remotesigned to restricted.)
5. pip install -r requirements.txt
7. $env:FLASK_APP="indexFlask" (Optional set development mode: $env:FLASK_ENV="development")
8. Flask run to start the website. Ctrl + c to stop it and rerun it in order to see any changes you made.
9. When done in the virtual env just type deactive and to reactivate follow steps 3-5.
--------------------------------------------------------------------------------------------------------------------------------------------------------------

