# 4. Processing Data

The process of moving data from the Staging Database to the Master Data is handled via an internal GUI tool that allows administrators to validate and review submissions.

## Data Review
- Administrators access the Staging Database through an internal tool that displays pending submissions.
- Each submission is reviewed to ensure all required fields are present and accurate.
- Data related to contacts and patients is validated, including checks for duplicates and data consistency.

## Transfer to Master Database
- Once validated, the data is processed into the RettDB data model.
- For each submission, contact and patient records are created or updated in the master database.
- Relationships between contacts and patients are established (e.g., mother-daughter, legal guardian, etc.).

## Logic for Managing Data
- **Duplication Check**: During the processing phase, checks are performed to prevent duplicate patients or contacts from being added.
- **Relationship Management**: The system ensures that relationships between contacts and patients are correctly established, with the possibility of one contact being linked to multiple patients and vice versa.

## Error Handling
- In case of validation errors (e.g., missing required fields, invalid data), submissions can be flagged for further review.
- Administrators can request more information from the contact before completing the data transfer.
