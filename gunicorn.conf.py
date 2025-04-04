import os
import sys

# Agregar el directorio src al path de Python
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

# Configuración de Gunicorn
bind = "0.0.0.0:10000"
workers = 4
timeout = 120 