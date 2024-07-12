from fastapi import Body, FastAPI

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


# FETCH A CONTACT
@app.get('/contact/{contact_id}')
async def get_contact_by_id(contact_id: int):
    for contact in CONTACTS:
        if contact.get('id') == contact_id:
            return contact


# SEARCH CONTACT BY NAME
@app.get('/contact/search/')
async def search_contact_by_name(name: str):
    contacts_to_return = []
    for i in range(len(CONTACTS)):
        if name.casefold() in CONTACTS[i].get("name").casefold():
            contacts_to_return.append(CONTACTS[i])
    return contacts_to_return


# CREATE NEW CONTACT
@app.post('/contact/create')
async def create_new_contact(new_contact=Body()):
    CONTACTS.append(new_contact)
    return {"message": "Contact saved successfully"}


# UPDATE CONTACT
@app.put('/contact/update/{contact_id}')
async def update_contact(contact_id: int, contact_to_update=Body()):
    for i in range(len(CONTACTS)):
        if CONTACTS[i].get('id') == contact_id:
            CONTACTS[i] = contact_to_update
    return {"message": "Contact updated successfully"}


# DELETE CONTACT
@app.delete('/contact/delete/{contact_id}')
async def delete_contact_by_id(contact_id: int):
    for i in range(len(CONTACTS)):
        if CONTACTS[i].get('id') == contact_id:
            CONTACTS.pop(i)
        break
    return {"message": "Contact deleted successfully"}

