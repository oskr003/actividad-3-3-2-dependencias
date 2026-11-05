FROM python:3.9-slim

WORKDIR /app

# Instalar pipenv
RUN pip install --no-cache-dir pipenv

# Copiar definiciones de dependencias
COPY Pipfile Pipfile.lock requirements.txt ./

# Instalar dependencias usando pipenv
RUN pipenv install --deploy --system

# Copiar el codigo de la aplicacion
COPY app.py test_app.py ./

EXPOSE 5000

CMD ["python", "app.py"]
