# Rett Syndrome Patient Registry - Functional Documentation

## 1. Overview

The Rett Syndrome Patient Registry is a system designed to collect, store, and manage data related to patients with Rett Syndrome. The system focuses on gathering essential contact, patient, and longitudinal data through various forms and surveys, ensuring secure and compliant data management.

The system provides administrators with tools to manage the data, while ensuring that contacts (legal guardians) can securely contribute relevant patient information. It is designed with GDPR compliance in mind, leveraging secure file handling and encryption protocols. The system integrates with the Microsoft ecosystem for user management and access control, providing a seamless experience for authorized personnel within the organization.

### Key Objectives:
- **Onboarding**: Provide a public form where legal guardians can onboard themselves and their associated patients without requiring authentication.
- **Data Management**: Enable the administration of contacts, patients, and relationships through a backoffice tool.
- **Longitudinal Data Collection**: Facilitate the continuous collection of patient data over time via secure surveys linked to specific patients.
- **File Upload**: Provide a secure mechanism for legal guardians to upload files, such as genetic reports, that are linked to patients.
- **User Management**: Leverage the Microsoft 365 ecosystem for authentication and authorization, ensuring that all user access is managed securely.
- **Security & Compliance**: Ensure the system complies with GDPR and maintains high standards for data encryption and protection.

---

## Key Functional Areas

### 1. Public Onboarding
The onboarding form is publicly accessible and allows contacts (legal guardians) to register themselves and the patients under their care. No authentication is required to complete the form, and all submissions are stored in a staging database for review before final entry into the master database.

- **Fields Collected**: 
  - Contact: Full Name, Email, Mobile, Country, State, Relationship to Patient
  - Patient: Full Name, Date of Birth, Gender, MECP2 Mutation (or clinical diagnosis)

- **Data Flow**: Submissions are first stored in the staging database and validated before being moved to the master database.

![Onboarding process](docs/./images/onboarding-process.png)

### 2. Staging Database and Data Processing
The staging database temporarily stores data from the onboarding form. Data must be validated (e.g., deduplication checks) before being moved to the master database, which contains the primary records for contacts, patients, and their relationships.

- **Processing Workflow**: Data validation, deduplication, and transfer to the master database.

### 3. Master Data
The master database contains all validated records of contacts, patients, and their relationships. Relationships define the connections between contacts (e.g., legal guardians) and patients (e.g., mother, father, legal guardian).

- **Entities**: 
  - Contacts: Legal guardians or caregivers.
  - Patients: Individuals diagnosed with Rett Syndrome.
  - Relationships: Connections between contacts and patients.

### 4. Backoffice Application (CRUD)
The backoffice application allows administrators to perform full CRUD operations on contacts, patients, and their relationships. It includes list views, search functionality, and allows for adding, updating, and deleting records.

- **Functionalities**:
  - CRUD operations for contacts, patients, and relationships.
  - List and search features for managing data.

### 5. Longitudinal Data Collection
The registry supports the collection of longitudinal data by allowing administrators to send surveys to contacts at different intervals. Each survey is linked to the corresponding patient through a secure, tokenized system, ensuring data integrity.

- **Process**:
  - Select a subset of patients.
  - Generate private links using individual tokens.
  - Send email notifications to contacts with unique links.
  - Process survey responses and associate them with the correct patient.

![Logitudinal Data](docs/./images/survey-data-gathering.png)

### 6. Secure File Upload
The system includes a secure file upload feature where legal guardians can upload files (e.g., genetic reports) using a private, token-based link. These files are securely stored and linked to the appropriate patient, ensuring GDPR compliance.

- **File Linking**: Each uploaded file is associated with a patient and stored securely in an encrypted environment.

### 7. User Management (Microsoft 365 Integration)
All user management is handled through the Microsoft 365 ecosystem, ensuring that only authorized personnel within the organization can access the system. The system uses Single Sign-On (SSO) and Role-Based Access Control (RBAC) for managing user permissions.

- **Roles**: Admin, Data Manager, Viewer.
- **Authentication**: Handled via Microsoft Azure AD and SSO.

### 8. Security and GDPR Compliance
The system is fully compliant with GDPR regulations, ensuring that all personal and sensitive data is protected. Explicit consent is required from contacts when submitting data or uploading files. The system uses encryption for data both at rest and in transit.

- **Security Features**:
  - Data encryption (at rest and in transit).
  - Role-based access control.
  - GDPR-compliant consent management.

### 9. Reporting and Analytics
The system integrates with reporting tools like PowerBI to allow administrators to generate detailed reports on patient demographics, mutation data, and longitudinal trends. All reports are anonymized to ensure privacy.

