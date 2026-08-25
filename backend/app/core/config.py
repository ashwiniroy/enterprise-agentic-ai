from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# enterprise-agentic-ai/.env
PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE = PROJECT_ROOT / ".env"


class Settings(BaseSettings):
    # Application
    app_name: str = "Enterprise Agentic AI"
    app_env: str = "local"

    # Azure OpenAI
    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_chat_deployment: str
    azure_openai_embedding_deployment: str
    azure_openai_api_version: str

    # Microsoft Foundry
    azure_ai_project_endpoint: str

    # Application Insights
    applicationinsights_connection_string: str | None = None

    # Azure PostgreSQL
    postgres_host: str
    postgres_port: int = 5432
    postgres_database: str
    postgres_user: str
    postgres_sslmode: str = "require"
    postgres_auth_mode: str = "entra"

    # Temporary compatibility with existing RAG code
    database_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()