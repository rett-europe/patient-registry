# 2a. Onboarding Process to Guarantee Valid Emails

## Process to Validate Email

The email validation process ensures that the legal guardian's email address is verified before accessing further steps in the system. Upon submitting the initial form with the required details (e.g., email and name), the system sends a magic link to the provided email address.

1. The legal guardian submits the form with their email.
2. The system stores the information in the database and sends a magic link via email.
3. The legal guardian clicks the magic link, which redirects them to the verification page.
4. The system verifies the token associated with the magic link and updates the database.
5. If valid, the legal guardian is granted access.

```mermaid
sequenceDiagram
    participant LegalGuardian
    participant LandingPage
    participant EmailService
    participant Database

    LegalGuardian->>LandingPage: Submit form (email, name, etc.)
    LandingPage->>Database: Store user info (email, name, etc.)
    LandingPage->>EmailService: Send magic link email
    EmailService->>LegalGuardian: Magic link email sent

    LegalGuardian->>EmailService: Click on magic link
    EmailService->>LandingPage: Redirect with token
    LandingPage->>Database: Validate token
    Database->>LandingPage: Token valid
    LandingPage->>LegalGuardian: Access granted (verified)
```

![Email verification process](./images/email-verification.png)

## Process to update email

This process allows a legal guardian to update their email address by submitting both their current and new emails. Verification of both the current and new emails ensures the legitimacy of the request.

1. The legal guardian submits their current and new email addresses.
2. The system sends a verification link to the current email address.
3. The legal guardian clicks the link in the current email to confirm the request.
4. The system then sends a verification link to the new email address.
5. The legal guardian verifies the new email by clicking the link.

Upon successful verification, the system updates the email in the database and notifies both the old and new email addresses of the change.

```mermaid
sequenceDiagram
    participant LegalGuardian
    participant LandingPage
    participant EmailService
    participant Database

    LegalGuardian->>LandingPage: Submit current and new email
    LandingPage->>EmailService: Send verification to current email
    EmailService->>LegalGuardian: Email verification link to current email

    LegalGuardian->>EmailService: Click on current email magic link
    EmailService->>LandingPage: Verify current email link
    LandingPage->>EmailService: Send verification to new email
    EmailService->>LegalGuardian: Email verification link to new email

    LegalGuardian->>EmailService: Click on new email magic link
    EmailService->>LandingPage: Verify new email link
    LandingPage->>Database: Update email in database
    Database->>LandingPage: Confirm email updated
    LandingPage->>EmailService: Send notification to new email and current email

    LandingPage->>LegalGuardian: Email successfully updated
```

![Email update process](./images/email-update.png)