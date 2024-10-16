from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.models.models import Headers, Lines, Buyers, Items, Markets, Resource, SalesRep
from app.models.schema import HeadersModel, LinesModel, BuyersModel, ItemsModel, MarketsModel, ResourceModel, SalesRepModel
from app.database.database import get_db  # Make sure this is correctly imported
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# Headers routes
@router.get("/headers", response_model=None, tags=["headers"])
async def get_headers(db: Session = Depends(get_db)):
    headers = db.query(Headers).all()
    return headers

@router.post("/add-headers/", tags=["headers"])
async def insert_header(header: HeadersModel, db: Session = Depends(get_db)):
    new_header = Headers(
        header_id=header.header_id,
        name=header.name,
        sales_rep_id=header.sales_rep_id,
        buyer_id=header.buyer_id,
        active=header.active
    )

    db.add(new_header)
    db.commit()
    db.refresh(new_header)
    return new_header

@router.put("/update-headers/", tags=["headers"])
async def update_header(updated_header: HeadersModel, db: Session = Depends(get_db)):
    existing_header = db.query(Headers).filter(Headers.header_id == updated_header.header_id).first()

    if existing_header:
        for field, value in jsonable_encoder(updated_header).items():
            if value is not None:
                setattr(existing_header, field, value)

        db.commit()
        db.refresh(existing_header)
        return existing_header

    return {"message": "Header not found"}

@router.delete("/delete-headers/{header_id}", tags=["headers"])
async def delete_header(header_id: int, db: Session = Depends(get_db)):
    existing_header = db.query(Headers).filter(Headers.header_id == header_id).first()

    if existing_header:
        db.delete(existing_header)
        db.commit()
        return True

    return False

# Lines routes
@router.get("/lines", response_model=None, tags=["lines"])
async def get_lines(db: Session = Depends(get_db)) -> List[LinesModel]:
    lines = db.query(Lines).all()
    return lines

# Buyers routes
@router.get("/buyers", response_model=None, tags=["buyers"])
async def get_buyers(db: Session = Depends(get_db)):
    buyers = db.query(Buyers).all()
    return buyers

@router.post("/add-buyers/", tags=["buyers"])
async def insert_buyer(buyer: BuyersModel, db: Session = Depends(get_db)):
    new_buyer = Buyers(
        buyer_id=buyer.buyer_id,
        name=buyer.name,
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return new_buyer

@router.put("/update-buyer/", tags=["buyers"])
async def update_buyer(updated_buyer: BuyersModel, db: Session = Depends(get_db)):
    existing_buyer = db.query(Buyers).filter(Buyers.buyer_id == updated_buyer.buyer_id).first()

    if existing_buyer:
        update_item_encoded = jsonable_encoder(updated_buyer)
        for field, value in update_item_encoded.items():
            if field != "buyer_id" and value is not None:
                setattr(existing_buyer, field, value)

        db.commit()
        db.refresh(existing_buyer)
        return existing_buyer

    return {"message": "Buyer not found"}

@router.delete("/delete-buyer/{buyer_id}", tags=["buyers"])
async def delete_buyer(buyer_id: int, db: Session = Depends(get_db)):
    existing_buyer = db.query(Buyers).filter(Buyers.buyer_id == buyer_id).first()

    if existing_buyer:
        db.delete(existing_buyer)
        db.commit()
        return True

    return False

# Items routes
@router.get("/items", response_model=None, tags=["items"])
async def get_items(db: Session = Depends(get_db)) -> List[ItemsModel]:
    items = db.query(Items).all()
    return items

# Markets routes
@router.get("/markets", response_model=None, tags=["markets"])
async def get_markets(db: Session = Depends(get_db)) -> List[MarketsModel]:
    markets = db.query(Markets).all()
    return markets

# Resource routes
@router.get("/resource", response_model=None, tags=["resource"])
async def get_resource(db: Session = Depends(get_db)) -> List[ResourceModel]:
    resource = db.query(Resource).all()
    return resource

# SalesRep routes
@router.get("/salesrep", response_model=None, tags=["salesrep"])
async def get_salesrep(db: Session = Depends(get_db)) -> List[SalesRepModel]:
    salesrep = db.query(SalesRep).all()
    return salesrep
