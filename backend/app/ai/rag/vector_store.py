from langchain_postgres import PGEngine, PGVectorStore

from app.ai.models.embedding_model import get_embedding_model
from app.database.connection import async_engine


TABLE_NAME = "enterprise_knowledge"

pg_engine = PGEngine.from_engine(
    engine=async_engine
)


async def get_vector_store():
    embedding_model = get_embedding_model()

    return await PGVectorStore.create(
        engine=pg_engine,
        table_name=TABLE_NAME,
        embedding_service=embedding_model,
    )