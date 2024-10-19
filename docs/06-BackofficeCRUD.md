# 6. Backoffice CRUD Operations

The Backoffice application provides administrators with a user interface to manage contacts, patients, and relationships. This interface allows for full CRUD (Create, Read, Update, Delete) operations and list views of all entities.

## Features
- **Contact Management**: Add new contacts, update existing ones, and delete or archive old records.
- **Patient Management**: Add new patients, update patient details, and delete or archive records.
- **Relationship Management**: Manage multiple relationships between contacts and patients (e.g., one contact linked to multiple patients, and vice versa).

## List Views
- **Contacts List**: Displays all registered contacts with basic details (name, email, relationship to patient).
- **Patients List**: Displays all patients with their name, date of birth, and MECP2 mutation status.
- **Relationships List**: Shows the relationships between contacts and patients.

## CRUD Functions
- **Create**: Administrators can create new contacts, patients, and relationships.
- **Read**: Administrators can view detailed records for each contact, patient, and relationship.
- **Update**: Existing records can be edited, with all changes logged and timestamped.
- **Delete/Archive**: Records can be soft-deleted, with an option for recovery or complete removal after a certain period.
