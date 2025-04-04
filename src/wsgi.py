# This file was created to run the application on heroku using gunicorn.
# Read more about it here: https://devcenter.heroku.com/articles/python-gunicorn

import os
import sys

# Agregar el directorio actual al path para que Python pueda encontrar los módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Importar la aplicación
from app import app as application

if __name__ == "__main__":
    application.run()

