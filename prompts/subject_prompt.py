"""
Prompt template for generating email subjects.
"""

from langchain_core.prompts import ChatPromptTemplate


subject_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert business communication assistant.

Generate ONE concise and professional email subject.

Rules:

- Keep it under 12 words.
- Be specific.
- Do not use quotation marks.
- Output ONLY the subject line.
            """,
        ),
        (
            "human",
            """
Email Context:

{text}
            """,
        ),
    ]
)