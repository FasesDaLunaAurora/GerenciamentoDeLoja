from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://loja:loja123@localhost:5432/gerenciamento"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT tablename FROM pg_tables WHERE schemaname='public';"))
    print(result.fetchall())
