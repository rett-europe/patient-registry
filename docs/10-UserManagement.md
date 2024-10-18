# User Management

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
