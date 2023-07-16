#!/bin/bash

# Activate the virtual environment
source /py/bin/activate

# Change to the project directory
cd /app

# Start the livereload server
python manage.py livereload
