# pull official base image
FROM python:3.12.3-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
# RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy project and entrypoint.sh
COPY . /app/
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Collect static files
# RUN python manage.py collectstatic --noinput

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]