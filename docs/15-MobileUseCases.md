# Mobile use cases

## 1. User Registration (Passwordless Login)
* Actors: Legal Guardians, Parents
* Description: Users introduce their email address and receive a magic link or verification code. After verification, they log in without a password.
* Flow:
    * User enters email.
    * System sends a verification code or link.
    * User verifies and logs in.
    * App confirms successful registration and login.

## 2. Profile Viewing and Completeness Check
* Actors: Legal Guardians, Parents
* Description: Users can view their profile information, including demographic details about themselves and their child. They can also see a "completeness score" for how many surveys they've completed.
* Flow:
    * User logs in.
    * App displays personal details and patient information.
    * App shows progress/completeness score for submitted surveys.

## 3. Survey Completion
* Actors: Legal Guardians, Parents
* Description: Users receive notifications to complete new surveys (e.g., RSBQ). Surveys are short and frequent to encourage participation.
* Flow:
    * User is notified about a new survey.
    * User opens the survey.
    * Completes the survey and submits responses.
    * App updates the completeness score and sends data to the server.

## 4. Document Submission (e.g., Genetic Reports)
* Actors: Legal Guardians, Parents
* Description: Users can upload documents such as genetic reports securely, which will be linked to the patient's profile.
* Flow:
    * User logs in and selects the patient profile.
    * User uploads a document (e.g., a genetic report).
    * App confirms successful upload and links the document to the patient's profile.

## 5. Survey and File Submission Status Tracking
* Actors: Legal Guardians, Parents
* Description: Users can track the status of the surveys they’ve submitted and any documents uploaded for their patient profile.
* Flow:
    * User logs in and selects a patient profile.
    * App displays a list of submitted surveys and uploaded documents.
    * Status indicators show if surveys are pending, submitted, or under review.

## 6. Push Notifications for Survey Reminders
* Actors: Legal Guardians, Parents
* Description: The app sends reminders when new surveys are available or when users haven't completed required steps (e.g., document uploads).
* Flow:
    * User receives a notification about an available survey.
    * User opens the app and completes the survey or takes necessary action.

## 7. View Patient Progress and Updates
* Actors: Legal Guardians, Parents
* Description: Users can view updates or new findings based on their submitted data and the progress of the patient registry as a whole.
* Flow:
    * User logs in.
    * User navigates to a section where they can see aggregated data insights or personal progress.
    * App displays updates relevant to the patient.

## 8. Edit Basic Profile Information
* Actors: Legal Guardians, Parents
* Description: Users can update basic information like their email address or contact details.
* Flow:
    * User logs in and navigates to profile settings.
    * User edits and updates basic personal details.
    * System validates changes and confirms updates.

## 9. Multi-language Support
* Actors: Legal Guardians, Parents
* Description: The app offers language support (e.g., Spanish, Portuguese, English) to accommodate users across different countries.
* Flow:
    * User selects preferred language at registration or in settings.
    * App content is displayed in the selected language.

## 10. Privacy and Consent Management
* Actors: Legal Guardians, Parents
* Description: Users review and agree to consent documents related to data privacy and participation in the registry.
* Flow:
    * User is prompted to review consent terms during registration.
    * User agrees or reviews terms at any time from their profile settings.
    * App logs consent responses.