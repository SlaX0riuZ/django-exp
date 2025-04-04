# django-exp
experimenting with django framework

## djangoproject.com
- ^^ link for django documentation
- (also install edge browser extension for ease of access)

# Steps to setting up django
#### install django
- terminal: python -m pip install Django
#### install django extension -> start the project
- terminal: django-admin startproject projectname
- if that doesn't work, try: python -m django startproject projectname

#### get into the folder with the app
- terminal: cd projectname
- terminal: ls (if you see manage.py you got it)

#### set up app environment
- terminal: python manage.py runserver
- use CTRL+C in terminal to take the webserver down
- retype command to relaunch webserver
- TIP: open up another terminal so you don't have to relaunch webserver (make sure you can see manage.py from ls!)

#### create the app
- terminal: python manage.py startapp applicationname
- create "templates" and "static" folders inside applicationname folder, below migrations
- set ALLOWED_HOSTS = ['localhost', '127.0.0.1'] in projectname settings.py
- add applicationname to INSTALLED_APPS in settings.py
- set 'DIRS': [BASE_DIR / 'templates'], in settings.py under TEMPLATES
- set TIME_ZONE = 'America/Chicago' in settings.py (CDT/CST timezone!)

#### start making the base page
- go to templates folder and create new 'index.html'
- go to views.py under applicationname
- addline: def home(request): return render(request, 'index.html')
- create new 'urls.py' in applicationname folder
- add line: from django.urls import path
- add line: from . import views
- add line: urlpatterns=\[path\('', views.home, name='home'\),\]

___
- goto urls.py in projectname
- add include library to from django.urls import path (-> from django.urls import path, include)
- add line under urlpatterns array: path('', include('applicationname.urls'))
