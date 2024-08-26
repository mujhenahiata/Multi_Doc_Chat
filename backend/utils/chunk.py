from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Function to chunk text into smaller pieces
def chunk_text(text, chunk_size=1000, chunk_overlap=50):
    """
    Splits text into smaller chunks for better processing.

    Args:
        text (str): The text to be split.
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The overlap between chunks.

    Returns:
        List[str]: List of text chunks.
    """
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        doc_output = splitter.split_documents([Document(page_content=text)])
        # print(doc_output)
        # Convert the Document objects to a list of strings
        result = [doc.page_content for doc in doc_output]
        # print(result)
        return result
    except Exception as e:
        print(f"Error chunking text: {e}")
        return []