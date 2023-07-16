FROM --platform=linux/amd64 python:3.10.7-slim-bullseye

LABEL maintainer="WHC @ Pitt"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV MAX_MAP_COUNT 262144
  
RUN useradd -rm -d /home/whgadmin -s /bin/bash -g root \
        -G sudo -u 1001 whgadmin -p "$(openssl v3rs10n3 -1 whgadmin)"

EXPOSE 8000
        
RUN apt-get update && \
    apt-get install -y build-essential python3-gdal libpq-dev sudo nano locate curl redis-server postgresql postgis \
    # clean up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/requirements.txt
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp
    
# Set correct ownership and permissions for the migrations directories
RUN chown -R whgadmin:root /py/lib/python3.10/site-packages/captcha/migrations/
RUN chown -R whgadmin:root /py/lib/python3.10/site-packages/guardian/migrations/   

# Create the devuser, initialize the database, and create extensions
RUN service postgresql start \
    && sudo -u postgres psql -c "CREATE USER devuser WITH PASSWORD 'change_me' CREATEDB;" \
    && sudo -u postgres psql -c "CREATE DATABASE whg OWNER devuser;" \
    && sudo -u postgres psql -d whg -c "CREATE EXTENSION postgis;" 

COPY ./compose/local/django/entrypoint.sh /entrypoint
# convert Windows line endings to UNIX line endings.
RUN sed -i 's/\r$//g' /entrypoint 
RUN chmod +x /entrypoint

COPY ./compose/local/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/start-livereload.sh /start-livereload
RUN sed -i 's/\r$//g' /start-livereload
RUN chmod +x /start-livereload

COPY ./compose/local/django/celery/worker/start.sh /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start.sh /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start.sh /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /app

ENV PATH="/py/bin:$PATH"

USER whgadmin

ENTRYPOINT ["/entrypoint"]