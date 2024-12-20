# 8. Survey Management

The Survey Management system facilitates the distribution of surveys to contacts associated with patients in the Rett Syndrome Patient Registry. To meet regulatory requirements, it includes a mechanism that guarantees surveys are answered by the designated contact, ensuring the integrity of the data collected.

## Survey Creation
- Surveys are created by administrators to collect data over time, such as health updates or new genetic information.
- Surveys can cover a wide range of topics and are designed to collect longitudinal data that can be linked to specific patients.

## Patient Targeting
- Administrators can select a subset of patients from the master database to receive specific surveys.
- The system allows filtering based on criteria such as age, mutation type, or previous survey responses.

## Private Area for Survey Access
- Surveys are accessed through a private area where users must authenticate.
- Each contact associated with a patient will log in to their private area to view and complete any assigned surveys.

## Contact Authentication and Verification
To comply with regulatory requirements, the system includes a mechanism to verify that the survey is completed by the designated contact:
  
1. **Authentication**: 
   - Contacts are required to authenticate themselves before accessing their private area where surveys are available. Authentication may include email verification and a passwordless login or a similar secure method.
  
2. **Two-Factor Authentication (2FA)**:
   - Before completing the survey, the contact may be required to verify their identity using a second factor of authentication (2FA), such as an SMS code or authentication app.
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