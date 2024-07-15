from typing import Annotated

from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy.orm import Session
from starlette import status

import model
from model import Contact
from database import engine, SessionLocal

app = FastAPI()

model.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class ContactRequest(BaseModel):
    id: int = Field(description="ID not required on creation", default=None)
    name: str = Field(min_length=3)
    email: EmailStr
    phone: str
    address: str

    model_config = {
        'json_schema_extra': {
            'example': {
                'name': 'John Doe',
                'email': 'john.doe@email.com',
                'phone': '444-444-444',
                'address': '654 Maple St, Thatown, USA'
            }
        }
    }


@app.get("/contacts", status_code=status.HTTP_200_OK)
async def get_all_contacts(db: db_dependency):
    all_contacts = db.query(Contact).all()
    return all_contacts


@app.get("/contacts/search", status_code=status.HTTP_200_OK)
async def search_contact_by_name(db: db_dependency, name: str):
    search_pattern = f"%{name}%"
    searched_contact = db.query(Contact).filter(Contact.name.ilike(search_pattern)).all()
    return searched_contact


@app.get("/contacts/{contact_id}", status_code=status.HTTP_200_OK)
async def get_contact(db: db_dependency, contact_id: int = Path(gt=0)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@app.post("/contacts/create", status_code=status.HTTP_204_NO_CONTENT)
async def create_contact(db: db_dependency, contact: ContactRequest):
    new_contact = Contact(**contact.model_dump())
    db.add(new_contact)
    db.commit()


@app.put("/contacts/update/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_contact(db: db_dependency, contact: ContactRequest, contact_id: int = Path(gt=0)):
    contact_to_update = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact_to_update is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    contact_to_update.name = contact.name
    contact_to_update.email = contact.email
    contact_to_update.phone = contact.phone
    contact_to_update.address = contact.address

    db.add(contact_to_update)
    db.commit()


@app.delete("/contacts/delete/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(db: db_dependency, contact_id: int = Path(gt=0)):
    contact_to_delete = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact_to_delete is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    db.query(Contact).filter(Contact.id == contact_id).delete()
    db.commit()

