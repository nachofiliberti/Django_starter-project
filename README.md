# Django Started Project

Este proyecto es una aplicación web creada con Django para aprender sobre el desarrollo web con este framework. Incluye autenticación de usuarios, gestión de productos, reseñas y comentarios, y más.

## Funcionalidades

- **Gestión de Usuarios**: Registro e inicio de sesión.
- **Vistas Basadas en Clases**: Implementación de vistas estructuradas.
- **Modelos de Datos**: Ejemplos de varios modelos de datos con sus relaciones.
- **Plantillas**: Uso de plantillas para renderizar el contenido.
- **Permisos**: Roles de usuario para staff y no staff.

## Requisitos

- Python 3.x
- Django 3.x
- Virtualenv (recomendado)

## Instalación

Sigue estos pasos para instalar y configurar el proyecto localmente.

### 1) Clonar el Repositorio

git clone git@github.com:nachofiliberti/Django_starter-project.git
cd Django_starter-project

### 2) Crear y Activar un Entorno Virtual
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`

### 3) Instalar Dependencias
pip install -r requirements.txt

### 4) Configurar la Base de Datos y Crear un Superusuario
python manage.py migrate
python manage.py createsuperuser

### 5) Ejecutar el Servidor de Desarrollo
python3 manage.py runserver

### 6)Accede a la aplicación en tu navegador:

http://127.0.0.1:8000
