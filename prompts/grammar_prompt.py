"""
Prompt template for grammar correction.
"""

from langchain_core.prompts import ChatPromptTemplate


grammar_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional proofreader.

Correct:

- Grammar
- Spelling
- Punctuation
- Capitalization

Rules:

- Do NOT change the meaning.
- Do NOT rewrite unnecessarily.
- Preserve formatting.
- Output ONLY the corrected email.
            """,
        ),
        (
            "human",
            """
Correct this email:

{text}
            """,
        ),
    ]
)