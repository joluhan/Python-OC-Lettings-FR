# Using a base image
FROM python:3.12-slim-bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential \
  && pip install --no-cache-dir --upgrade pip
  
# Configure the Python environment to avoid creating .pyc (bytecode) files when running scripts.
ENV PYTHONDONTWRITEBYTECODE 1

# Disable buffering of standard and error output, which is recommended for Docker applications.
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy and install requirements.txt to the container's working directory
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt

# Copy the rest of your application's source code, if any to container's working directory
COPY . /app

# Collect static Django application files into a specified directory. Useful during deployment
RUN python manage.py collectstatic --noinput

# Inform Docker that the application is listening on port 8000
EXPOSE 8000

# Using Gunicorn to serve Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "OrangeCountyLettings.wsgi:application"]