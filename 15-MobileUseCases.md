# Mobile use cases

## High level requirements

* Multi platform support: it must render and provide full functionality in both desktop and mobile.

* Multi-language support: The app must support multiple languages to accommodate a diverse user base.

* Landing Page: A simple introduction screen with the app's logo, welcome message, and a button to initiate the login process.

* Login Page: Integrated with an identity provider (Auth0) to manage secure user authentication via OAuth.

* Home Page:
  * Displays a personalized welcome message.
  * Shows profile completeness percentage to encourage users to fill in missing information.
  * Options to Edit Profile and Manage Patients (add or edit patients).

* Profile Management:
  * Edit Profile: Allows users to update their personal details and increase profile completeness.

* Patient Management:
  * Add New Patient: Interface to input details of a new patient.
  * Edit Existing Patient: Allows users to update or correct information about previously added patients.
  * Basic Patient Insights: Summary view of key details for each patient (based on previous survey responses)

* Survey response functionality:
  * Users can respond to surveys related to individual patients (e.g., patient A, B, or C).
  * Easy Survey Management: The system must make it straightforward for administrators to add new surveys or update existing ones.

* Upload file functionality:
  * Users can upload a new file about the patient (this is mainly to upload a diagnosis confirmation, but ultimately may be used for other use cases)
  * Scan file using camera
  * Upload from image gallery

## Wireframes

![Mobile app wireframes](./images/mobile-app-wireframes.png)

## 1. Landing Page
- **Description**: This is the initial page that users see when they open the app.
- **Content**:
  - **Logo**: The logo of the patient registry.
  - **Welcome Message**: A brief welcome message introducing the purpose of the app.
  - **Login Button**: A button that initiates the login process for users.

## 2. Auth0 Authentication Flow
- **Description**: Users will authenticate using Auth0's OAuth flow.
- **Flow Details**:
  - **OAuth Flow**: When users click the login button, they will be redirected to Auth0 to complete the login process.
  - **Successful Login**: After successful login, users are redirected to the app's Home Page.

## 3. Home Page
- **Description**: This is the entry point to the user's private area after a successful login.
- **Content**:
  - **Welcome User**: Displays a welcome message with the user's name.
  - **Options**:
    - **Edit Profile**: Navigate to the profile editing page.
    - **Add Patient**: Option to add a new patient.
    - **Edit Patients**: If patients were previously added, an option to view and edit them.

## 4. Edit Profile Page
- **Description**: This page allows users to view and edit their profile information.
- **Content**:
  - **User Profile Info**: Fields such as name, email, phone number, etc.
  - **Edit Capability**: Users can update their information and save changes.

## 5. Add New Patient Page
- **Description**: This page allows users to add a new patient to the registry.
- **Flow**:
  - **First Patient**: If no patients have been added yet, the user will be prompted to create the first patient.
  - **Additional Patients**: Users can add multiple patients.
- **Fields**:
  - **Name**: First and last name of the patient.
  - **Birth Date**: Patient's date of birth.
  - **Additional Information**: Gender, relationship to user, and other basic details.

## 6. List Patients Page
- **Description**: Displays a list of patients that have been added by the user.
- **Content**:
  - **Patient List**: Displays the names and brief details of each patient.
  - **Edit Button**: Each patient entry includes an edit button.
  - **Add New Patient Button**: Provides an option to add another patient.

## 7. Edit Patient Info Page
- **Description**: This page allows the user to edit information about a specific patient.
- **Content**:
  - **Patient Details**: Fields such as name, birth date, age, and other information related to the patient.
  - **Save Changes**: Users can make modifications and save the updated details.

# User Flow Summary

1. **Landing Page**: User starts here and clicks the login button.
2. **Auth0 Authentication**: User is redirected to Auth0 for authentication.
3. **Home Page**: Upon successful login, the user can choose to edit their profile, add a patient, or edit existing patients.
4. **Edit Profile**: Allows users to update their personal information.
5. **Add New Patient**: Users add the first or additional patients.
6. **List Patients**: If patients exist, they are listed here with options to edit.
7. **Edit Patient Info**: Users can edit the details of an existing patient.
