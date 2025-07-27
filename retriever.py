import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from datasets import load_dataset

# 1. Load IMDb dataset
print("Loading IMDb dataset...")
dataset = load_dataset("imdb", split="train[:2000]")
corpus = [f"Review: {review} | Sentiment: {'Positive' if label else 'Negative'}" 
          for review, label in zip(dataset['text'], dataset['label'])]

# 2. Load embedding model
print("Encoding with SentenceTransformer...")
embedder = SentenceTransformer('all-MiniLM-L6-v2')
corpus_embeddings = embedder.encode(corpus, show_progress_bar=True)

# 3. Initialize FAISS index
print("Indexing vectors in FAISS...")
dim = corpus_embeddings[0].shape[0]
index = faiss.IndexFlatL2(dim)
index.add(np.array(corpus_embeddings))

# 4. Load lightweight LLM (FLAN-T5)
print("Loading T5-based language model...")
qa_llm = pipeline("text2text-generation", model="google/flan-t5-base")

# 5. Query-response function
def get_response(query: str, k: int = 3) -> str:
    print(f"\nUser Query: {query}")
    query_embedding = embedder.encode([query])
    _, I = index.search(np.array(query_embedding), k)
    
    context = "\n".join([corpus[i] for i in I[0]])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    
    result = qa_llm(prompt, max_length=200, do_sample=False)
    return result[0]['generated_text']
