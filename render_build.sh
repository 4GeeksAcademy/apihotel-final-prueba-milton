#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias de Node
npm install
npm run build

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias de Python
pip install --upgrade pip
pip install -r requirements.txt

# Ejecutar migraciones
flask db upgrade
