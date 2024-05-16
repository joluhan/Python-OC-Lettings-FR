Installing the project
======================

Repository cloning
-------------------

Download the entire repository at:

https://github.com/hire-blac/OrangeCountyLettings

To do this, please open your Order Terminal:

1. Using the cd command, go to the directory where you want to install the repository example: ``cd Desktop``
*(to install it on your computer's Desktop)*.

2. Subsequently, enter the command in your terminal:

``git clone https://github.com/hire-blac/OrangeCountyLettings.git``

then press enter to create your local clone.

Once the repository has been downloaded and stored locally, go to the project folder. To do this use the command:

``cd OrangeCountyLettings``

Create a virtual environment to retrieve the project's dependencies and packages.

*(example procedure)*: ``python -m venv .venv``

Check with ``ls`` that you now have a folder env. If this is not the case, repeat this step, checking the syntax of the command line. Otherwise activate your new virtual environment.
  
    example procedure:
    - (PowerShell): ``.\.venv\Scripts\activate``
    - (Windows): ``.\.venv\Scripts\activate.bat``
    - (Linux): ``source .venv/bin/activate``

*If you encounter difficulties you can refer to the site:*

https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789
  
  To check the success of this maneuver, you should have an ``(.venv)`` in front of your command line.

  PS: Just type ``deactivate`` to close it.

Finally, download with pip the packages and dependencies required for the correct functioning of the code with requirements.txt by entering the following command *(in your virtual environment!)*

``pip install -r requirements.txt```

Once the download is complete and the installation is complete, you are ready to run the code.

Creating the ``.env``  file
------------------------------

To ensure optimal security, sensitive data has not been integrated into the repository.
Please therefore create a file at the root of the project named: ``.env`` and put the following variables there:

``SECRET_KEY = "the secret key of the project"``

``DSN = "the sentry dsn key"``
 
The Sentry DSN key will be communicated to you by Sentry https://sentry.io/signup/, when you create an account and create a project. You will only have to copy and paste the value of the DSN key.

Run the site:
------------------
In the project directory with your ``.venv`` enabled:
   - Type: ``python manage.py runserver``
   - Go to http://localhost:8000/ in a browser.
   - Confirm that the site is working and navigable (you should see several profiles and locations).
