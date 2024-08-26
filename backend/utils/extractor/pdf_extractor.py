from langchain_community.document_loaders import PyPDFLoader

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF file.
    """
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        text = "\n".join(page.page_content for page in pages)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""