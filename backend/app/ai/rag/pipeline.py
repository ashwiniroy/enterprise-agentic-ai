from langchain_core.messages import HumanMessage, SystemMessage

from app.ai.models.chat_model import get_chat_model
from app.ai.rag.retriever import retrieve_documents


SYSTEM_PROMPT = """
You are an enterprise customer-support assistant.

Answer only from the retrieved context.

Rules:
1. Do not invent information.
2. If the answer is not present, say you do not have enough information.
3. Prefer product-specific information over generic policy information.
4. Keep the answer concise and factual.
"""


async def ask_rag(question: str):
    documents = await retrieve_documents(
        query=question,
        k=5,
    )

    # Keep the rest of your existing RAG logic here.

    context = "\n\n".join(
        f"""
Source: {doc.metadata.get("file_name") or doc.metadata.get("source")}

Content:
{doc.page_content}
"""
        for doc in documents
    )

    model = get_chat_model()

    response = model.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"""
Retrieved context:

{context}

Question:

{question}
"""
            ),
        ]
    )

    sources = []

    for doc in documents:
        metadata = doc.metadata

        sources.append(
            {
                "file_name": metadata.get("file_name")
                or metadata.get("source"),
                "file_type": metadata.get("file_type"),
                "page": metadata.get("page"),
                "sheet": metadata.get("sheet"),
                "row": metadata.get("row"),
                "chunk_index": metadata.get("chunk_index"),
            }
        )

    return {
        "answer": str(response.content),
        "sources": sources,
    }