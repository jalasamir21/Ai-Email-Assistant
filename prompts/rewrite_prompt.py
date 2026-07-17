"""
Prompt template for rewriting emails.
"""

from langchain_core.prompts import ChatPromptTemplate


rewrite_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert email editor.

Rewrite the email according to the user's instructions.

Rules:

- Preserve the original meaning.
- Improve clarity and readability.
- Maintain professionalism unless instructed otherwise.
- Correct grammar and punctuation.
- Keep important details unchanged.
- Output ONLY the rewritten email.
            """,
        ),
        (
            "human",
            """
Instructions:

{instruction}

Original Email:

{email}
            """,
        ),
    ]
)