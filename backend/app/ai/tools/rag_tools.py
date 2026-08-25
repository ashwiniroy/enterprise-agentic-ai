from langchain.tools import tool

from app.ai.rag.retriever import retrieve_documents


@tool
async def search_knowledge_base(query: str) -> str:
    """
    Search enterprise knowledge from PDF, TXT, and Excel documents.

    Use this tool for questions about:
    - refund policies
    - return policies
    - warranties
    - product information
    - customer support procedures
    """

    documents = await retrieve_documents(
        query=query,
        k=5,
    )

    if not documents:
        return "No relevant enterprise knowledge was found."

    results = []

    for index, document in enumerate(documents, start=1):
        metadata = document.metadata

        source = (
            metadata.get("file_name")
            or metadata.get("source")
            or "unknown"
        )

        results.append(
            f"""
Result {index}

Source: {source}

Content:
{document.page_content}
"""
        )

    return "\n".join(results)