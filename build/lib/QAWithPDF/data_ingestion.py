from llama_index.core import SimpleDirectoryReader
import sys
from exception import customException
from logger import logging


def load_data(data):
    """
    Loads data from a specified directory 
    
    Parameter: data(str): Directory path to load data from.

    Returns: list: List of documents loaded from the directory.type of document ,ay vary
    """

    try:
        logging.info(f"Loading data from {data}")
        loader=SimpleDirectoryReader("data")
        documents=loader.load_data()
        logging.info(f"Data loaded successfully from {data}")
        return documents
    except Exception as e:
        logging.error(f"Error occurred while loading data: {e}")
        raise customException(e, sys)
       