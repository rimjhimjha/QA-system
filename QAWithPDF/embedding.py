from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini

import sys
from exception import customException
from logger import logging

def download_gemini_embedding(api_key: str, documents):
    """
    Downloads and initializes a Gemini Embedding model and LLM for vector embeddings.

    Args:
        api_key (str): Your Google Cloud API key.
        documents (List[Document]): A list of LlamaIndex Document objects.

    Returns:
        QueryEngine: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("Initializing Gemini embedding model and LLM...")
        gemini_embed_model = GeminiEmbedding(
            model_name="models/embedding-001", api_key=api_key
        )
        gemini_llm = Gemini(model_name="gemini-pro", api_key=api_key)

        node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)

        logging.info("Building vector store index...")
        index = VectorStoreIndex.from_documents(
            documents=documents,
            storage_context=StorageContext.from_defaults(),
            llm=gemini_llm,
            embed_model=gemini_embed_model,
            node_parser=node_parser
        )

        index.storage_context.persist()
        logging.info("Vector store index created and saved.")

        query_engine = index.as_query_engine()
        return query_engine

    except Exception as e:
        logging.error(f"Error during Gemini embedding setup: {e}")
        raise customException(e, sys)
