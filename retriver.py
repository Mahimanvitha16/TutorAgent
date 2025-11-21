import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB client and collection
client = chromadb.Client()

collection = client.create_collection(
    name="study_notes",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

# Sample documents — can be replaced with your own notes
documents = [
    "Photosynthesis is the process by which plants convert light energy into chemical energy.",
    "Chlorophyll absorbs sunlight to initiate photosynthesis.",
    "Mitochondria are often called the powerhouse of the cell.",
    "A noun is a word that represents a person, place, or thing."
]

collection.add(
    documents=documents,
    ids=[str(i) for i in range(len(documents))]
)

def retrieve_notes(query):
    """
    Retrieves the top relevant notes from ChromaDB.
    """
    results = collection.query(query_texts=[query], n_results=2)
    return results["documents"][0]


