# Public Onboarding Form

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
