from app.ai.rag.vector_store import get_vector_store


async def retrieve_documents(
    query: str,
    k: int = 5,
):
    vector_store = await get_vector_store()

    documents = await vector_store.asimilarity_search(
        query=query,
        k=k,
    )

    return documents