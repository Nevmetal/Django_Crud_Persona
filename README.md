# Pasos para Correr a la App

App realizada con PostgreSQL y Django.

### Requerimientos:
- Tener la gestor de base de datos PostgreSQL
- Tener Python instalado en la maquina
- Tener Visual Studio Code (vscode)

**Ejecucion de la App**


Pasos:

1. Descargar el zip o clonar el repositorio
2. Crea el entorno virtual en vscode:

   En la **terminal** de vscode escribir:
  - pip install virtualenv (para instalar el entorno virtual)
  - virtualenv venv (para crear la carpeta del entorno virtual)
  - .\venv\Scripts\actívate (para activar el entorno virtual)
3. Instalar Django y la dependencias para utilizar PostgreSQL 
  - pip install django psycopg2-binary
4. Configurar la conexión de la BD para ello ir a la carpeta "mysite_person" el archivo "settings.py" buscar "DATABASE" (linea 77)
    
    `DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'DB_Persona',
    'USER': 'tu_usuario',
    'PASSWORD': 'tu_contraseña',
    'HOST': 'localhost',
    'PORT': '5432',
    }
    }`

5. Una vez configurado la conexión migrar la base de datos para ello ya debemos tener creado en PostgreSQL una base de datos llamada DB_Persona o con el nombre que le puso en la conexión 'NAME': 'DB_Persona':

 - python manage.py makemigrations (para obtener los cambios)
 - python manage.py migrate (para realizar la migración )


6. Y para Finalizar Correr el Server:
 - python manage.py runserver
