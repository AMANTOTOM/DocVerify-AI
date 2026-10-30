# Administrator stories

## 1. Manage User Roles

	•	User story: As an administrator, I want to manage user accounts and assign roles (Applicant, Reviewer, Admin), so that system access is properly restricted and secure.
	•	Acceptance criteria:
	1.	Displays searchable list of user accounts.
	2.	Admin can modify assigned roles.
	3.	Changes take effect immediately.
	4.	A user without the Admin role cannot open or access the user management page.

## 2. Add, Edit, and Remove Knowledge-Base Entries

	•	User story: As an administrator, I want to add, edit, and remove entries in the local knowledge base, so that the system evaluates applications using up-to-date guidelines.
	•	Acceptance criteria:
	1.	View, add, edit, or remove rule entries.
	2.	Invalid syntax triggers explicit error messages.
	3.	Every knowledge-base entry must include a title, a type, and a version date.
	4.	After an entry is changed, the RAG index is automatically rebuilt so the new version is used for subsequent checks.

## 3. View Audit Log

	•	User story: As an administrator, I want to view the system audit log, so that I can track administrative actions and compliance records.
	•	Acceptance criteria:
	1.	Chronological view of system/user actions.
	2.	Records timestamps, user IDs, and action types.
	3.	Protected and restricted to admin privileges.

## 4. Configure AI Service

	•	User story: As an administrator, I want to configure the external AI service endpoint and API keys, so that the system can connect to the chosen LLM backend.
	•	Acceptance criteria:
	1.	Input fields for connection parameters and model names.
	2.	Encrypted storage of API keys.
	3.	Test connection verification button.