- **Capabilities**:
  - Anonymized reporting.
  - Exporting data for external analysis.

---

# 2. Public Onboarding Form

The public onboarding form is the first step for contacts (legal guardians) to register patients in the system.

## Form Details
- Accessible publicly without requiring authentication.
- Open to any legal guardian who needs to add a new patient.
- The form will collect basic information about both contacts and patients.

## Required Fields
### Contact Information
- Full Name
- Email
- Mobile Number (Optional)
- Country
- State (Optional, depends on the country)
- Relationship to Patient

### Patient Information
- Full Name
- Date of Birth
- Gender
- Confirm if there is a MECP2 mutation or it's a clinical diagnosis (or a different gene)

### Consent Information
- Explicit consent of privacy policy

## Data Submission
- All responses are persisted in the Staging Database for review before being moved into the master dataset.


# 3. Staging Database

The Staging Database serves as a temporary storage layer for all data submitted through the Public Onboarding Form. This layer allows administrators to review and validate the data before transferring it to the master dataset.

## Purpose
- To ensure data quality by allowing for manual or automated validation steps.
- To temporarily store information on contacts and patients before their final inclusion in the master dataset.
- To allow for deduplication and verification of data entries.

## Data Flow
1. Form submissions from the Public Onboarding Form are automatically persisted in the Staging Database.
2. Data remains in the Staging Database until it is processed into the RettDB data model.
3. Once data is validated and confirmed, it is transferred into the master database, where it becomes part of the main dataset.

## Data Validation
- Validation steps can include checking for duplicate records (e.g., patients with the same name and birthdate) and verifying the integrity of the provided MECP2 mutation data.
- Administrators can review submissions through the backoffice interface before finalizing the transfer.

## Data Retention
- Data in the Staging Database is retained until reviewed and processed. After processing, staging data can be either archived or deleted, based on retention policies.


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


# 5. Master Data

The Master Data section covers the main data structure for contacts, patients, and relationships. This database represents the final version of validated records.

## Data Structure
- **Contacts**: Stores information related to legal guardians, caregivers, or individuals who are responsible for patients.
- **Patients**: Contains details about the patients with Rett Syndrome, including genetic information, demographics, and medical history.
- **Relationships**: Captures the relationships between contacts and patients, such as "mother", "father", or "legal guardian".

## Data Fields
### Contacts
- Contact UUID
- Full Name
- Email
- Mobile Number (Optional)
- Country
- State (Depends on the country)

### Patients
- Patient UUID
- Full Name
- Date of Birth
- Gender
- MECP2 Mutation or Clinical Diagnosis

### Relationships
- Relationship UUID
- Contact UUID
- Patient UUID
- Relationship Type (e.g., "Mother", "Father", "Legal Guardian")


# 6. Backoffice CRUD Operations

The Backoffice application provides administrators with a user interface to manage contacts, patients, and relationships. This interface allows for full CRUD (Create, Read, Update, Delete) operations and list views of all entities.

## Features
- **Contact Management**: Add new contacts, update existing ones, and delete or archive old records.
- **Patient Management**: Add new patients, update patient details, and delete or archive records.
- **Relationship Management**: Manage multiple relationships between contacts and patients (e.g., one contact linked to multiple patients, and vice versa).

## List Views
- **Contacts List**: Displays all registered contacts with basic details (name, email, relationship to patient).
- **Patients List**: Displays all patients with their name, date of birth, and MECP2 mutation status.
- **Relationships List**: Shows the relationships between contacts and patients.

## CRUD Functions
- **Create**: Administrators can create new contacts, patients, and relationships.
- **Read**: Administrators can view detailed records for each contact, patient, and relationship.
- **Update**: Existing records can be edited, with all changes logged and timestamped.
- **Delete/Archive**: Records can be soft-deleted, with an option for recovery or complete removal after a certain period.


# 7. Longitudinal Data Collection

The longitudinal data collection process allows for gathering ongoing data for each patient at different points in time, through surveys. This process is crucial for tracking changes and updates in the patients' condition, genetic information, and treatments over time.

## Workflow

1. **Select a Subset of Patients**  
   - An administrator selects a target group of patients from the master database. This selection is based on certain criteria such as patient demographics, mutation status, or previous survey responses.

2. **Generate Private Links for Surveys**  
   - A process generates individual tokens for each contact-patient pair.
   - Each token is linked to a specific survey and patient, ensuring that the survey is unique and can only be submitted once by the contact.
   - These tokens are stored in the Tokens table and are associated with both contacts and patients.

