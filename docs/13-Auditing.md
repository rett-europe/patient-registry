# Auditing and Compliance

To meet regulatory requirements and ensure the integrity of the data in the Rett Syndrome Patient Registry, the system includes a comprehensive auditing mechanism. This system records all key actions, submissions, and data changes in a traceable and immutable manner, ensuring full accountability and compliance with relevant regulatory frameworks.

## Key Auditing Features

### 1. **Audit Trail for Data Submissions**
- **Survey Responses**: Every survey submission is logged with the following information:
  - Contact's identity (verified through token and/or two-factor authentication).
  - Patient associated with the submission.
  - Timestamp of the submission.
  - Details of the survey completed.
  
- **File Uploads**: For every file uploaded by a contact, the audit trail records:
  - Contact's identity.
  - The patient to whom the file is linked.
  - File type and timestamp.
  - The extracted data (e.g., MECP2 mutation) and processing status.
  
- **Backoffice Operations**: Any action performed by an administrator in the backoffice (CRUD operations on contacts, patients, or relationships) is logged with:
  - Administrator's identity.
  - The action performed (e.g., create, update, delete).
  - Entity involved (contact, patient, relationship).
  - Timestamp of the action.

### 2. **Audit Logs for User Access**
- **Login and Authentication Events**: All access to the backoffice system is logged, including:
  - User identity (via Microsoft 365 authentication).
  - Time of login.
  - Success or failure of the login attempt.
  
- **Two-Factor Authentication (2FA)**: When 2FA is used (e.g., for survey responses), the verification process is logged with details of the authentication step (e.g., SMS code sent and verified).

### 3. **Immutable Logs**
- All audit logs are immutable, meaning they cannot be altered or deleted by any user, including administrators.
- Logs are stored securely and can only be accessed by authorized personnel with audit privileges.

### 4. **Regulatory Compliance**
- **GDPR**: The system ensures full compliance with GDPR by logging all actions related to data submission, access, and deletion requests from contacts or patients.
- **HIPAA** (if applicable): For healthcare-related data, the system adheres to the Health Insurance Portability and Accountability Act (HIPAA), ensuring data security and privacy.

### 5. **Data Retention Policies**
- Audit logs are retained for a specified period, as required by applicable regulations (e.g., GDPR, HIPAA).
- After the retention period, logs can be archived but must still remain accessible for auditing purposes when required by law.

## Audit Review and Reporting

- **Regular Audits**: Administrators or authorized audit personnel can generate audit reports periodically to review system activity and ensure compliance.
- **Regulatory Reports**: The system supports the generation of detailed audit reports to be shared with regulatory bodies during inspections or audits.

## Audit Logs and External Integrations
- Logs can be exported for integration with external compliance tools or platforms, enabling further review and analysis by third-party auditors or legal teams.

## Data Security for Audit Logs
- **Encryption**: All audit logs are encrypted both at rest and in transit.
- **Access Control**: Only authorized personnel with specific audit roles have access to the logs.
- **Regular Backups**: Logs are backed up regularly to ensure that no data is lost.