from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from app.core.config import settings


DATASET_FILE = (
    Path(__file__).parent
    / "foundry_dataset.jsonl"
)


def upload_dataset():

    project_client = AIProjectClient(
        endpoint=settings.azure_ai_project_endpoint,
        credential=DefaultAzureCredential(),
    )

    dataset = project_client.datasets.upload_file(
        name="enterprise-agentic-ai-evals",
        version="1",
        file_path=str(DATASET_FILE),
    )

    print("\nDataset uploaded successfully")
    print("Name:", dataset.name)
    print("Version:", dataset.version)
    print("ID:", dataset.id)


if __name__ == "__main__":
    upload_dataset()