3. **Send Email Notifications**  
   - Automated emails are sent to the selected contacts.
   - Each email contains a unique survey link generated by the token system, which directs the contact to the survey page.

4. **Receive and Process Survey Responses**  
   - Once the survey is completed, the response is stored with the corresponding token.
   - The survey responses are linked to the correct patient in the master database, ensuring that longitudinal data is properly maintained for each patient.
   - This allows multiple surveys to be associated with the same patient, forming a longitudinal data set.

## Data Association

- **Patient Surveys**: Each patient can have multiple surveys associated with them over time, providing longitudinal data. 
- **Token System**: Ensures that each response is uniquely tied to a patient-contact pair, avoiding duplicate submissions or data inconsistencies.


# 8. Survey Management

The Survey Management system facilitates the distribution of surveys to contacts associated with patients in the Rett Syndrome Patient Registry. To meet regulatory requirements, it includes a mechanism that guarantees surveys are answered by the designated contact, ensuring the integrity of the data collected.

## Survey Creation
- Surveys are created by administrators to collect data over time, such as health updates or new genetic information.
- Surveys can cover a wide range of topics and are designed to collect longitudinal data that can be linked to specific patients.

## Patient Targeting
- Administrators can select a subset of patients from the master database to receive specific surveys.
- The system allows filtering based on criteria such as age, mutation type, or previous survey responses.

## Token-Based Survey Distribution
- For each selected patient, the system generates a unique token tied to the contact associated with the patient.
- This token is used to create a private, one-time link for the survey, ensuring that only the designated contact can submit a response.

## Contact Authentication and Verification
To comply with regulatory requirements, the system includes a mechanism to verify that the survey is completed by the designated contact:
  
1. **Token Verification**: 
   - The survey link is unique to each contact-patient pair and can only be used once. Each link contains an embedded token that is verified before the survey is opened.
  
2. **Two-Factor Authentication (2FA)**:
   - Before completing the survey, the contact is required to verify their identity using a second factor of authentication (2FA), such as an SMS code or authentication app.
   - This ensures that only the authorized contact can access and complete the survey.

3. **Audit Trail**:
   - The system records a detailed audit trail for each survey submission, including the identity of the contact who submitted the survey, the timestamp, and any authentication steps completed.
   - This guarantees compliance with regulatory requirements and provides accountability for the data submitted.

4. **Consent Confirmation**:
   - Each contact must confirm their consent before submitting the survey, ensuring compliance with privacy regulations such as GDPR.
  
## Survey Response Processing
- Once the survey is submitted, the response is securely stored in the database.
- Each response is linked to the corresponding patient, enabling longitudinal tracking of the patient’s condition or genetic information.
- Data is stored securely and is accessible only to authorized administrators.

## Data Security and Privacy
- All survey responses are encrypted both in transit and at rest.
- The system adheres to GDPR and other regulatory requirements for data protection, ensuring that sensitive patient and contact information is handled with care.
- Contact authentication ensures that responses are submitted only by verified individuals, protecting the integrity of the collected data.


# 9. File Upload Feature

The file upload feature allows contacts to securely upload files (such as genetic reports) associated with specific patients. To minimize storage and improve data processing, OpenAI is integrated to extract key information from the files. Additionally, a doctor can be requested to validate the diagnosis by analyzing the report, ensuring that both automated and expert validation processes are applied.

---

## Workflow

1. **Token-Based Links**
   - Each contact receives an individual token (unique link) via email, which is associated with a specific patient.
   - The token is used to access the file upload page, ensuring that the file is securely linked to the correct patient.

2. **Secure Upload**
   - Contacts can upload files (e.g., genetic reports) through a secure form.
   - File types can include PDFs, images, or any other supported format.
   - The file upload form does not require login, only the token for authentication.

3. **OpenAI Integration for Key Data Extraction**
   - Once the file is uploaded, OpenAI is used to extract key information such as:
     - MECP2 mutation data.
     - Patient demographics.
     - Relevant medical details.
   - This extracted data is structured and normalized before being stored in the database.
   - The goal is to minimize the amount of raw data stored by only saving the extracted, relevant information.

4. **Temporary File Storage**
   - Uploaded files are stored temporarily while OpenAI processes them.
   - Once the key data is extracted, the files are securely deleted from the system to avoid long-term storage.
   - A retention policy ensures that files are only kept for the minimum time required for processing.

