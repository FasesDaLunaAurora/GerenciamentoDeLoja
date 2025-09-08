import sys # para manipular o path
import os # para manipular o path
from logging.config import fileConfig # para configurar logging
from sqlalchemy import engine_from_config, pool # para criar o engine do banco
from alembic import context # contexto do Alembic

# adiciona a raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# importa Base e modelos
from src.db import Base
from src.models.insumo_model import Insumo, CategoriaInsumo  # garante que Alembic veja a tabela Insumo
from src.models.cesta_model import Cesta, cesta_insumo_table, CategoriaCesta  # garante que Alembic veja a tabela Cesta
# metadata para autogenerate das migrações do Alembic
target_metadata = Base.metadata

# Configuração do Alembic
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
