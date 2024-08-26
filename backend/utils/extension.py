import os 

# Function to get file extension
def get_file_extension(file_path):
    """
    Gets the extension of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File extension in lowercase.
    """
    try:
        return os.path.splitext(file_path)[1].lower()
    except Exception as e:
        print(f"Error getting file extension: {e}")
        return ""