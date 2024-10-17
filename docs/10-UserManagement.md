# User Management

This section outlines the user management process, which is integrated with the Microsoft ecosystem to ensure secure and centralized control of access to the system.

## Microsoft 365 Integration

- **Authentication**: The system uses Microsoft 365 accounts to authenticate administrators and users with access to sensitive data.
- **Azure AD**: All user accounts are managed via Azure Active Directory (Azure AD), allowing for centralized management of roles and permissions.
- **Single Sign-On (SSO)**: Users can log in using their Microsoft credentials, streamlining access through Single Sign-On (SSO) functionality.

## Role-Based Access Control (RBAC)

- **Roles**: Users are assigned specific roles such as Admin, Data Manager, or Viewer.
- **Permissions**:
  - **Admin**: Full access to CRUD operations on contacts, patients, relationships, and longitudinal data.
  - **Data Manager**: Can access and manage patient and contact information but cannot modify user roles.
  - **Viewer**: Can view reports and data but cannot modify or delete any records.
  
- **User Provisioning**: Admins can provision new users within Azure AD by assigning them roles and permissions as required.

## Security

- **Microsoft Compliance**: Using Microsoft 365 and Azure AD ensures that the system leverages Microsoft’s built-in security measures, including two-factor authentication (2FA), conditional access policies, and compliance with industry standards.
- **Activity Logging**: All user actions within the backoffice are logged for audit purposes, ensuring traceability and accountability.
  
## Future Integrations

- **Group-Based Permissions**: Possibility to set up group-based permissions within Azure AD to streamline user role assignments (e.g., a group for "Admins" and another for "Data Managers").
- **Azure AD Conditional Access**: Further refinement of access policies based on conditions such as device health, location, and risk level.
