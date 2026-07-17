"""
chains/grammar_chain.py
-----------------------

Chain responsible for grammar correction.
"""

from langchain_core.output_parsers import StrOutputParser

from models.llm import get_llm
from prompts.grammar_prompt import grammar_prompt


llm = get_llm()

grammar_chain = (
    grammar_prompt
    | llm
    | StrOutputParser()
)