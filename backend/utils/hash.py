import hashlib

file_hash_map = {}

def get_file_hash_map(): 
    # Hash map to keep track of file metadata
    return file_hash_map

# Add file metadata to the hash map
def add_to_hash_map(file_name):
    """
    Adds file metadata to the hash map by generating a hash.

    Args:
        file_name (str): The name of the file.
    """
    try:
        file_hash_map[str(file_name)] = generate_hash(file_name)
    except Exception as e:
        print(f"Error adding to hash map: {e}")


# Generate a hash from an input string
def generate_hash(input_string):
    """
    Generates a SHA-256 hash from a string.

    Args:
        input_string (str): The input string to hash.

    Returns:
        str: The resulting hash.
    """
    try:
        hash_object = hashlib.sha256(input_string.encode())
        return hash_object.hexdigest()
    except Exception as e:
        print(f"Error generating hash: {e}")
        return ""