5. **Doctor Review and Validation**
   - After OpenAI extracts the key data, the system can notify a designated doctor to review and validate the diagnosis.
   - The doctor receives a secure, token-based link to access the patient’s report and the extracted data.
   - The doctor reviews the report, analyzes the provided diagnostic information, and can validate or add comments to the diagnosis.
   - The doctor’s validation is securely logged and linked to the patient’s record in the database.

6. **Data Linking**
   - The extracted data, along with any validation from the doctor, is linked to the appropriate patient in the master database.
   - Only the essential extracted information and doctor’s validation are stored, ensuring that database size is minimized.

7. **GDPR Compliance**
   - The file upload, data extraction, and validation processes adhere to GDPR standards.
   - Contacts must give explicit consent before uploading files.
   - Files and extracted data are encrypted both at rest and in transit, and unnecessary data is securely deleted after processing.

---

## Key Advantages
- **Automated Data Extraction**: Using OpenAI to process files ensures that key information is extracted efficiently and stored in a structured format.
- **Expert Validation**: By involving a doctor in the validation process, the system ensures that diagnoses are accurate and reviewed by a medical expert.
- **Minimized Storage**: By extracting only key information and deleting the original files, the system avoids long-term file storage.
- **Improved Efficiency**: OpenAI reduces manual data entry, while doctors ensure the accuracy and validation of the extracted data.
- **GDPR Compliance**: The process is fully compliant with data protection laws, ensuring privacy and security for sensitive patient data.

# 10. User Management

This section outlines the user management process, which is integrated with the Microsoft ecosystem to ensure secure and centralized control of access to the system.

---

## Microsoft 365 Integration

- **Authentication**: The system uses Microsoft 365 accounts to authenticate administrators, doctors, and users with access to sensitive data.
- **Azure AD**: All user accounts are managed via Azure Active Directory (Azure AD), allowing for centralized management of roles and permissions.
- **Single Sign-On (SSO)**: Users can log in using their Microsoft credentials, streamlining access through Single Sign-On (SSO) functionality.

---

## Role-Based Access Control (RBAC)

- **Roles**: Users are assigned specific roles, including Admin, Data Manager, Viewer, and Doctor, based on their responsibilities.
  
### Permissions by Role:

- **Admin**: 
  - Full access to CRUD operations on contacts, patients, relationships, and longitudinal data.
  - Manage users and roles, including provisioning new users.
  
- **Data Manager**: 
  - Can access and manage patient and contact information but cannot modify user roles or access sensitive data like genetic reports.

- **Viewer**: 
  - Can view reports and data but cannot modify or delete any records.

- **Doctor**:
  - Can securely access and review patient reports uploaded by contacts.
  - Responsible for validating diagnoses based on genetic reports.
  - Can add comments or approve/reject diagnosis, which is logged in the system.
  - No access to administrative or management functions (CRUD operations).

---

### User Provisioning

- **Admins** can provision new users within Azure AD by assigning them roles and permissions as required.
- Users can be easily managed within Azure AD, including setting up doctors and other key personnel for review and validation of patient data.

---

## Security

- **Microsoft Compliance**: Using Microsoft 365 and Azure AD ensures that the system leverages Microsoft’s built-in security measures, including two-factor authentication (2FA), conditional access policies, and compliance with industry standards.
  
- **Activity Logging**: All user actions within the backoffice and validation processes are logged for audit purposes, ensuring traceability and accountability. This includes:
  - Doctor actions related to reviewing and validating diagnoses.
  - Access to sensitive patient reports and genetic data.
  - OpenAI processing logs for actions performed by automated systems under specific roles.

---

### Doctor Role Integration:

By adding the **Doctor** role, the system allows healthcare professionals to securely access, review, and validate patient diagnoses based on uploaded genetic reports. The doctor’s actions are limited to reviewing and validating reports, while any modification or validation is tracked and logged for compliance purposes.

- **Doctor Access**: 
  - Doctors can only view and validate reports assigned to them through the secure link.
  - Their access is logged, including timestamp and report review details, ensuring full traceability.
  - They cannot perform any other system operations (CRUD on patients, contacts, etc.).
  
- **Doctor Validation Process**: 
  - Once the doctor reviews the uploaded report, they can validate the diagnosis, which is logged and stored in the system.
  - The validation is then available to administrators or data managers for further action, such as updating patient information or preparing reports.


# 11. Reporting and Analytics

This section covers the reporting and analytics capabilities provided by the system, with a focus on patient demographics, mutations, and relationships.

## PowerBI Dashboard
- Provides real-time reporting on data such as:
  - Number of registered patients.
  - Age groups and demographic distribution.
  - MECP2 mutation statuses and other genetic data.

