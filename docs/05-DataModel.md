# 5. Data model

The Master Data section covers the main data structure for contacts, patients, and relationships. This database represents the final version of validated records.

## Data Structure
- **Contacts**: Stores information related to legal guardians, caregivers, or individuals who are responsible for patients.
- **Patients**: Contains details about the patients with Rett Syndrome, including genetic information, demographics, and medical history.
- **Relationships**: Captures the relationships between contacts and patients, such as "mother", "father", or "legal guardian".

## Data model

```mermaid
erDiagram
    Contacts {
        UUID Contact_UUID PK "Primary identifier for the contact"
        string Full_Name
        string Email "Contact's email address"
        string Mobile_Number
        string Status
        string Consent_Status
        string Country_Code FK "Foreign key to Countries"
        string State_Code FK "Foreign key to States"
        string Preferred_Language
        timestamp Created_At "Record creation timestamp"
        timestamp Last_Updated_At "Record update timestamp"
        boolean Email_Verified "Whether email has been verified"
        text Notes
    }

    Patients {
        UUID Patient_UUID PK "Primary identifier for the patient"
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

    Relationships {
        UUID Relationship_UUID PK "Primary identifier for the relationship"
        UUID Contact_UUID FK "Foreign key to Contacts"
        UUID Patient_UUID FK "Foreign key to Patients"
        int Relationship_Type_ID FK "Foreign key to Relationship_Types"
        string Relationship_Validity
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

    Contacts ||--o{ Relationships : "has"
    Patients ||--o{ Relationships : "related to"
    Relationships ||--|| Relationship_Types : "uses"
    Contacts }o--|| Countries : "located in"
    Contacts }o--|| States : "state located in"
    States }o--|| Countries : "belongs to"
```

![Database model](./images/datamodel.png)