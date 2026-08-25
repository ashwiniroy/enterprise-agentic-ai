import pandas as pd

from langchain_core.documents import Document


def load_excel(file_path: str):
    excel_file = pd.ExcelFile(file_path)

    documents = []

    for sheet_name in excel_file.sheet_names:
        dataframe = pd.read_excel(
            file_path,
            sheet_name=sheet_name,
        )

        dataframe = dataframe.fillna("")

        for row_index, row in dataframe.iterrows():

            values = []

            for column in dataframe.columns:
                value = row[column]

                if str(value).strip():
                    values.append(
                        f"{column}: {value}"
                    )

            if not values:
                continue

            content = "\n".join(values)

            document = Document(
                page_content=content,
                metadata={
                    "source": file_path,
                    "file_type": "xlsx",
                    "sheet": sheet_name,
                    "row": int(row_index) + 2,
                },
            )

            documents.append(document)

    return documents