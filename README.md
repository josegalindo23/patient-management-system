# Patient Management System for Hospital (Basic)

This project is a backend application for the management of patients in a hospital, implemented with Python using a Clean Architecture.

## Features

- Full CRUD for patients
- RESTful API
- Clean Architecture
- Containerisation with Docker
- PostgreSQL database

## Prerequisites

- Python 3.12+
- Docker and Docker Compose
- PostgreSQL (if running outside of Docker)

## Configuration

1. Clone the repository:
` https://github.com/josegalindo23/patient-management-system.git`
2. Navigate to the project directory:
 `cd patient-management-system`

## Ejecución
1. Build the Docker image using the Dockerfile:
 `docker build -t patient-management-system .`
2. Start the container using the docker-compose.yml file:
 `docker-compose up -d`
4. Access the application in your browser:
 `http://localhost:8080`

### Localmente

1. Asegúrate de tener PostgreSQL en ejecución y configurado según tu archivo `.env`.

2. Ejecuta la aplicación: `python -m src.app.app`

3. La aplicación estará disponible en: `http://localhost:8080`.

## API Endpoints

- `POST /api/add-patient`: Añadir un nuevo paciente
- `GET /api/get-patient/<id>`: Obtener un paciente por ID
- `PUT /api/update-patient`: Actualizar información de un paciente
- `GET /api/get-patients`: Obtener todos los pacientes
- `DELETE /api/delete-patient/<id>`: Eliminar un paciente

## Desarrollo

Para contribuir al proyecto:

1. Crea un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Herramientas utilizadas

- [Flask](https://flask.palletsprojects.com/): Framework web
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM para la base de datos
- [Docker](https://www.docker.com/): Containerización
- [PostgreSQL](https://www.postgresql.org/): Base de datos

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Jose Galindo - juniorgala23@gmail.com

Link del Proyecto: [https://github.com/josegalindo23/patient-management-system](https://github.com/josegalindo23/patient-management-system.git)
