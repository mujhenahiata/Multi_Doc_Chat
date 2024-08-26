import chromadb

# Store embeddings in ChromaDB
def chromadb_vector_store(embeddings, paragraphs, collection_name):
    """
    Stores embeddings in a ChromaDB collection.

    Args:
        embeddings (List): List of embeddings to store.
        paragraphs (List[str]): List of text paragraphs corresponding to the embeddings.
        collection_name (str): Name of the ChromaDB collection.

    Returns:
        chromadb.Collection: The collection where embeddings are stored.
    """
    try:
        client = chromadb.HttpClient(host='localhost', port=8001)  # ChromaDB port
        collection = client.get_or_create_collection(
            name=collection_name, metadata={"hnsw:space": "cosine"})

        # Add embeddings to the collection
        n = len(paragraphs)
        collection.add(
            ids=[str(id) for id in range(n)],
            embeddings=[embedding for embedding in embeddings],
            documents=[paragraph for paragraph in paragraphs],
            metadatas=[{"doc_id": i} for i in range(n)],
        )

        print("Stored embeddings in ChromaDB collection")
        return collection
    except Exception as e:
        print(f"Error storing embeddings in ChromaDB: {e}")
        return None

# Function to delete the embeddings and collection from ChromaDB
def delete_from_chromadb(collection_name):
    """
    Delete a collection and its associated embeddings from ChromaDB.

    Parameters:
    collection_name (str): The name of the collection to delete.
    """
    try:
        client = chromadb.HttpClient(host='localhost', port=8001)  # ChromaDB port
        collection = client.get_collection(name=collection_name)
        if collection:
            client.delete_collection(collection_name)
            print(f"Collection {collection_name} deleted from ChromaDB")
    except Exception as e:
        print(f"Error deleting collection from ChromaDB: {e}")

