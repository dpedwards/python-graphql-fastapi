from app.database.database import get_db

def get_context():
    return {"db": next(get_db())}
