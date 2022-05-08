from .config import settings
from schema.schema import db


async def init_db():
    db.bind(
        provider="postgres",
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        database=settings.DATABASE_NAME,
    )
    # db.bind(provider="sqlite", filename="test.db", create_db=True)
    print("[+] Generating database schema")
    db.generate_mapping(create_tables=True)
