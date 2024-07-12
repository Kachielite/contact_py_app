from fastapi import FastAPI

app = FastAPI()

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


# FECTCH ALL BOOKS

@app.get('/contacts')
async def list_all_contacts():
    return CONTACTS


