# Data Model

With Auth0 handling user profile information, we will use a simplified `Contacts` entity in the data model by removing some fields and leveraging Auth0 for authentication and basic profile management.

## Adjusted Data Model

### 1. Auth0 Integration
 * User information like email, name, and mobile number will be stored in Auth0.
 * Auth0 will handle email verification, status, and other attributes related to authentication.

### 2. Contacts
 * Stores information related to legal guardians, caregivers, or individuals who are responsible for patients. This includes additional details not managed by Auth0, such as country, state, preferred language, and notes.

 * **DECISION NEEDED:** Should the contact profile info be entirely stored in Auth0, since it allows usual profile info and also custom information
 https://auth0.com/docs/manage-users/user-accounts/metadata

### 3. Patients
 * Contains personal, demographic, and clinical information about the patient. Each patient is linked to a contact, representing their legal guardian or caregiver.

### 4. Consent Management
 * Manages consent information for each patient, covering data sharing, research participation, and other specific permissions. Consent records are linked to both the contact (legal guardian) and the patient, ensuring that each consent is clearly traceable to the responsible party. This structure provides flexibility to manage multiple types of consent for each patient.

## Data Model Diagram

![Data model](./images/datamodel.png)

```mermaid
erDiagram
    Contacts {
        UUID Contact_UUID PK "Primary identifier for the contact"
        string Auth0_User_ID "Reference to the Auth0 user profile"
        string Country_Code FK "Foreign key to Countries"
        string State_Code FK "Foreign key to States"
        string Preferred_Language
        timestamp Created_At "Record creation timestamp"
        timestamp Last_Updated_At "Record update timestamp"
        text Notes
    }

    Patients {
        UUID Patient_UUID PK "Primary identifier for the patient"
        UUID Contact_UUID FK "Foreign key to Contacts"
        string National_ID "National Identification Number - **Optional**"
        string Full_Name
        date Date_of_Birth
        string Gender
        date Diagnosis_Date
        string MECP2_Mutation_Clinical_Diagnosis
        boolean Deceased
        date Death_Date "Optional"
        timestamp Created_At
        timestamp Last_Updated_At
    }

    Consent {
        UUID Consent_ID PK "Primary identifier for consent record"
        UUID Contact_UUID FK "Foreign key to Contacts"
        UUID Patient_UUID FK "Foreign key to Patients"
        string Consent_Type "Type of consent"
        string Consent_Status "Consent status"
        timestamp Consent_Date "Consent date"
    }

    Countries {
        string Country_Code PK "Primary key for Country"
        string Country_Name
        string Region
    }

    States {
        string State_Code PK "Primary key for State"
        string State_Name
        string Country_Code FK "Foreign key to Countries"
    }

    Relationship_Types {
        int Relationship_Type_ID PK "Primary key for Relationship Type"
        string Relationship_Type_Name
    }

    Contacts ||--o{ Patients : "manages"
    Contacts }o--|| Countries : "located in"
    Contacts }o--|| States : "state located in"
    Patients ||--o{ Consent : "has"
    Contacts ||--o{ Consent : "gives"
    States }o--|| Countries : "belongs to"
```
