from langchain_openai import AzureOpenAIEmbeddings

from app.core.config import settings


def get_embedding_model():
    return AzureOpenAIEmbeddings(
        azure_endpoint=settings.azure_openai_endpoint,
        api_key=settings.azure_openai_api_key,
        azure_deployment=settings.azure_openai_embedding_deployment,
        api_version=settings.azure_openai_api_version,
    )