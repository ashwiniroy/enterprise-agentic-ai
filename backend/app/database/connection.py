from azure.identity import DefaultAzureCredential
from sqlalchemy import create_engine, event
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import settings


# Azure PostgreSQL token scope
POSTGRES_SCOPE = "https://ossrdbms-aad.database.windows.net/.default"

credential = DefaultAzureCredential()


# ============================================================
# DATABASE URL
# ============================================================

sync_database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.postgres_user,
    host=settings.postgres_host,
    port=settings.postgres_port,
    database=settings.postgres_database,
)


# ============================================================
# SYNC ENGINE
# ============================================================

engine = create_engine(
    sync_database_url,
    connect_args={
        "sslmode": settings.postgres_sslmode,
    },
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800,
)


@event.listens_for(engine, "do_connect")
def provide_sync_token(
    dialect,
    conn_rec,
    cargs,
    cparams,
):
    token = credential.get_token(
        POSTGRES_SCOPE
    )

    cparams["password"] = token.token


# ============================================================
# ASYNC ENGINE
# ============================================================

async_engine = create_async_engine(
    sync_database_url,
    connect_args={
        "sslmode": settings.postgres_sslmode,
    },
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800,
)


@event.listens_for(
    async_engine.sync_engine,
    "do_connect",
)
def provide_async_token(
    dialect,
    conn_rec,
    cargs,
    cparams,
):
    token = credential.get_token(
        POSTGRES_SCOPE
    )

    cparams["password"] = token.token