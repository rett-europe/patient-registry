# External Integrations

The Rett Syndrome Patient Registry integrates with external systems for data collection, reporting, and processing.

## JotForm Integration
- The onboarding form is built using JotForm (or other forms system), and submissions are sent directly to the Staging Database.
- An API integration fetches form submissions and stores them for review.

## PowerBI Reporting
- Data from the master database can be anonymized and exported to PowerBI for detailed reporting and analytics on patient demographics, mutations, and other metrics.

## RDCA-DAP Platform
- The registry integrates with the RDCA-DAP platform (C-Path) to share anonymized patient data for international research efforts.

## Email Integration (SendGrid or similar)
- Automated emails are sent to contacts as part of onboarding or data request processes, using an email service such as SendGrid.
