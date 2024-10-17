# Security and Compliance

This section outlines the security and compliance measures for the Rett Syndrome Patient Registry, ensuring GDPR compliance and the protection of sensitive data.

## Authentication and Authorization
- **Backoffice Access**: Access to the backoffice is restricted to authorized personnel only, using Microsoft 365 authentication (or other OAuth systems).
- **Role-based Access Control (RBAC)**: Permissions are granted based on user roles, such as Admin or Data Manager, with different levels of access.

## GDPR Compliance
- **Data Minimization**: Only necessary data is collected from contacts and patients.
- **Explicit Consent**: All contacts must give explicit consent for data collection, as per GDPR requirements.
- **Right to Erasure**: Contacts and patients have the right to request their data be removed from the system.
- **Data Encryption**: All sensitive data (e.g., patient medical records, genetic information) is encrypted both in transit and at rest.

## File Handling
- **Secure Uploads**: Files uploaded (e.g., genetic reports) are stored in a secure environment, with access restricted to authorized personnel only.
- **Anonymization**: Personal identifiers are anonymized when used in reports or exports to protect patient and contact privacy.

## Data Retention
- Staging data is retained only until it is reviewed and transferred to the master database.
- Master data is retained indefinitely unless deletion is requested by a user or required by law.
