Application deployment and management procedures
========================================================

Deployment :
-------------
The deployment was automated so that each commit on the ``main`` branch
of the repository requires the execution of several steps beforehand.
These are managed using the CI-CD Pipeline (``.github/workflows/ci-cd.yml``).

Here is the chronological list of the Pipeline stages:
    - Reproduction of the local development environment
    - Checking code formatting (Linting)
    - Triggering project tests
    - Verification that test coverage is greater than 80%

If a step is invalid and returns an error, it will not execute the rest of the Pipeline.
If all these steps are validated then the Pipeline will execute its last action
which is the Containerization of the project with Docker:

    - Creation of two Docker images:
    - A Docker image with the tag: ``latest`` (Latest stable version)
    - A Docker image with the last commit tag. (Allows you to better manage the version system)
    - Push Docker images to DockerHub

Once the Pipeline has been executed correctly without returning errors,
the images are therefore available on DockerHub and the host Render 
automatically recovers the Docker image: ``latest`` , which keeps the project up to date.

The ``ci-cd-other.yml`` file concerns commits from other branches and therefore
does not support changes to the main ``main`` branch!
This file behaves in the same way as ``ci-cd.yml`` except that the Pipeline
only performs the first 4 steps
(from reproducing the environment to verifying test coverage).

Prerequisites:
---------------

- Your GitHub account
- Sentry account (*https://sentry.io/signup/*)
- Docker Hub account (*https://hub.docker.com/*)
- Render account (*https://render.com/*)

Configuration step:

Normally you should have already created a ``.env`` file during project initialization.
at the root of the project. If this is not the case, then do so in order to ensure optimal security,
sensitive data has not been integrated into the repository.
So create a file named at the root of the project: ``.env`` and put the following variables there:

``SECRET_KEY = "the secret key of the project"``

``DSN = "the sentry dsn key"``

The Sentry DSN key will be communicated to you by Sentry (*https://sentry.io/signup/*),
when you have created an account and created a project.
You will only have to copy and paste the value of the DSN key.

1 - Using GitHub Actions:
-----------------------------------

Once you have created an account on DockerHub:

  - Go to the GitHub repository of the project that you will have previously pushed to your remote account.

  - Then click on ```Settings``` in the horizontal bar above your files.

  - In the left sidebar, select ``Secrets and variables`` then click on ``Actions``.

  - You can then at the base of the page (Secrets section), create new secret repositories:
            - DSN (Your Sentry DSN key)
            - SECRET_KEY (Your django secret key)
            - DOCKERHUB_USERNAME (Your DockerHub connection username)
            - DOCKERHUB_PASSWORD (Your password for a DockerHub connection)

  - Once done, create a new commit and push the project to your repository.

  - Go to your repository and click on Actions in the horizontal bar above the project.
    Normally you should notice the following things:
        - The first is that in the right sidebar, you have the two Pipelines ( ``ci-cd.yml`` & ``ci-cd-other.yml`` ).
        - By clicking on ``ci-cd.yml`` you should normally have two workflows.
        - A workflow (the first) which is green and therefore successful. It corresponds to the last commit you just made.
        - A workflow (the last) which is red and therefore which has failed.
          It corresponds to the first push that you perform before entering your secret variables in GitHub.


2 - Configuration of the Render host:
-----------------------------------------

Go to the Render hosting site and create an account.
Different options are available to you, note that not using the ssh option,
the free version is more than sufficient for deployment to be successful.
However, if you choose the free version, be aware that the services may
require more time to operate.

Once your account is created:
  - Click ``New`` then ``Web Service`` to create a new instance.
  - Choose the method: ``Deploy an existing image from a registry``
  - In Image Url, please enter the URL of your Docker image.
  - This done, you find yourself in front of your application logs.
    Once the message ``Your service is live`` appears in your logs,
    your application is online!
  - Retrieve in the settings of your application on Render, 
    the private URL in Deploy Hook to create your secrets 
    variable in github: RENDER_WEBHOOK. This will allow the 
    ci-cd.yml Pipeline to automatically redeploy the latest 
    Docker image update to Render.
  - Copy the address generated for the service by render and 
    add it to the ``ALLOWED_HOSTS`` array in ``OrangeCountyLettings/settings.py``.
  - Commit and push the new updates to GitHub
