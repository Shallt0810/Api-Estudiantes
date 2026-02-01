Este proyecto implementa una API REST para la gestión de estudiantes utilizando FastAPI, SQLite, Uvicorn, Pydantic, etc.
La API permite realizar operaciones CRUD completas sobre el recurso Student, aplicando validaciones estrictas, con manejo de errores HTTP y prácticas de diseño REST.

El proyecto está estructurado siguiendo principios de separación de responsabilidades, arquitectura y estándares de codificación en inglés, facilitando su mantenimiento.

Requisitos Previos

-Python 3.10 o superior
-pip
-Git (opcional)

Este proyecto fue creado localmente. No es necesario clonar un repositorio
para ejecutarlo.


Si desea instalarlo, debe seguir los siguientes pasos en cmd:

1. Instalación

Clonar el repositorio:
git clone [https://github.com/Shallt0810/Api-Estudiantes.git]

2. Crear y activar entorno virtual:

cd //direccion donde este el proyecto//

Para activar el entorno, puede usar
-Si es windows:
python -m venv venv
venv\Scripts\activate

-Si es Linux/MacOs:
python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias:

pip install -r requirements.txt


Ahora, para hacer uso del proyecto ejecutar los siguientes comandos:

1. python -m app.database.init_db

Esto accionara lo siguiente:

-Crear la base de datos
-Generar la tabla students
-Insertar 10 registros de prueba

2. uvicorn app.main:app --reload

Esto para dar inicio al servidor, para entrar, la API estara disponible en: #http://127.0.0.1:8000# (Caso contrario, acceder a: http://127.0.0.1:8000/docs)

Endpoints Disponibles

-Obtener lista de estudiantes
GET /api/students

-Obtener estudiantes (con paginación)
GET /api/students/students-per-page

-Obtener estudiante por ID
GET /api/students/{student_id}

-Crear estudiante
POST /api/students

-Actualizar estudiante
PUT /api/students/{student_id}

-Eliminar estudiante
DELETE /api/students/{student_id}

Body (JSON):

{
  "id"
  "first_name": 
  "last_name": 
  "email": 
  "major": 
  "gpa": 
  "semester": 
  "enrollment_date": 
}

Validaciones Implementadas

Email= Formato válido - Debe ser único (409 Conflict)

GPA= Rango permitido: 0.0 – 4.0

Semester= Número entero entre 1 y 12

Campos requeridos= first_name, last_name, email, major, enrollment_date

Manejo de Errores HTTP

Código	Descripción
 400	Bad Request – datos inválidos
 404	Not Found – recurso no existe
 409	Conflict – email duplicado
 500	Internal Server Error

Las respuestas siguen un formato JSON.

Estándares de Codificación

- Código completamente en inglés
- Nombres descriptivos para variables, funciones y archivos

Separación entre: Rutas, Controladores, Modelos, Validaciones, Configuración de base de datos

Uso de IA (Obligatorio)

Herramientas de IA utilizadas

ChatGPT (OpenAI) y Geminis (Google)

Uso dentro del proyecto

-Diseño inicial de la arquitectura del proyecto (ChatGPT)
-Generación de ejemplos de endpoints REST (ChatGPT y Geminis)
-Apoyo en validaciones de datos y manejo de errores (Geminis)
-Asistencia en configuración de FastAPI y SQLite (ChatGPT y Geminis)

-Soporte en la documentación técnica (README) (CHatGPT)

Adaptación y mejoras realizadas

El código generado fue revisado, corregido y adaptado manualmente
Se ajustaron validaciones para cumplir requisitos académicos
Se reestructuró el proyecto para cumplir la arquitectura solicitada
Se añadio paginación personalizada