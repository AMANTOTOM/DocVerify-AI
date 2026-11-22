# Sprint documentation

Project: DocVerify AI, an AI document verification web app for German university admissions.
Developer: Anto Tom
Method: Kanban board (Todo, In Progress, Done) combined with short sprints, tracked as milestones on GitHub.
Board: https://github.com/users/AMANTOTOM/projects/2
Repository: https://github.com/AMANTOTOM/DocVerify-AI

## Product backlog

The backlog is the list of issues from the Phase 1 product definition. It is ordered by priority and lives on the project board.

Phase 2 items (non-AI core): user registration, login and roles, document upload and storage, review dashboard, administration, Docker, CI, tests, sprint documentation and README.
Later phases (AI extraction, validation, evaluation) stay in the backlog as Todo.

## Sprint 1 (6 Nov to 9 Nov 2026)

### Planning
Goal: a working repository with a backend skeleton, a README, Docker and a first CI pipeline.
Selected work: backend folder, minimal FastAPI app, README, Dockerfile, docker compose, GitHub Actions build.
Capacity: 4 to 6 hours in the evenings.

### Review
Done: #19 backend folder, #20 simple backend, #21 project README, #22 Dockerfile, #23 docker compose, #24 GitHub Actions build.
Not done: nothing planned was left open.

### Retrospective
Went well: small pull requests, every step tested locally before the commit, Docker and CI running early.
Went badly: pull request reviews and the board were not kept up to date during the sprint. I added the reviews later. There was also a break after this sprint until 17 Nov.
Change: keep the board current and write the PR review on the same day as the merge.

## Sprint 2 (16 Nov to 19 Nov 2026)

### Planning
Goal: vector database service, linting and tests in CI, and the first user features.
Selected work: Qdrant, ruff and pytest in CI, registration, login, roles.
Capacity: <2-4 hours at night>.

### Review
Done: #25 Qdrant, #26 linting and first test in CI, #27 user registration, #28 login with token, #29 roles and protected routes.
Not done: nothing planned was left open.

### Retrospective
Went well: ruff found style problems before they reached main, and secrets are handled with an environment variable and a .env file that is never committed.
Went badly: one commit landed on main instead of a feature branch and had to be moved. The board was still not updated.
Change: protect the main branch so changes can only come through a pull request (done on 21 Nov) and update the board every day.

## Sprint 3 (20 Nov to 21 Nov 2026)

### Planning
Goal: the two core features that use documents.
Selected work: document upload with validation, reviewer dashboard endpoints.
Capacity: <2-4 hr per day>.

### Review
Done: #30 document upload, #31 reviewer dashboard endpoints.
Not done: administration, automated integration tests and the frontend were moved to Sprint 4.

### Retrospective
Went well: upload checks file type, size and empty files, and reviewer routes are protected by role.
Went badly: testing by hand in the API docs was slow.
Change: write automated integration tests so every flow is checked on every pull request.

## Sprint 4 (22 Nov 2026)

### Planning
Goal: finish Phase 2: administration, automated tests, frontend container, documentation.
Selected work: admin functions, unit and integration tests in CI, frontend container, sprint documentation, final README, final checks.
Capacity: <4-6 hours>.

### Review
Done: #32 admin functions and first admin setup, #33 unit and integration tests in CI, #34 frontend container. Sprint documentation and final README are in the pull requests of this sprint.
Not done: AI features (Phase 3).

### Retrospective
Went well: the integration tests found a real bug in the registration route that came from the admin pull request, and it was fixed in the same sprint. All four services start with one command.
Went badly: the admin feature was merged before the tests existed, and a line break error in the CI file blocked the checks for a while.
Change for Phase 3: write the tests together with the feature, not afterwards.

## Individual contribution log

I worked alone, so  each pull request has my self-review comment.The dates are merge dates of the pull requests.

| Date | Sprint | PR | What I did |
| --- | --- | --- | --- |
| 6 Nov | 1 | #19 | Added the backend folder with a short description |
| 8 Nov | 1 | #20 | Added a simple backend that says it is running |
| 8 Nov | 1 | #21 | Added the project README |
| 9 Nov | 1 | #22 | Added a Dockerfile for the backend |
| 9 Nov | 1 | #23 | Added docker compose |
| 9 Nov | 1 | #24 | Added a GitHub Actions workflow that builds the backend |
| 18 Nov | 2 | #25 | Added the Qdrant vector database |
| 18 Nov | 2 | #26 | Added linting and the first test to CI |
| 18 Nov | 2 | #27 | Added user registration |
| 18 Nov | 2 | #28 | Added login with token |
| 18 Nov | 2 | #29 | Added roles and protected routes |
| 21 Nov | 3 | #30 | Added document upload |
| 21 Nov | 3 | #31 | Added reviewer dashboard endpoints |
| 22 Nov | 4 | #32 | Added admin functions and first admin setup |
| 22 Nov | 4 | #33 | Added unit and integration tests to CI |
| 22 Nov | 4 | #34 | Added the frontend container with a simple web page |


## Phase 3 sprint plan (AI features)

Phase 3 is due on 13 December. The last sprint ends on 10 December, so 11 to 13 December are a buffer for fixes, documentation and the final checks. No new features are started in the buffer.

| Sprint | Dates | Issues | Goal |
| --- | --- | --- | --- |
| Sprint 5 | 23 to 28 Nov | #2, #6 | Read text from uploaded documents (OCR), check the document checklist, detect blurry scans |
| Sprint 6 | 29 Nov to 4 Dec | #3, #4, #5, #16 | Extract data with an LLM, knowledge base in Qdrant, institution and seal checks |
| Sprint 7 | 5 to 10 Dec | #12, #13, #14, #17, #18 | RAG check with source citation, AI view for reviewers, confirm or override, audit log, AI settings |
| Buffer | 11 to 13 Dec | none | Fixes, README, sprint documents, final checks, submission |