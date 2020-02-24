HOW TO MAKE A DJANGO SITE THAT DISPLAYS CMDLINE OUTPUT

made for Priyabrata

# Create a new project
* https://docs.djangoproject.com/en/3.0/intro/tutorial02/
* `django-admin startproject mysite`
* `python manage.py startapp cmdexample`

# add a template
* https://djangobook.com/mdj2-django-templates/

# run a command line process then pipe it into the template
* (see cmdexample/views.py)


# Run server 
* `python manage.py runserver`

* visit http://127.0.0.1:8000/cmdexample/
