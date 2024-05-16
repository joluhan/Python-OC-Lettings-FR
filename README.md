# Orange County Lettings - Web Application

Orange County Lettings is a start-up in the real estate rental industry. The start-up is in the midst of an expansion phase in the United States. She wants to improve her site both in terms of code and deployment.

## Summary
0. [Complete Documentation](#documentation)

1. [Development](#development)
  - [Improvement of Version 2.0](#improvement-of-version-20)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Creation of the ".env" file](#creation-of-the-env-file)
  - [Run Site](#run-site)
  - [Run Linting](#run-linting)
  - [Run Tests](#run-tests)
  - [Database](#database)
  - [Admin Panel](#admin-panel)

2. [Deployment](#deployment)
  - [Prerequisites](#prc3a9requisites-1)
  - [Configuration step](#configuration-step)
    - [Using GitHub Actions](#1---using-github-actions)
    - [Render host configuration](#2---render-host-configuration)

## Documentation

To access the complete documentation for this project please click here: --> [Complete documentation](https://python-oc-lettings-joluhan.readthedocs.io/en/latest/)


## Development

### Improvement of Version 2.0
  - Redesign of the modular architecture in the GitHub repository;
  - Reduction of various technical debts on the project;
  - Added a CI/CD pipeline and its deployment;
  - Application monitoring and error tracking via Sentry;
  - Creation of technical documentation for the application with Read The Docs and Sphinx.

### Prerequisites

- GitHub account with read access to this repository
-Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed that your OS shell's `python` command runs the Python interpreter above (unless a virtual environment is enabled).

### Facility
Download the entire repository at: https://github.com/hire-blac/OrangeCountyLettings

To do this, please open your Order Terminal:

1. Using the cd command, go to the directory where you want to install the repository example: ```cd Desktop``` *(to install it on your computer's Desktop)*.

2. Subsequently, enter the command in your terminal:
```
git clone https://github.com/hire-blac/OrangeCountyLettings.git
```
then press enter to create your local clone.

Once the repository has been downloaded and stored locally, go to the project folder. To do this use the command: 
```cd OrangeCountyLettings```

- Create a virtual environment to retrieve the project's dependencies and packages.
*example procedure*: ```python -m venv .venv```
- Check with ```ls``` that you now have an .venv. If this is not the case, repeat this step, checking the syntax of the command line. Otherwise activate your new virtual environment.
  
    example procedure:
    - (PowerShell): ```.\.venv\Scripts\activate```
    - (Windows): ```.\.venv\Scripts\activate.bat```
    - (others): ```source .venv/bin/activate```

*If you encounter difficulties you can refer to the site:* https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789
  
  To check the success of this maneuver, you should have a ``(env)``` in front of your command line.

  PS: Just type ```deactivate``` to close it.

Finally, download with pip the packages and dependencies required for the correct functioning of the code with requirements.txt by entering the following command *(in your virtual environment!)*

```pip install -r requirements.txt```

Once the download is complete and the installation is complete, you are ready to run the code.

### Creation of the ```.env``` file
To ensure optimal security, sensitive data has not been integrated into the repository.
Please therefore create a file at the root of the project named: ```.env``` and put the following variables there:
```SECRET_KEY="the secret key of the project"```
```DSN="the sentry dsn key"```

> NOTES:
> The Sentry DSN key will be communicated to you by Sentry (*https://sentry.io/signup/*), when you create an account and create a project. You will only have to copy and paste the value of the DSN key.

### Run site
In the project directory with your ```.venv``` activated:
  - Type: `python manage.py runserver`
  - Go to `http://localhost:8000` in a browser.
  - Confirm that the site is working and navigable (you should see several profiles and locations).

### Run Linting
In order to manually test the project linting, position yourself in the root directory of the project and (```.venv``` activated) type:
- `flake8.`

### Run Tests
In order to manually test the project tests, position yourself in the root directory of the project and (```.venv``` activated) type:

- `pytest`

If you want to test the project with test coverage, you can use this command:

- ```pytest --cov=.```

And if you also want to generate a new test coverage html report, you can use this command:
- ```pytest --cov=. --cov-report html```

### Admin dashboard
- Run database migrations with ```python manage.py migrate```
- Create a superuser with ```python manage.py createsuperuser```
- Start the server with ```python manage.py runserver```
- Go to `http://localhost:8000/admin`
- Log in with the new superuser details or with user `admin`, password `Abc1234!`

## Deployment
The deployment has been automated so that each commit to the ```main``` branch of the repository results in the prior execution of several steps. These are managed using the CI-CD Pipeline (```.github/workflows/ci-cd.yml```).

Here is the chronological list of the Pipeline stages:
- Reproduction of the local development environment
- Checking code formatting (Linting)
- Triggering project tests
- Verification that test coverage is greater than 80%

If a step is invalid and returns an error, it will not execute the rest of the Pipeline. If all these steps are validated then the Pipeline will execute its last action which is the Containerization of the project with Docker:
- Creation of two Docker images:
  - a Docker image with the tag: ```latest``` (Latest stable version)
  - a Docker image with the last commit tag. (Allows you to better manage the version system)
- Push Docker images to DockerHub

Once the Pipeline has been executed correctly without error feedback, our images are available on DockerHub and our host Render automatically retrieves our Docker image: ```latest```, which keeps our project up to date.

> Note:
> the ``ci-cd-other.yml``` file concerns commits from other branches and therefore does not support changes to the main ``main``` branch!
> This file behaves in the same way as ```ci-cd.yml``` except that the Pipeline only performs the first 4 steps (from reproducing the environment to checking the test coverage).

### Prerequisites
- Your GitHub account
- Sentry account (*https://sentry.io/signup/*)
- Docker Hub account (*https://hub.docker.com/*)
- Render account (*https://render.com/*)

### Configuration step

> Note:
> Please have carefully followed the development step: ```Creation of an .env file```

#### 1 - Using GitHub Actions

Once you have created an account on DockerHub:

  - Go to the GitHub repository of the project that you will have previously pushed to your remote account.

  - Then click on ```Settings``` in the horizontal bar above your files.

  - In the left sidebar, select ```Secrets and variables``` then click on ```Actions```.

  - You can then at the base of the page (Secrets section), create new secret repositories. Please create the following secret variables:
    - DSN (Your Sentry DSN key)
    - SECRET_KEY (Your django secret key)
    - DOCKERHUB_USERNAME (Your DockerHub connection username)
    - DOCKERHUB_PASSWORD (Your password for a DockerHub connection)

  - Once done, create a new commit and push the project to your repository.

  - Go to your repository and click on Actions in the horizontal bar above the project. Normally you should notice two several things:
    - The first is that in the right sidebar, you have the two Pipelines ( ```ci-cd.yml``` & ```ci-cd-other.yml``` ).
    - By clicking on ```ci-cd.yml``` you should normally have two workflows.
      - A workflow (the first) which is green and therefore successful. It corresponds to the last commit that you have just made.
      - A workflow (the last) which is red and therefore which has failed. It corresponds to the first push that you perform before entering your secret variables in GitHub.
  
#### 2 - Render host configuration

Go to the Render hosting site and create an account. Different options are available to you, note that not using the ssh option, the free version is more than sufficient for the deployment to be successful. However, if you choose the free version, be aware that the services may require more time to operate.

Once your account is created:
  - Click on ```New``` then ```Web Service``` to create a new instance.
  - Choose the method: ```Deploy an existing image from a registry```
  - In Image Url, please enter the URL of your Docker image.
  - This done, you find yourself in front of your application logs. Once the message "Your service is live" appears in your logs, your application is online!
  - Retrieve in the settings of your application on Render, the private URL in Deploy Hook to create your secrets variable in github: RENDER_WEBHOOK. This will allow the ci-cd.yml Pipeline to automatically redeploy the latest Docker image update to Render.
  - Copy the address generated for the service by render and add it to the ```ALLOWED_HOSTS``` array in ```OrangeCountyLettings/settings.py```.
  - Commit and push the new updates to GitHub