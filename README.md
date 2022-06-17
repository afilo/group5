# Clifford Systems
Software Engineering group 5 for CEN3. 

### Production and Supplying Managment



The main idea of the software is to find a solution to the production that factories have to make. As the production is hard without having a good idea of the demands that the clients wants for the productions. Our soultion is an implimentation of a E-store that is connected to the main program, by inputing the orders with using their own formula they can predict the amounts od supplys that they need to make the production. On top of that taking on consideration the 2,3 previous years for that month we can find an average that can be like a blueprint for the factory to have supplies. 

# To run this Project

Make Sure you are using Python 3.10 , Download it from the official Python website
Also Make sure to download pip together with Python.

You will need to install pipenv , to do so do the command below 
> pip install pipenv
or 
> python -m pip install pipenv

Open a folder in your computer and open a terminal inside it.
Now you need to clone the repository
> git clone https://github.com/afilo/group5

go inside the src file 
> cd src/

Now here create a file called db_configure.py
Inside this file write:
```
host = "mongodb+srv://afilopati19:.Klevi123@cluster0.wwqj1sf.mongodb.net/test?authMechanism=DEFAULT"
name = "clifford_systems"
authMechanism = "SCRAM-SHA-1"

django_secret_key = "django-insecure-omc9gh4#xa8+1uyp(%f&-0$y633e1r0m*4a5_*scnyn1fj3b#u"
```
now install all libraries needed with pipenv 
>pipenv install
All libraries are written inside the pipfile which pipenv uses to find what it needs to install

To run the server , simply run the command
>python manage.py runserver

At default settings it runs on port 8000 
Employee account:
Email: aosmani19@epoka.edu.al
Password: klevi123

Admin Account:

Email: aldi@gmail.com 
Password: klevi123

Client Account:
Email: kciko@gmail.com
Password: klevi123

