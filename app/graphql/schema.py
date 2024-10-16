from typing import List
import strawberry
from app.graphql.definitions import (
    Headers, Lines, Buyers, Items, Markets, SalesRep, Resource, BuyersInput,
    BuyersDelete, HeadersInput, HeadersDelete
)
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import Session
from app.routers.routers import (
    get_headers as fetch_headers, get_lines as fetch_lines, get_buyers as fetch_buyers,
    get_items as fetch_items, get_markets as fetch_markets, get_resource as fetch_resource,
    get_salesrep as fetch_salesrep, insert_buyer, update_buyer, delete_buyer,
    insert_header, update_header, delete_header
)

def get_context():
    from main import get_context as main_get_context  # Lazy import to avoid circular dependency
    return main_get_context()

@strawberry.type
class Query:
    @strawberry.field
    def get_headers(self, info) -> List[Headers]:
        db: Session = info.context["db"]
        return fetch_headers(db)

    @strawberry.field
    def get_lines(self, info) -> List[Lines]:
        db: Session = info.context["db"]
        return fetch_lines(db)

    @strawberry.field
    def get_buyers(self, info) -> List[Buyers]:
        db: Session = info.context["db"]
        return fetch_buyers(db)

    @strawberry.field
    def get_items(self, info) -> List[Items]:
        db: Session = info.context["db"]
        return fetch_items(db)

    @strawberry.field
    def get_markets(self, info) -> List[Markets]:
        db: Session = info.context["db"]
        return fetch_markets(db)

    @strawberry.field
    def get_resource(self, info) -> List[Resource]:
        db: Session = info.context["db"]
        return fetch_resource(db)

    @strawberry.field
    def get_salesrep(self, info) -> List[SalesRep]:
        db: Session = info.context["db"]
        return fetch_salesrep(db)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_buyer(self, buyer: BuyersInput, info) -> Buyers:
        db: Session = info.context["db"]
        return insert_buyer(buyer, db)

    @strawberry.mutation
    def update_buyer(self, buyer: BuyersInput, info) -> Buyers:
        db: Session = info.context["db"]
        return update_buyer(buyer, db)

    @strawberry.mutation
    def delete_buyer(self, buyer: BuyersDelete, info) -> bool:
        db: Session = info.context["db"]
        return delete_buyer(buyer_id=buyer.buyer_id, db=db)

    @strawberry.mutation
    def create_header(self, header: HeadersInput, info) -> Headers:
        db: Session = info.context["db"]
        return insert_header(header, db)

    @strawberry.mutation
    def update_header(self, header: HeadersInput, info) -> Headers:
        db: Session = info.context["db"]
        return update_header(header, db)

    @strawberry.mutation
    def delete_header(self, header: HeadersDelete, info) -> bool:
        db: Session = info.context["db"]
        return delete_header(header_id=header.header_id, db=db)

# Create schema with both Query and Mutation classes
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Use the imported get_context in your GraphQLRouter as shown before.
graphql_app = GraphQLRouter(schema, context_getter=get_context)
