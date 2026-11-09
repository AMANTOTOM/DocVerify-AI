# DocVerify AI

DocVerify AI is a web application that helps German universities check the application documents of international students. It compares the documents with admission rules and shows the result with sources and a confidence score. A human reviewer always makes the final decision.

Course project for MIT 5.2 - Senior IT Project.

## Status

Phase 2: Git workflow and backend skeleton in progress.

## How to run the backend

1. Go to the backend folder:
   ```bash
   cd backend
   ```
2. Install the packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   python -m uvicorn main:app --reload
   ```
4. Open http://127.0.0.1:8000 in your browser. You should see a message that the backend is running.

## Run with Docker

Start the backend and MongoDB together:

```bash
docker compose up --build
```

The API is then available at http://localhost:8000/docs

Stop everything with `docker compose down`.

## this is the project structure

- `backend/` - the Python (FastAPI) backend
- `docs/` - project documents: motivation, vision, personas, scenarios, user stories and features

## following are my lanned tech stack

Python, FastAPI, MongoDB, Docker

## Backlog

The backlog is on git (https://github.com/users/AMANTOTOM/projects/2).