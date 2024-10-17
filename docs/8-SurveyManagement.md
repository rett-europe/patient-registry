# Survey Management

This section outlines the management of surveys used for data collection in the Rett Syndrome Patient Registry.

## Survey Creation
- Surveys are designed and created by administrators, covering topics like patient health status, MECP2 mutation updates, and other relevant information.
- Each survey is added to the Forms table, which tracks available surveys for future selection.

## Patient Targeting
- Administrators can select a subset of patients from the master database based on criteria such as age, geographic location, or previous survey participation.
- The tool allows for filtering and selecting patients based on these attributes.

## Token Generation and Distribution
- For each selected patient, a unique token is generated for the contact associated with that patient.
- This token creates a private, one-time link to the survey, ensuring secure and controlled participation.

## Survey Response Processing
- When a contact completes a survey, the response is processed and stored in the Survey Responses table.
- Each response is linked to the corresponding patient, allowing the data to be associated correctly for longitudinal tracking.
