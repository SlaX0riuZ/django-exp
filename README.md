# django-exp
experimenting with django framework

## djangoproject.com
^^ link for django documentation

# Steps to setting up django
#### install django
terminal: python -m pip install Django
#### install django extension
#### start the project
terminal: django-admin startproject projectname
if that doesn't work, try: python -m django startproject projectname
#### get into the folder with the app
terminal: cd projectname
terminal: ls (if you see manage.py you got it)
#### set up app environment
terminal: python manage.py runserver
use CTRL+C in terminal to take the webserver down
retype command to relaunch webserver
TIP: open up another terminal so you don't have to relaunch webserver (make sure you can see manage.py from ls!)
#### create the app
terminal: python manae.py startapp applicationname