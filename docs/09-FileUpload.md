# File Upload Feature

The file upload feature allows contacts to securely upload files (such as genetic reports) associated with specific patients. This process is token-based to ensure security and data integrity.

## Workflow

1. **Token-Based Links**
   - Each contact receives an individual token (unique link) via email, which is associated with a specific patient.
   - The token is used to access the file upload page, ensuring that the file is securely linked to the correct patient.

2. **Secure Upload**
   - Contacts can upload files (e.g., genetic reports) through a secure form.
   - File types can include PDFs, images, or any other supported format.
   - The file upload form does not require login, only the token for authentication.

3. **File Linking**
   - Once the file is uploaded, it is automatically linked to the patient in the master database.
   - The file is stored in the system with a reference to both the patient and the contact who uploaded the file.

4. **GDPR Compliance**
   - The file upload process is fully GDPR-compliant.
   - Contacts must give explicit consent before uploading any files.
   - Files are encrypted at rest and in transit to ensure maximum data protection.

5. **Storage and Encryption**
   - All files are stored securely in the database with access restricted to authorized users only.
   - Files are encrypted, both at rest and in transit.
   - Administrators can review the uploaded files from the backoffice interface.
