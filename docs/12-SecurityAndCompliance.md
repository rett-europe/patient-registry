# 12. Security and Compliance

This section outlines the security and compliance measures for the Rett Syndrome Patient Registry, ensuring GDPR compliance and the protection of sensitive data.

## Authentication and Authorization
- **Private Area for Contacts**: Contacts must authenticate via Auth0 to access their private area, where they can view and manage patient information, upload files, and complete surveys.
- **Backoffice Access**: Access to the backoffice is restricted to authorized personnel only, using Microsoft 365 authentication (or other OAuth systems).
- **Role-based Access Control (RBAC)**: Permissions are granted based on user roles, such as Admin, Data Manager, or Contact, with different levels of access. The private area is accessible only to authenticated contacts, while the backoffice is limited to administrators and data managers.

## GDPR Compliance
- **Data Minimization**: Only necessary data is collected from contacts and patients.
- **Explicit Consent**: All contacts must give explicit consent for data collection, as per GDPR requirements.
- **Right to Erasure**: Contacts and patients have the right to request their data be removed from the system.
- **Data Encryption**: All sensitive data (e.g., patient medical records, genetic information) is encrypted both in transit and at rest.

## File Handling
- **Secure Uploads**: Files uploaded (e.g., genetic reports) are handled within the private area, ensuring that only authenticated users can upload files. The files are stored in a secure environment, with access restricted to authorized personnel only.
- **Anonymization**: Personal identifiers are anonymized when used in reports or exports to protect patient and contact privacy.

## Data Retention
- **Staging Data**: Staging data is retained only until it is reviewed and transferred to the master database.
- **Master Data**: Master data is retained indefinitely unless deletion is requested by a user or required by law.
