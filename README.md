# Contact Management API

This project is aimed at learning FastAPI by creating a simple contact management system. The API allows you to perform CRUD operations on a list of contacts.

## Features

- **List all contacts**
- **Fetch a specific contact by ID**
- **Search contacts by name**
- **Create a new contact**
- **Update an existing contact**
- **Delete a contact by ID**

## Endpoints

### List All Contacts

- **URL**: `/contacts`
- **Method**: `GET`
- **Description**: Fetches all contacts.
- **Response**: A list of all contacts.

### Fetch a Contact by ID

- **URL**: `/contact/{contact_id}`
- **Method**: `GET`
- **Description**: Fetches a contact by its ID.
- **Response**: A contact matching the given ID.

### Search Contacts by Name

- **URL**: `/contact/search/`
- **Method**: `GET`
- **Description**: Searches for contacts by name.
- **Parameters**: `name` (query parameter) - The name to search for.
- **Response**: A list of contacts matching the given name.

### Create a New Contact

- **URL**: `/contact/create`
- **Method**: `POST`
- **Description**: Creates a new contact.
- **Body**: A JSON object containing the contact details.
- **Response**: A success message.

### Update an Existing Contact

- **URL**: `/contact/update/{contact_id}`
- **Method**: `PUT`
- **Description**: Updates an existing contact by its ID.
- **Body**: A JSON object containing the updated contact details.
- **Response**: A success message.

### Delete a Contact by ID

- **URL**: `/contact/delete/{contact_id}`
- **Method**: `DELETE`
- **Description**: Deletes a contact by its ID.
- **Response**: A success message.

## Sample Data

```python
CONTACTS = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "phone": "987-654-3210",
        "address": "456 Elm St, Othertown, USA"
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "phone": "555-555-5555",
        "address": "789 Oak St, Sometown, USA"
    },
    {
        "id": 4,
        "name": "Dana White",
        "email": "dana.white@example.com",
        "phone": "444-444-4444",
        "address": "321 Pine St, Thistown, USA"
    },
    {
        "id": 5,
        "name": "Eve Black",
        "email": "eve.black@example.com",
        "phone": "333-333-3333",
        "address": "654 Maple St, Thatown, USA"
    }
]
```

## How to Run

1. **Install FastAPI and Uvicorn**:
    ```sh
    pip install fastapi uvicorn
    ```

2. **Run the Application**:
    ```sh
    uvicorn main:app --reload
    ```

3. **Access the API**:
    - Open your browser and go to `http://127.0.0.1:8000`
    - You can also view the interactive API documentation at `http://127.0.0.1:8000/docs`

## Deployed Application

You can access the deployed API and view the Swagger UI documentation at [https://contact-py-app.onrender.com/docs](https://contact-py-app.onrender.com/docs).

## Conclusion

This project serves as a learning tool for FastAPI, providing a basic implementation of CRUD operations in a contact management system. Feel free to expand and modify the project to explore more features and functionalities of FastAPI.
