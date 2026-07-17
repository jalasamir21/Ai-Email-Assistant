"""
models/llm.py
-------------

Centralized LLM initialization.

Every part of the project imports the language model from here instead of
creating new ChatGroq instances.
"""

from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
)


def get_llm(
    model_name: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
):
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=model_name,
        temperature=temperature,
    )