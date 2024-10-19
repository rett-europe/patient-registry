# 3. Staging Database

The Staging Database serves as a temporary storage layer for all data submitted through the Public Onboarding Form. This layer allows administrators to review and validate the data before transferring it to the master dataset.

## Purpose
- To ensure data quality by allowing for manual or automated validation steps.
- To temporarily store information on contacts and patients before their final inclusion in the master dataset.
- To allow for deduplication and verification of data entries.

## Data Flow
1. Form submissions from the Public Onboarding Form are automatically persisted in the Staging Database.
2. Data remains in the Staging Database until it is processed into the RettDB data model.
3. Once data is validated and confirmed, it is transferred into the master database, where it becomes part of the main dataset.

## Data Validation
- Validation steps can include checking for duplicate records (e.g., patients with the same name and birthdate) and verifying the integrity of the provided MECP2 mutation data.
- Administrators can review submissions through the backoffice interface before finalizing the transfer.

## Data Retention
- Data in the Staging Database is retained until reviewed and processed. After processing, staging data can be either archived or deleted, based on retention policies.
