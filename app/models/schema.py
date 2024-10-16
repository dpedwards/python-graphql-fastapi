from dataclasses import dataclass
from typing import Optional, List


@dataclass
class BuyersModel:
    buyer_id: int
    name: Optional[str]


@dataclass
class ItemsModel:
    item_id: int
    name: Optional[str]
    description: Optional[str]


@dataclass
class MarketsModel:
    market_id: int
    name: Optional[str]
    location: Optional[str]


@dataclass
class ResourceModel:
    resource_id: int
    name: Optional[str]


@dataclass
class SalesRepModel:
    sales_rep_id: int
    resource_id: Optional[int]

    # Reflect the relationships
    resource: Optional[ResourceModel] = None


@dataclass
class LinesModel:
    line_id: int
    header_id: Optional[int]
    name: Optional[str]
    market_id: Optional[int]
    item_id: Optional[int]
    creation_date: Optional[str]

    # Relationship to Markets and Items
    market: Optional[MarketsModel] = None
    items: Optional[ItemsModel] = None


@dataclass
class HeadersModel:
    header_id: int
    name: Optional[str]
    sales_rep_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]

    # Relationships to Buyers, SalesRep, and Lines
    buyers: Optional[BuyersModel] = None
    sales_rep: Optional[SalesRepModel] = None
    lines: Optional[List[LinesModel]] = None  # Changed to Optional[List] for handling no lines case

