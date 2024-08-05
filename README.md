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

## Running the Application
1. Build the Docker image using the Dockerfile:
 `docker build -t patient-management-system .`
2. Start the container using the docker-compose.yml file:
 `docker-compose up -d`
4. Access the application in your browser:
 `http://localhost:8080`

### Running Locally

1. Ensure PostgreSQL is running and configured according to your `.env` file.

2. Run the application: `python -m src.app.app`

3. The application will be available at: `http://localhost:8080`.

## API Endpoints

- `POST /api/add-patient`: Add a new patient
- `GET /api/get-patient/<id>`: Get a patient by ID
- `PUT /api/update-patient`: Update patient information
- `GET /api/get-patients`: Get all patients
- `DELETE /api/delete-patient/<id>`: Delete a patient

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Tools 

- [Flask](https://flask.palletsprojects.com/): Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM for the database
- [Docker](https://www.docker.com/): Containerization
- [PostgreSQL](https://www.postgresql.org/): Database

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Jose Galindo - `juniorgala23@gmail.com`

Wpp: `+57 321 2927 430`

Link del Proyecto: [https://github.com/josegalindo23/patient-management-system](https://github.com/josegalindo23/patient-management-system.git)
