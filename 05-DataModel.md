# 5. Master Data

The Master Data section covers the main data structure for contacts, patients, and relationships. This database represents the final version of validated records.

## Data Structure
- **Contacts**: Stores information related to legal guardians, caregivers, or individuals who are responsible for patients.
- **Patients**: Contains details about the patients with Rett Syndrome, including genetic information, demographics, and medical history.
- **Relationships**: Captures the relationships between contacts and patients, such as "mother", "father", or "legal guardian".

## Data model

```mermaid
erDiagram
    Contacts {
        UUID Contact_UUID
        string Full_Name
        string Email
        string Mobile_Number
        string Status
        string Consent_Status
        string Country_Code
        string State_Code
    }

    Patients {
        UUID Patient_UUID
        string Full_Name
        date Date_of_Birth
        string Gender
        string MECP2_Mutation_Clinical_Diagnosis
        string Country_Code
    }

    Relationships {
        UUID Relationship_UUID
        UUID Contact_UUID
        UUID Patient_UUID
        int Relationship_Type_ID
        string Relationship_Validity
    }

    Countries {
        string Country_Code
        string Country_Name
        string Region
    }

    States {
        string State_Code
        string State_Name
        string Country_Code
    }

    Relationship_Types {
        int Relationship_Type_ID
        string Relationship_Type_Name
    }

    Contacts ||--o{ Relationships : "has"
    Patients ||--o{ Relationships : "related to"
    Relationships ||--|| Relationship_Types : "uses"
    Contacts }o--|| Countries : "located in"
    Contacts }o--|| States : "state located in"
    Patients }o--|| Countries : "located in"
    States }o--|| Countries : "belongs to"
```

![Database model](./images/datamodel.png)