from typing import Optional

from fastapi import FastAPI, HTTPException, Path
from pydantic import Field, EmailStr, BaseModel
from starlette import status

app = FastAPI()


# Contact Schema Model
class Contact:
    id: int
    name: str
    email: str
    phone: str
    address: str

    def __init__(self, id, name, email, phone, address):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


# Contact Request Schema
class ContactRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not required on creation", default=None)
    name: str = Field(min_length=3)
    email: EmailStr
    phone: str
    address: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Doe",
                "email": "john.doe@email.com",
                "phone": "234 XXX XXXX XX",
                "address": "321 Pine St, Thistown, USA"
            }
        }
    }


CONTACTS = [
    Contact(1, "Alice Johnson", "alice.johnson@example.com", "123-456-7890", "123 Main St, Anytown, USA"),
    Contact(2, "Bob Smith", "bob.smith@example.com", "987-654-3210", "456 Elm St, Othertown, USA"),
    Contact(3, "Charlie Brown", "charlie.brown@example.com", "555-555-5555", "789 Oak St, Sometown, USA"),
    Contact(4, "Dana White", "dana.white@example.com", "444-444-4444", "321 Pine St, Thistown, USA"),
    Contact(5, "Eve Black", "eve.black@example.com", "333-333-3333", "654 Maple St, Thatown, USA")
]


# FECTCH ALL BOOKS
@app.get('/contacts', status_code=status.HTTP_200_OK)
async def list_all_contacts():
    return CONTACTS


# FETCH A CONTACT
@app.get('/contact/{contact_id}', status_code=status.HTTP_200_OK)
async def get_contact_by_id(contact_id: int = Path(gt=0)):
    for contact in CONTACTS:
        if contact.id == contact_id:
            return contact
    raise HTTPException(detail="Contact not found", status_code=404)


# SEARCH CONTACT BY NAME
@app.get('/contact/search/', status_code=status.HTTP_200_OK)
async def search_contact_by_name(name: str):
    contacts_to_return = []
    for i in range(len(CONTACTS)):
        if name.casefold() in CONTACTS[i].name.casefold():
            contacts_to_return.append(CONTACTS[i])
    return contacts_to_return


# CREATE NEW CONTACT
@app.post('/contact/create', status_code=status.HTTP_201_CREATED)
async def create_new_contact(new_contact: ContactRequest):
    contact = Contact(**new_contact.model_dump())
    generate_id(contact)
    CONTACTS.append(contact)


# UPDATE CONTACT
@app.put('/contact/update/{contact_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_contact(contact_to_update: ContactRequest):
    contact_updated = False
    for i in range(len(CONTACTS)):
        if CONTACTS[i].id == contact_to_update.id:
            CONTACTS[i] = contact_to_update
            contact_updated = True
    if not contact_updated:
        raise HTTPException(detail="Contact not found", status_code=404)


# DELETE CONTACT
@app.delete('/contact/delete/{contact_id}')
async def delete_contact_by_id(contact_id: int):
    contact_updated = False
    for i in range(len(CONTACTS)):
        if CONTACTS[i].id == contact_id:
            CONTACTS.pop(i)
            contact_updated = True
        break
    if not contact_updated:
        raise HTTPException(detail="Contact not found", status_code=404)


# Generate id
def generate_id(contact: Contact):
    contact.id = 1 if len(CONTACTS) == 0 else CONTACTS[-1].id + 1