## Custom Reports
- Administrators can generate custom reports based on specific filters (e.g., all patients with a clinical diagnosis, patients under 5 years old).
- Reports can be exported to CSV for sharing with external stakeholders or further analysis.

## Anonymized Data Exports
- All reports are anonymized to protect the privacy of patients and contacts.
- Sensitive fields such as names, emails, and birthdates are hashed or removed.


# 12. Security and Compliance

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


# 13. Auditing and Compliance

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

# 14. Consent Management

The European Rett Syndrome Patient Registry places a high priority on ensuring that all data collection activities comply with GDPR regulations, particularly with respect to obtaining explicit consent from participants or their legal guardians. This section outlines the processes for managing and tracking consent throughout the registry.

---

## Consent Collection

Consent is required before any personal or sensitive data can be collected from participants or their legal guardians. This includes demographic information, genetic data, medical history, and caregiver information.

### Key Principles:
- **Explicit Consent**: Consent must be clearly and explicitly given by the participant or legal guardian. No data is collected without this.
- **Informed Consent**: Participants are provided with full details of how their data will be used, who will have access to it, and their rights under GDPR.
- **Right to Withdraw**: Participants have the right to withdraw consent at any time. Upon withdrawal, their data will be anonymized or deleted as required by GDPR.

### How Consent is Obtained:
- **Online Forms**: Consent is collected through the public onboarding forms, where participants or legal guardians are required to check a box confirming their agreement with the data usage terms.
- **File Uploads**: Before uploading any documents (e.g., genetic reports), participants are required to give consent for the processing and storage of these files.
- **Surveys**: Each survey sent to participants is accompanied by a clear consent prompt, ensuring that participants understand how their responses will be used.

---

## Consent Tracking and Documentation

To ensure compliance, the system tracks and stores detailed information about each consent provided by participants. This information is maintained in the system as long as it is legally required.

### Consent Tracking Includes:
- **Date and Time of Consent**: The exact timestamp when consent was given.
- **Form or Action**: The specific form or action (e.g., survey submission, onboarding, file upload) that required consent.
- **Participant Details**: The identity of the participant or legal guardian who provided the consent.
- **IP Address**: When necessary, the IP address from which consent was given may be logged for additional verification.
- **Audit Logs**: All consent actions are recorded in an audit log for compliance and accountability purposes.

---

## Consent for Minors and Legal Guardianship

In cases where the participant is a minor or unable to provide consent on their own, legal guardians are responsible for providing consent. The system accommodates this by allowing legal guardians to act on behalf of the patient.

### Key Provisions:
- **Guardian Consent**: Legal guardians must explicitly confirm their status and provide consent on behalf of the minor or dependent.
- **Verification**: Additional verification steps may be taken to ensure that the person providing consent is the authorized legal guardian.

---

## Right to Withdraw Consent

Participants or legal guardians have the right to withdraw consent at any time, in accordance with GDPR. The system is designed to facilitate this process smoothly.

### Withdrawal Process:
- **Request for Withdrawal**: Participants can submit a withdrawal request via the registry’s contact options or through the system's user interface.
- **Anonymization**: Upon withdrawal, all personally identifiable information will be anonymized, ensuring that the participant’s data cannot be traced back to them.
- **Data Deletion**: In cases where anonymization is not feasible, the data will be securely deleted from the system, and a record of the withdrawal will be stored in the audit logs.
- **Confirmation**: Once the withdrawal is processed, the participant or legal guardian will receive confirmation that their data has been removed or anonymized.

---

## Compliance with GDPR

The consent management process fully complies with GDPR, ensuring that participants are informed, their consent is obtained and tracked properly, and their right to withdraw is respected.

### GDPR Key Requirements:
- **Transparency**: Participants are fully informed of how their data will be used.
- **Data Minimization**: Only the necessary data is collected, and participants are made aware of the scope.
- **Right to Access**: Participants have the right to request access to the data collected on them, including their consent records.
- **Right to Erasure**: Participants can request the erasure of their data if they withdraw consent or if the data is no longer necessary for the registry’s purposes.

---

## Auditing and Accountability

All consent actions, including the provision and withdrawal of consent, are logged in the audit trail. This provides a clear record for regulatory bodies and helps ensure the registry’s compliance with legal and ethical standards.

- **Audit Logs**: Every consent-related action is recorded, ensuring that compliance with GDPR is verifiable.
- **Regular Audits**: Internal and external audits can be conducted to verify that consent is being managed in line with regulatory requirements.

---

## Ongoing Consent Review

As the project evolves and new features are added, participants or their legal guardians may be asked to re-confirm their consent if new types of data are collected or if the data use changes.


