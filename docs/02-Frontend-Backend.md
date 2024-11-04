
# Front-end / Back-end Interaction

## User Profile Creation / Sign-up

In this sequence, a new user signs up and creates their profile through **Auth0**, which then authenticates the user with an access token. The **Backend API** logs the user registration in the **DB** if needed.

```mermaid
sequenceDiagram
    participant Frontend
    participant Auth0
    participant BackendAPI
    participant DB

    Frontend->>Auth0: Sign-Up Request
    Auth0-->>Frontend: Access Token
    Frontend->>BackendAPI: Send Access Token for registration
    BackendAPI->>Auth0: Verify Access Token
    Auth0-->>BackendAPI: Token Verified
    BackendAPI->>DB: Log user registration (optional)
    BackendAPI-->>Frontend: Success Message
```

## User Sign-In

This sequence shows the user sign-in process. **Auth0** authenticates the user and provides an access token, which the **Frontend** uses to make authenticated requests to the **Backend API**. The **Backend API** verifies the token, retrieves necessary data from the **DB**, and returns it to the **Frontend**.

```mermaid
sequenceDiagram
    participant Frontend
    participant Auth0
    participant BackendAPI
    participant DB

    Frontend->>Auth0: Sign-In Request
    Auth0-->>Frontend: Access Token
    Frontend->>BackendAPI: Access Token for authenticated requests
    BackendAPI->>Auth0: Verify Access Token
    Auth0-->>BackendAPI: Token Verified
    BackendAPI->>DB: Retrieve data (e.g., user or patient info)
    BackendAPI-->>Frontend: Data Response
```

## Update User Profile

In this sequence, a user requests to update their profile information. The **Backend API** receives the request, verifies the token with **Auth0**, and updates the user profile in **Auth0**. Any necessary logs can also be saved to the **DB**.

```mermaid
sequenceDiagram
    participant Frontend
    participant BackendAPI
    participant Auth0
    participant DB

    Frontend->>BackendAPI: Update Profile Request with Access Token
    BackendAPI->>Auth0: Verify Access Token
    Auth0-->>BackendAPI: Token Verified
    BackendAPI->>Auth0: Update Profile Information
    Auth0-->>BackendAPI: Update Confirmation
    BackendAPI->>DB: Log profile update (optional)
    BackendAPI-->>Frontend: Success Response
```

## Create a New Patient

This sequence shows how a new patient entry is created. The **Frontend** sends a request to create a new patient, which the **Backend API** verifies with **Auth0**. Upon successful verification, the **Backend API** stores the patient data in the **DB** and confirms with the **Frontend**.

```mermaid
sequenceDiagram
    participant Frontend
    participant BackendAPI
    participant Auth0
    participant DB

    Frontend->>BackendAPI: Create Patient Request with Access Token
    BackendAPI->>Auth0: Verify Access Token
    Auth0-->>BackendAPI: Token Verified
    BackendAPI->>DB: Store new patient data
    BackendAPI-->>Frontend: Success Response with Patient ID
```

## Get User and Patient Information

In this sequence, the **Frontend** requests both profile and patient information. The **Backend API** verifies the user’s token with **Auth0**, retrieves profile information from **Auth0** and patient data from the **DB**, and sends both back to the **Frontend**.

```mermaid
sequenceDiagram
    participant Frontend
    participant BackendAPI
    participant Auth0
    participant DB

    Frontend->>BackendAPI: Request Profile & Patient Info with Access Token
    BackendAPI->>Auth0: Verify Access Token
    Auth0-->>BackendAPI: Token Verified
    BackendAPI->>Auth0: Get Profile Information
    Auth0-->>BackendAPI: Profile Data
    BackendAPI->>DB: Retrieve Patient Information
    DB-->>BackendAPI: Patient Data
    BackendAPI-->>Frontend: Profile and Patient Data Response
```
