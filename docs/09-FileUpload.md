# File Upload Feature

The file upload feature allows contacts to securely upload files (such as genetic reports) associated with specific patients. To minimize storage and improve data processing, OpenAI is integrated to extract key information from the files, ensuring that only essential data is stored in the database.

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

5. **Data Linking**
   - The extracted data is linked to the appropriate patient in the master database.
   - Only the essential extracted information is stored, ensuring that database size is minimized.

6. **GDPR Compliance**
   - The file upload and data extraction processes adhere to GDPR standards.
   - Contacts must give explicit consent before uploading files.
   - Files are encrypted at rest and in transit, and all unnecessary data is securely deleted after processing.

## Key Advantages
- **Minimized Storage**: By extracting only key information and deleting the original files, the system avoids long-term file storage.
- **Improved Efficiency**: Using OpenAI to process files reduces manual data entry and ensures that only relevant data is saved.
- **GDPR Compliance**: The process is designed to comply with data protection laws, ensuring privacy and security for sensitive patient data.
