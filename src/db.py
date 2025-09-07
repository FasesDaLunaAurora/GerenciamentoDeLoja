from sqlalchemy import create_engine # cria o engine do banco
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker cria sessões, declarative_base é a base para os modelos
import os # para variáveis de ambiente

# URL do banco de dados (pegando do .env ou, caso não consifa, pega fixa)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://loja:loja123@localhost:5432/gerenciamento"
)

engine = create_engine(DATABASE_URL, echo=True) # conecta ao banco e habilita logging de SQL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # cria sessões vinculadas ao engine

Base = declarative_base() # base para os modelos


# Dependência para injeção (FastAPI ou uso manual)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
