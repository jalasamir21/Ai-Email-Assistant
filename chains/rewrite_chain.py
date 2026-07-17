"""
chains/rewrite_chain.py
-----------------------

Chain responsible for rewriting emails.
"""

from langchain_core.output_parsers import StrOutputParser

from models.llm import get_llm
from prompts.rewrite_prompt import rewrite_prompt


llm = get_llm()

rewrite_chain = (
    rewrite_prompt
    | llm
    | StrOutputParser()
)