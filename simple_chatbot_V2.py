"""
This is an a different implemntation of IBM AI Developer Chatbot like ChatGPT
Stack used:
    - Gemini API for LLM backend
    - Gradio for the frontend
"""

import os

from dotenv import load_dotenv

load_dotenv()


GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
