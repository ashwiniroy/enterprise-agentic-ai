from langchain_openai import AzureChatOpenAI

from app.core.config import settings


def get_chat_model():
    return AzureChatOpenAI(
        azure_endpoint=settings.azure_openai_endpoint,
        api_key=settings.azure_openai_api_key,
        azure_deployment=settings.azure_openai_chat_deployment,
        api_version=settings.azure_openai_api_version,
        temperature=0,
    )