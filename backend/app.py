from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "sqlite:///./items.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class ItemCreate(BaseModel):
    name: str

@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    with SessionLocal() as session:
        existing: Item | None = session.query(Item).filter(Item.name == item.name).first()
        if existing:
            raise HTTPException(status_code=400, detail="Item already exists")
        new_item = Item(name=item.name)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return {"id": new_item.id, "name": new_item.name}
