# Auditing and Compliance

To ensure regulatory compliance and data integrity, the Rett Syndrome Patient Registry maintains a comprehensive auditing system. All actions related to data submission, file uploads, user access, backoffice operations, OpenAI processing, and doctor validation are logged, providing full traceability and accountability.

---

## Key Auditing Features

### 1. **Survey Responses**
- Every survey submission is logged with the following information:
  - Contact's identity (verified through token and/or two-factor authentication).
  - Patient associated with the submission.
  - Timestamp of the submission.
  - Details of the survey completed.
  - Authentication logs (2FA verification if used).
- **Immutable Logs**: Once a survey is submitted, all related logs are stored in an immutable format to ensure they meet regulatory requirements.

### 2. **File Uploads and Data Processing**
- For every file uploaded by a contact, the audit trail records:
  - Contact identity (verified through token or 2FA).
  - The patient to whom the file is linked.
  - File type, upload timestamp, and extraction status.
  - Details of the extracted data (e.g., MECP2 mutation) and the file's deletion status.
- **Processing Logs**: OpenAI processing is logged to track:
  - When the file was processed.
  - What data was extracted.
  - The deletion of the original file after processing is completed.

### 3. **Doctor Review and Validation**
- When a doctor is requested to validate a diagnosis based on an uploaded report, the audit trail captures:
  - The identity of the doctor accessing the report.
  - The timestamp when the report was accessed.
  - Any diagnosis validation or notes provided by the doctor.
  - Confirmation that the validation or feedback has been stored in the system.

### 4. **Backoffice Operations**
- All CRUD operations performed by administrators are logged, including:
  - Administrator's identity.
  - Action performed (e.g., create, update, delete).
  - Entity involved (contact, patient, relationship).
  - Timestamp of the action.
- **Access Logs**: Every login or access to the backoffice system is logged, including:
  - User identity.
  - Timestamp of access.
  - Success or failure of login attempts.

### 5. **User Access and Management**
- **Login Events**: Every login event is tracked, logging:
  - User's identity.
  - Login timestamp.
  - Authentication status (success or failure).
- **Role Changes**: Any modifications to user roles are logged, including:
  - User who made the change.
  - User whose role was changed.
  - Timestamp of the role modification.
- **Activity Logs**: Every action taken by administrators or other authorized users is logged to ensure full accountability.

### 6. **Report Generation and Exports**
- **Report Logs**: Every time a report is generated, the following information is logged:
  - User who generated the report.
  - Date and time of the report generation.
  - Type of report (e.g., patient demographics, mutation data).
  - Whether the report was exported (e.g., to CSV or PowerBI).

---

## Regulatory Compliance

The auditing system is designed to ensure full compliance with various regulations, including:
- **GDPR**: All access and data management actions are logged, ensuring that data processing is transparent and auditable.
- **HIPAA** (if applicable): All interactions with patient data are logged and protected, ensuring compliance with healthcare-related regulations.
- **Consent Tracking**: For all sensitive actions (e.g., data submission, file uploads), consent logs are maintained to prove compliance with privacy laws.

---

## Data Security for Audit Logs

- **Immutable Logs**: Audit logs are immutable, meaning they cannot be altered or deleted.
- **Encryption**: All audit logs are encrypted both at rest and in transit to ensure they are securely stored.
- **Access Control**: Only authorized personnel with specific auditing privileges can view or generate audit reports.
- **Regular Backups**: Audit logs are backed up regularly to prevent data loss and ensure availability during audits.

---

## Data Retention Policies

- Audit logs are retained for a period specified by regulatory requirements (e.g., GDPR, HIPAA).
- After the retention period, logs may be archived but will remain accessible for legal or regulatory audits.
- All audit data will be securely deleted after the legally required retention period if no further use is mandated.

---

## Audit Review and Reporting

- **Audit Reports**: Administrators or authorized personnel can generate detailed audit reports to review all activities, ensuring compliance.
- **External Review**: The system supports exporting audit logs for review by external auditors or regulatory bodies.