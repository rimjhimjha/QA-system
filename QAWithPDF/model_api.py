import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
import google.generativeai as genai
from exception import customException
from logger import logging

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the specified model.
    """
    try:
        model = Gemini(model_name='models/gemini-1.5-pro-latest', api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise customException(e, sys)
