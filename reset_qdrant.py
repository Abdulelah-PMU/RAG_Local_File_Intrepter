from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

if client.collection_exists("docs"):
    client.delete_collection("docs")
    print("Collection deleted!")
else:
    print("Collection doesn't exist")


print(client.get_collections())

