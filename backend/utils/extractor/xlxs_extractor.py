import pandas as pd

# Function to extract text from an XLSX file
def extract_text_from_xlsx(xlsx_path):
    """
    Extracts text from an XLSX file.

    Args:
        xlsx_path (str): Path to the XLSX file.

    Returns:
        str: Extracted text from the XLSX file.
    """
    try:
        df = pd.read_excel(xlsx_path)
        text = df.to_string(index=False)
        return text
    except Exception as e:
        print(f"Error extracting text from XLSX: {e}")
        return ""