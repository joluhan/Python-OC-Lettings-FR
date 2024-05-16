Programming Interfaces
===========================

This project was entirely coded with django. Therefore two actions are possible:


Programming interface via django administration site
--------------------------------------------------------

Only accessible to Super Users, this platform allows you to manage using CRUD actions
(Create, Read, Update and Delete) all data in the Database.

    A Super User has already been created in the Database but if you wish to create a new one,
    You can enter this command in your terminal at the root of the project:

    ``python manage.py createsuperuser``

    All you have to do is answer the questions and your super user will be created.

To connect to the Django administrative platform, simply add ``/admin/`` at the end
of your URL. Whether you are Local or using the latest version online, the process is identical.
Enter your super user's information and you will have access to the platform.


Programming Interface via the Python shell
----------------------------------------------

Less intuitive than the Django administration platform, it is simply used
by entering your terminal at the root of the project, the command:

``python manage.py shell``

Using the Shell offers several advantages over the interface
administrative of Django (Django Admin):

A - Exploration and Rapid Test:

The interactive shell allows developers to quickly explore the structure of their application,
query the database, test queries, and experiment with Python code without having to
to go through a graphical user interface.

B - Scripting and Automation:

The shell is a great environment for writing scripts and automating tasks.
You can write scripts to manipulate data, perform maintenance operations
or perform tasks specific to your application.

C - Direct Access to the Django ORM Console:

The shell allows direct access to Django's ORM (Object-Relational Mapping),
which makes it easier to run queries against the database without having to create specific views or models.

D - Interactive Debugging:

Using the interactive shell you can debug your application interactively,
by inspecting objects, testing specific functionality, and understanding behavior
of your code at a deeper level.

E - Personalization and Control:

While Django's administrative interface offers a ready-to-use user interface for managing models,
The shell provides more flexibility and control for developers who want to customize or automate specific tasks.

For more information :

https://shell.readthedocs.io/en/latest/shell_api.html
