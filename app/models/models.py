from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database.database import Base


class Headers(Base):
    __tablename__ = "headers"

    header_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    sales_rep_id: Mapped[int] = mapped_column(ForeignKey('salesrep.sales_rep_id'))
    buyer_id: Mapped[int] = mapped_column(ForeignKey('buyers.buyer_id'))
    active: Mapped[str] = mapped_column(String)

    # Relationships
    buyers: Mapped["Buyers"] = relationship("Buyers", back_populates="headers")
    sales_rep: Mapped["SalesRep"] = relationship("SalesRep", back_populates="headers")
    lines: Mapped[List["Lines"]] = relationship("Lines", back_populates="headers")


class Lines(Base):
    __tablename__ = "lines"

    line_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    header_id: Mapped[int] = mapped_column(ForeignKey('headers.header_id'))
    name: Mapped[str] = mapped_column(String)
    market_id: Mapped[int] = mapped_column(ForeignKey('markets.market_id'))
    item_id: Mapped[int] = mapped_column(ForeignKey('items.item_id'))
    creation_date: Mapped[str] = mapped_column(String)

    # Relationships
    headers: Mapped["Headers"] = relationship("Headers", back_populates="lines")
    markets: Mapped["Markets"] = relationship("Markets", back_populates="lines")
    items: Mapped["Items"] = relationship("Items", back_populates="lines")


class Buyers(Base):
    __tablename__ = "buyers"

    buyer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # Relationships
    headers: Mapped[List["Headers"]] = relationship("Headers", back_populates="buyers")


class Items(Base):
    __tablename__ = "items"

    item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)

    # Relationships
    lines: Mapped[List["Lines"]] = relationship("Lines", back_populates="items")


class Markets(Base):
    __tablename__ = "markets"

    market_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)

    # Relationships
    lines: Mapped[List["Lines"]] = relationship("Lines", back_populates="markets")


class Resource(Base):
    __tablename__ = "resource"

    resource_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # Relationships
    sales_rep: Mapped[List["SalesRep"]] = relationship("SalesRep", back_populates="resource")


class SalesRep(Base):
    __tablename__ = "salesrep"

    sales_rep_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resource_id: Mapped[int] = mapped_column(ForeignKey('resource.resource_id'))

    # Relationships
    headers: Mapped[List["Headers"]] = relationship("Headers", back_populates="sales_rep")
    resource: Mapped["Resource"] = relationship("Resource", back_populates="sales_rep")
