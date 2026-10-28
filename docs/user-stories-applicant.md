# User Stories: Applicant

## 1. Document Upload
User story: As an applicant, I want to upload application documents such as transcripts,
language certificates, and degree certificates in PDF, PNG, or JPG format up to 10 MB,
so that I can submit all my required paperwork in one place.
Acceptance criteria:
1. Accepts standard formats under 10 MB.
2. Rejects files over 10 MB with an error.
3. Successfully uploaded files appear in the list with a "Submitted" status.

## 2. Document Checklist Presence Check
Userstory: As an applicant, I want the system to check my uploaded files against the
required document checklist for my chosen program, so that I can know I haven't missed
any vital requirements.
Acceptance criteria:
1. Checks uploaded files against checklist requirements.
2. Highlights missing mandatory items.
3. Updates overarching checklist status when all items are present.

## 3. APS Certificate Digital Seal Check
User story: As an applicant, I want the system to check that my mandatory APS
certificate is uploaded as a PDF with an intact digital seal, so that I know my APS
certificate will be accepted.
Acceptance criteria:
1. Detects whether an APS certificate PDF file is uploaded.
2. Checks that the file carries an intact digital seal.
3. Marks presence status as verified if valid, or flags as missing/invalid otherwise.

## 4. Knowledge-Base and Anabin Institution Check
User story: As an applicant, I want the system to check my university against its internal
knowledge base of recognized institutions, so that I can see if my degree institution
meets the criteria.
Acceptance criteria:
1. Matches institution name against local knowledge base.
2. Exact match marks institution as recognized.
3. Closed matches are successfully mapped for confirmation.
4. Unmatched institutions are flagged as "Needs Review".

## 5. Grade Extraction and Estimation
User story: As an applicant, I want the system to extract my grades and show an
estimated conversion to the German scale using the modified Bavarian formula, so that I
can understand how my qualifications translate.
Acceptance criteria:
1. Extracts numerical grades.
2. Retrieves best/lowest passing grades from document or knowledge base.
3. Flags grade as "Needs Review" if boundaries are missing.
4. Converts grades using the modified Bavarian formula.
5. Displays result as an estimate, not an official grade.
6. Flags unreadable text for manual review.

## 6. Blurry Scan and Error Feedback
User story: As an applicant, I want to receive clear feedback when a document scan is
too blurry or unreadable, so that I can upload a corrected version before the deadline.
Acceptance criteria:
1. Assigns "Needs Review" status to illegible scans.
2. Displays human-readable reason.
3. Allows file replacement.
4. Automatically triggers re-check and updates status upon replacement.

## 7. User Registration and Login
User story: As an applicant, I want to register for an account and log in securely, so that
my personal application data remains private and accessible only to me.
Acceptance criteria:
1. Creates account via email/password.
2. Secure login grants dashboard access.
3. Invalid credentials deny access.

## 8. Application Status Tracking
User story: As an applicant, I want to see the status of each individual document and my
overall application, so that I can avoid radio silence and know if anything needs my
attention.
Acceptance criteria:
1. Dashboard shows document-level status like - - -: Submitted, Verified, Needs Review
2. Overall status shows completeness.
3. Status updates appear within 1 minute of a check finishing or on page refresh.

## 9. Account and Data Deletion (Privacy / GDPR)
User story: As an applicant, I want to delete my account and all associated documents,
so that my personal data can be removed in compliance with privacy regulations.
Acceptance criteria:
1. Profile settings provide delete account option.
2. Permanently erases account and active documents.
3. Removes or anonymizes personal data stored within audit logs.
4. Displays success confirmation.
