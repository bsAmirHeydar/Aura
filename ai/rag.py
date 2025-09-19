import os
from docx import Document
import faiss
import numpy as np
from ai.embedder import Embedder

class RAG:
    def __init__(self, folder_path="data", model_name="paraphrase-multilingual-MiniLM-L12-v2", chunk_size=200):
        self.embedder = Embedder(model_name)
        self.chunks = self._load_all_docs(folder_path, chunk_size)
        self.index = self._build_index()

    def _load_word(self, path):
        doc = Document(path)
        return [p.text for p in doc.paragraphs if p.text.strip()]

    def _chunk_texts(self, texts, chunk_size):
        chunks = []
        for text in texts:
            words = text.split()
            for i in range(0, len(words), chunk_size):
                chunks.append(" ".join(words[i:i+chunk_size]))
        return chunks

    def _load_all_docs(self, folder_path, chunk_size):
        all_chunks = []
        for file in os.listdir(folder_path):
            if file.endswith(".docx"):
                path = os.path.join(folder_path, file)
                texts = self._load_word(path)
                chunks = self._chunk_texts(texts, chunk_size)
                all_chunks.extend(chunks)
        return all_chunks

    def _build_index(self):
        vectors = self.embedder.encode(self.chunks)
        dim = vectors.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(vectors))
        return index

    def search(self, query, k=3):
        q_vec = self.embedder.encode(query)
        D, I = self.index.search(np.array(q_vec), k)
        return [self.chunks[i] for i in I[0]]
