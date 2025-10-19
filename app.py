#from sentence_transformers import SentenceTransformer
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load a pre-trained sentence transformer model (e.g., 'all-MiniLM-L6-v2')
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your documents (text chunks)
documents = [
    "Hello. Hello. Ah, hello, Ms. Heinz. Hello, nice to see you again...",
    "Social Roles: Teacher (Weak), Principal (Strong)... Communicative Action types: Strategic, Understanding-Oriented...",
    "Dialogue Rules: Teacher initiates politely, Principal questions relevance and cost...",
    "Actor Profiles and Goals: Teacher Heinz: weak social role, seeks approval. Principal Horn: strong social role, skeptical...",
    "Instructions for Role-Playing Participants: Teacher emphasizes school benefits, responds to cost/time concerns..."
]

# Step 1: Generate embeddings for all documents
embeddings = model.encode(documents, convert_to_numpy=True, normalize_embeddings=True)

# Step 2: Create FAISS index for cosine similarity search
index = faiss.IndexFlatIP(embeddings.shape[1])  # Inner product = cosine similarity (since normalized)
index.add(embeddings)

print(f"Indexed {index.ntotal} documents.")

# Step 3: Query example
query = "What are the principal's concerns about the training cost?"
query_embedding = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)

k = 3  # number of top results
distances, indices = index.search(query_embedding, k)

print("Top documents relevant to query:")
for i, dist in zip(indices[0], distances[0]):
    print(f"Document: {documents[i][:60]}... | Score: {dist:.4f}")