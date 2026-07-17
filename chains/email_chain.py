"""
chains/email_chain.py
---------------------

Chain responsible for generating complete emails.
"""

from langchain_core.output_parsers import StrOutputParser

from models.llm import get_llm
from prompts.email_prompt import email_prompt


llm = get_llm()

email_chain = (
    email_prompt
    | llm
    | StrOutputParser()
)