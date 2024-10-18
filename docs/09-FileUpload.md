# File Upload Feature

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