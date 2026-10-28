# Reviewer stories

## 1. Filter the Review Queue
User story: As a reviewer, I want to filter the application queue by status, so that I can
prioritize edge cases and manage my workload efficiently.
Acceptance criteria:
1. Provides filter options by status.
2. "Needs Review" isolates human intervention cases.
3. "Verified" isolates clear-cut high-confidence cases.

## 2. Open and Inspect a Case
User story: As a reviewer, I want to open an application case and view the original
document side-by-side with the extracted data, so that I can easily verify its contents.
Acceptance criteria:
1. Opens detailed view showing original document preview next to parsed fields side-
by-side.
2. Highlights flagged discrepancies.

## 3. View AI Results, Confidence Score, and Explanation
User story: As a reviewer, I want to see the AI result (Verified, Needs Review, or
Rejected) with a confidence score and a written explanation, so that I can decide how
much to trust it.
Acceptance criteria:
1. Displays clear AI evaluation status.
2. Shows numerical confidence score.
3. Details written explanation for the conclusion.

## 4. View Rule and Source Citation
User story: As a reviewer, I want to see the specific rule and source citation used by the
system for an evaluation, so that I can verify the reasoning behind the automated check.
Acceptance criteria:
1. Displays matching rule snippet from local knowledge base.
2. Clicking citation opens full knowledge-base entry with its title and version date.

## 5. Confirm or Override with Comments
User story: As a reviewer, I want to confirm or override an AI recommendation and add a
mandatory comment explaining my decision, so that the outcome is well-documented
and defensible.
Acceptance criteria:
1. Select confirmation or custom override.
2. Requires mandatory text comment before saving.
3. Logs updated status and comment in audit trail.
