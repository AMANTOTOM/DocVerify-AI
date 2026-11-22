# DocVerify AI

DocVerify AI is a web application for checking application documents for German university admissions. Applicants upload their documents, reviewers check them, and administrators manage users. Phase 2 delivers the complete non-AI core. The AI features (OCR, language model, retrieval with a vector database) follow in Phase 3.

## Status

- Phase 1 (product definition): done, see the `docs` folder
- Phase 2 (core application, Docker, CI, agile process): done
- Phase 3 (AI extraction and validation): planned

## Tech stack

- Backend: Python 3.12, FastAPI
- Database: MongoDB 7
- Vector database: Qdrant (prepared for Phase 3)
- Frontend: plain HTML and JavaScript served by nginx
- Containers: Docker and Docker Compose
- CI: GitHub Actions (build, ruff, pytest)

## Requirements

- Docker Desktop (running)
- Git

## Setup

1. Clone the repository:

        git clone https://github.com/AMANTOTOM/DocVerify-AI.git
        cd DocVerify-AI

2. Create your local settings file from the example:

        copy .env.example .env

3. Open `.env` and set the two values:

        SECRET_KEY=<a long random text>
        ADMIN_EMAIL=<the email you will register with as the first admin>

   A random secret can be created with `python -c "import secrets; print(secrets.token_hex(32))"`.
   The `.env` file is never committed. `.env.example` only shows the names.

4. Start everything with one command:

        docker compose up --build

5. Open the application:

| What | Address |
| --- | --- |
| Web page | http://localhost:3000 |
| API documentation | http://localhost:8000/docs |
| MongoDB | localhost:27017 |
| Qdrant | http://localhost:6333 |

6. Stop everything with `docker compose down`. Add `-v` to also delete the stored data.

## Environment variables

| Name | Purpose |
| --- | --- |
| `SECRET_KEY` | Signs the login tokens. Required. |
| `ADMIN_EMAIL` | The user who registers with this email becomes the first administrator. |
| `MONGO_URL` | Database address. Set to the MongoDB container by docker compose. |

## Roles

| Role | What the role can do |
| --- | --- |
| Applicant | Register, log in, create applications, upload documents, see own applications |
| Reviewer | See all applications, approve or reject each document with a comment, set the application status |
| Administrator | Everything a reviewer can do, plus list users, change roles and delete users |

New users are applicants. The first administrator is the user who registers with `ADMIN_EMAIL`. After that, administrators change roles (for example to create a reviewer).

## Document upload rules

- File types: PDF, JPG and PNG
- Maximum size: 10 MB per file, empty files are refused
- Document types: degree certificate, transcript, language certificate, passport, cv, other
- One application can have several documents, and each upload can contain several files
- Files are stored in a Docker volume, details are stored in MongoDB

## API endpoints

| Method | Path | Who | Purpose |
| --- | --- | --- | --- |
| POST | `/register` | anyone | Create an account |
| POST | `/login` | anyone | Get a login token |
| GET | `/me` | logged in | Show own email and role |
| POST | `/applications` | applicant | Create an application |
| GET | `/applications` | applicant | List own applications with documents |
| POST | `/applications/{id}/documents` | applicant | Upload documents to an application |
| GET | `/review/applications` | reviewer, admin | List all applications |
| GET | `/review/applications/{id}` | reviewer, admin | Show one application with its documents |
| PATCH | `/review/documents/{id}` | reviewer, admin | Approve or reject a document |
| PATCH | `/review/applications/{id}` | reviewer, admin | Set the application status |
| GET | `/admin/users` | admin | List users |
| PATCH | `/admin/users/{email}/role` | admin | Change a user's role |
| DELETE | `/admin/users/{email}` | admin | Delete a user |

The full interactive documentation is at http://localhost:8000/docs.

## Running the tests

The integration tests need MongoDB, so start it first:

    docker compose up -d mongo
    cd backend
    pip install -r requirements-dev.txt
    ruff check .
    pytest -v

## Continuous integration

GitHub Actions runs on every pull request and on every push to `main`:

- `build-backend`: builds the backend Docker image
- `build-frontend`: builds the frontend Docker image
- `lint-and-test`: runs ruff, the unit tests and the integration tests (with a MongoDB container)

The checks must be green before a pull request can be merged.

## Project structure

    backend/             FastAPI application, tests and Dockerfile
    frontend/            Web page, nginx settings and Dockerfile
    docs/                Phase 1 documents and docs/sprints.md
    .github/workflows/   CI pipeline
    docker-compose.yml   All services (backend, frontend, MongoDB, Qdrant)
    .env.example         Names of the required settings

## Documentation

- Sprint documentation (backlog, planning, review, retrospective, contribution log): [docs/sprints.md](docs/sprints.md)
- Project board: https://github.com/users/AMANTOTOM/projects/2

## Data

Only synthetic data is used. Do not upload real personal documents.

## Git workflow

Every change is made on a feature branch and merged through a pull request. The `main` branch is protected. Each pull request has a description, a self-review comment and green checks. Issues are linked to pull requests, and sprints are tracked as milestones.