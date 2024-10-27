# Technical Implementation

We are still finalizing the technical implementation details, but in the interim, this sections explains the main building blocks.

## High-level architecture

![High-level-architecture diagram](./images/high-level-architecture.png)

## Content Management System (CMS) - WordPress

The WordPress CMS serves as the frontend for the registry, handling public-facing content and facilitating initial data intake via forms. This CMS setup is chosen for its simplicity, ease of maintenance, and extensive plugin ecosystem, making it ideal for hosting and managing content updates.

* Technology: WordPress (hosted on WordPress.com using Business subscription)
* Primary Role: Public website for informational content and registry landing page

### Forms tool for survey management - Gravity Forms

Gravity Forms is used within WordPress to handle user data intake, from initial onboarding to ongoing survey participation. It provides flexibility in form creation and allows easy integration with Azure services for data processing and storage.

* Primary Role: Collecting form submissions and survey data
* Integration: Data submitted via Gravity Forms is processed by Azure Functions and stored in the Azure SQL database.

## Secure Authentication - Auth0

The registry employs Auth0 for passwordless, secure authentication. Auth0 simplifies login management, allowing for secure access without traditional passwords, and supports two-factor authentication (2FA) for added security.

Primary Role: Authentication and identity management.
Integration: Enables secure access to both WordPress and the backend services.

## Orchestrator - Azure Functions

Azure Functions act as the core orchestrator, managing workflows across different services. This includes processing form data submissions, managing file uploads, and ensuring that data flows securely and consistently between components.

* Primary Role: Data processing, orchestration of backend tasks, and handling API requests.
* Functionality: Integrates with Auth0 for authentication, handles data storage in Azure SQL, and triggers events for file uploads.

## Storage 

### Relational database - Azure SQL

The primary database for the registry, Azure SQL stores patient, contact, and relationship data securely. It offers flexibility for structuring longitudinal data and supports scalability for future analytical needs.

* Primary Role: Storing structured data like patient demographics, contact relationships, and survey responses.
* Schema: Initial data model setup through SQL scripts (with Terraform setup for initial provisioning).

### File storage - Azure Blob Storage

Azure Blob Storage securely stores uploaded files (e.g., genetic reports) linked to patients. Blob Storage provides scalable and secure file management, essential for large files and GDPR-compliant storage practices.

* Primary Role: Secure storage for files associated with patient records.
* File Management: Files are linked via metadata in Azure SQL, enabling easy retrieval for processing.

## Admin frontend - PowerApps

PowerApps serves as the internal admin interface for managing and reviewing patient registry data. This platform allows authorized administrators to perform CRUD operations and view reports in a user-friendly, customizable interface.

* Primary Role: Admin portal for managing patient and contact records.
* Access Control: Integrated with Microsoft Authentication for secure access.

## Reporting & Analytics - PowerBI

Power BI is used for reporting and analytics, providing a comprehensive view of patient demographics, registry growth, and survey results. It integrates directly with Azure SQL for seamless data access and visualization.

* Primary Role: Data analytics and visual reporting for stakeholders.
* Data Security: Anonymized data extracts from Azure SQL maintain privacy.

## Notification Service (Email and SMS) - SendGrid/Twilio

To ensure effective communication with registry users, SendGrid is used for email notifications, and Twilio for SMS alerts (e.g., for two-factor authentication). These tools support both initial onboarding communications and ongoing engagement.

* Primary Role: Secure notification handling for verification and survey reminders.
* Integration: Notifications are triggered from Azure Functions to SendGrid/Twilio.

## Networking

All Azure services are configured within a secure Virtual Network (VNet) to enhance security, ensuring all internal services communicate over private IPs. Additionally, a firewall limits traffic to only authorized IPs.

* Primary Role: Enabling secure communication between Azure services.
* Configuration: IP restrictions, Azure Virtual Network Integration, and TLS.

## Other Azure services

### Application Insights for Monitoring

Azure Application Insights provides logging, diagnostics, and performance monitoring for Azure Functions and other backend services. It supports real-time insights, helping to optimize performance and troubleshoot issues.

* Primary Role: Performance monitoring and error diagnostics.
* Use Case: Logging and analyzing request metrics, latency, and errors.