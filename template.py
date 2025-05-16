import os
import logging  
from pathlib import Path

list_of_files = [
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "StreamlitApp.py",
    "logger.py",  
    "exception.py",
    "setup.py",
    "Experiments/experiment1.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # Just create an empty file
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")