from langchain_community.document_loaders.csv_loader import CSVLoader
    
# Function to extract text from a CSV file
def extract_text_from_csv(csv_path):
    """
    Extracts text from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        str: Extracted text from the CSV file.
    """
    try:
        loader = CSVLoader(file_path=csv_path)
        data = loader.load()
        text = "\n".join([str(record) for record in data])
        return text
    except Exception as e:
        print(f"Error extracting text from CSV: {e}")
        return ""
