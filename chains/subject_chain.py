"""
chains/subject_chain.py
-----------------------

Chain responsible for generating email subject lines.
"""

from langchain_core.output_parsers import StrOutputParser

from models.llm import get_llm
from prompts.subject_prompt import subject_prompt


llm = get_llm()

subject_chain = (
    subject_prompt
    | llm
    | StrOutputParser()
)