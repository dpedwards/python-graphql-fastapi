from typing import Optional, List
import strawberry


# Define the Buyers type
@strawberry.type
class Buyers:
    buyer_id: int
    name: Optional[str]


# Input type for creating or updating buyers
@strawberry.input
class BuyersInput:
    buyer_id: int
    name: Optional[str]


# Input type for deleting buyers
@strawberry.input
class BuyersDelete:
    buyer_id: int


# Define the SalesRep type
@strawberry.type
class SalesRep:
    sales_rep_id: int
    resource_id: int
    resource: Optional["Resource"]  # Referencing another type


# Define the Resource type
@strawberry.type
class Resource:
    resource_id: int
    name: Optional[str]


# Define the Items type
@strawberry.type
class Items:
    item_id: int
    name: Optional[str]
    description: Optional[str]


# Define the Markets type
@strawberry.type
class Markets:
    market_id: int
    name: Optional[str]
    location: Optional[str]


# Define the Lines type with relationships to Markets and Items
@strawberry.type
class Lines:
    line_id: int
    header_id: int
    name: Optional[str]
    market_id: int
    item_id: int
    creation_date: str
    markets: Optional[Markets] = None
    items: Optional[Items] = None


# Define the Headers type with relationships to Buyers, SalesRep, and Lines
@strawberry.type
class Headers:
    header_id: int
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    buyers: Optional[Buyers] = None
    sales_rep: Optional[SalesRep] = None
    lines: Optional[List[Lines]] = None  # List of related lines


# Input type for creating or updating headers
@strawberry.input
class HeadersInput:
    header_id: int
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]


# Input type for deleting headers
@strawberry.input
class HeadersDelete:
    header_id: int
