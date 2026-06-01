import json
import os
from rich import print as rprint

# --- Simulated documents (next week these come from real files/URLs) ---
documents = [
    {
        "id": 1,
        "title": "Introduction to RAG",
        "content": "Retrieval Augmented Generation is a technique that enhances AI responses by fetching relevant documents before generating an answer. It combines the power of search with language models.",
        "source": "ai_handbook.pdf"
    },
    {
        "id": 2,
        "title": "Vector Databases",
        "content": "Vector databases store embeddings — numerical representations of text. They enable semantic search, meaning you can find documents by meaning rather than exact keyword match.",
        "source": "database_guide.pdf"
    },
    {
        "id": 3,
        "title": "FastAPI Basics",
        "content": "FastAPI is a modern Python web framework for building APIs. It is fast, easy to use, and automatically generates documentation. It is the backbone of most Python AI backends.",
        "source": "backend_guide.pdf"
    }
]


def process_document(doc):
    """Takes a raw document, enriches it with metadata."""
    content = doc["content"]
    
    # Chunking — splitting content into smaller pieces
    # Real chunking in Week 2 will be more sophisticated
    words = content.split()
    chunks = []
    chunk_size = 20  # 20 words per chunk
    
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return {
        "id": doc["id"],
        "title": doc["title"],
        "source": doc["source"],
        "word_count": len(words),
        "chunk_count": len(chunks),
        "chunks": chunks
    }


def process_all_documents(documents):
    """Pipeline — processes every document."""
    processed = []
    for doc in documents:
        result = process_document(doc)
        processed.append(result)
        print(f"✓ Processed: {doc['title']} → {result['chunk_count']} chunks")
    return processed


def save_pipeline_output(processed_docs, filename="pipeline_output.json"):
    """Saves processed docs to JSON — ready to be picked up by AI pipeline."""
    with open(filename, "w") as f:
        json.dump(processed_docs, f, indent=2)
    print(f"\n✓ Pipeline output saved to {filename}")


def display_summary(processed_docs):
    """Shows a clean summary using rich."""
    rprint("\n[bold green]===== PIPELINE SUMMARY =====[/bold green]")
    for doc in processed_docs:
        rprint(f"\n[bold]{doc['title']}[/bold]")
        rprint(f"  Source     : {doc['source']}")
        rprint(f"  Words      : {doc['word_count']}")
        rprint(f"  Chunks     : {doc['chunk_count']}")
        rprint(f"  First chunk: [italic]{doc['chunks'][0]}...[/italic]")


# --- Main pipeline ---
print("Starting document processing pipeline...\n")
processed = process_all_documents(documents)
save_pipeline_output(processed)
display_summary(processed)