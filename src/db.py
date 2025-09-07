from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL do banco de dados (pegando do .env ou fixa)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://loja:loja123@localhost:5432/gerenciamento"
)

# Cria o engine
engine = create_engine(DATABASE_URL, echo=True)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()


# Dependência para injeção (FastAPI ou uso manual)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
