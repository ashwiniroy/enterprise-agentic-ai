from pathlib import Path

from app.ai.rag.chunking import split_documents
from app.ai.rag.loaders.file_loader import load_file
from app.ai.rag.vector_store import get_vector_store


async def ingest_file(file_path: str):

    path = Path(file_path)

    print(f"\nLoading: {path.name}")

    documents = load_file(file_path)

    print(f"Documents extracted: {len(documents)}")

    if path.suffix.lower() in {".pdf", ".txt"}:
        documents = split_documents(documents)

    print(f"Documents after chunking: {len(documents)}")

    for index, document in enumerate(documents):
        document.metadata.update(
            {
                "file_name": path.name,
                "file_type": path.suffix.lower(),
                "chunk_index": index,
            }
        )

    vector_store = await get_vector_store()

    ids = await vector_store.aadd_documents(documents)

    print(f"Inserted {len(ids)} documents into pgvector.")

    return ids