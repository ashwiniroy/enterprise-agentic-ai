import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

BACKEND_PATH = PROJECT_ROOT / "backend"

sys.path.insert(
    0,
    str(BACKEND_PATH),
)


from app.ai.rag.ingestion import ingest_file


DATA_DIRECTORY = (
    PROJECT_ROOT
    / "data"
    / "raw"
)


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".xlsx",
}


def main():

    files = sorted(
        [
            file
            for file in DATA_DIRECTORY.iterdir()
            if file.suffix.lower()
            in SUPPORTED_EXTENSIONS
        ]
    )

    if not files:

        print(
            "No supported files found in data/raw"
        )

        return

    print(
        f"Found {len(files)} file(s)"
    )

    for file in files:

        try:

            ingest_file(
                str(file)
            )

        except Exception as error:

            print(
                f"ERROR while processing "
                f"{file.name}: {error}"
            )


if __name__ == "__main__":
    main()