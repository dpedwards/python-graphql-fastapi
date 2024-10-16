import sqlalchemy
from fastapi import FastAPI
from app.database.database import engine, Base, get_db
from app.graphql.schema import graphql_app  # Ensure graphql_app is correctly imported
from app.routers import routers

# Create all tables on app startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Define context to include the database session
def get_context() -> dict:
    db = next(get_db())
    return {"db": db}

# Attach the routers, including the GraphQL router
app.include_router(graphql_app, prefix="/graphql")
app.include_router(routers.router)

@app.on_event("startup")
async def startup():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    print("Database connected on startup")

@app.on_event("shutdown")
async def shutdown():
    engine.dispose()
    print("Database disconnected on shutdown")
