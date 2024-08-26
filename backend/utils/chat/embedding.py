import ollama
import json
import os

# Load and save embeddings using JSON files
def save_embeddings(filename, embeddings):
    """
    Save embeddings to a JSON file.

    Parameters:
    filename (str): The name of the file to save the embeddings to.
    embeddings (List[List[float]]): The embeddings to save.
    """
    try:
        if not os.path.exists("embeddings"):
            os.makedirs("embeddings")
        with open(f"embeddings/{filename}.json", "w") as f:
            json.dump(embeddings, f)
    except Exception as e:
        print(f"Error saving embeddings: {e}")


def load_embeddings(filename):
    """
    Load embeddings from a JSON file.

    Parameters:
    filename (str): The name of the file to load the embeddings from.

    Returns:
    List[List[float]]: The loaded embeddings, or False if loading fails.
    """
    try:
        if not os.path.exists(f"embeddings/{filename}.json"):
            return False
        with open(f"embeddings/{filename}.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading embeddings: {e}")
        return False
    
# Function to get or generate embeddings
def get_embeddings(filename, modelname, chunks):
    """
    Get or generate embeddings for the provided chunks of text.

    Parameters:
    filename (str): The name of the file associated with the embeddings.
    modelname (str): The name of the model to use for generating embeddings.
    chunks (List[str]): The chunks of text to generate embeddings for.

    Returns:
    List[List[float]]: The embeddings for the provided chunks.
    """
    try:
        if (embeddings := load_embeddings(filename)) is not False:
            return embeddings
        embeddings = [
            ollama.embeddings(model=modelname, prompt=chunk)["embedding"]
            for chunk in chunks
        ]
        save_embeddings(filename, embeddings)
        return embeddings
    except Exception as e:
        print(f"Error getting embeddings: {e}")
        return []
