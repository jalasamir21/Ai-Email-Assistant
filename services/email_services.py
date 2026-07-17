"""
services/email_service.py
-------------------------

Business logic layer for the AI Email Writer.
"""

from chains.email_chain import email_chain
from chains.rewrite_chain import rewrite_chain
from chains.grammar_chain import grammar_chain
from chains.subject_chain import subject_chain

from utils.validators import (
    validate_generate_email,
    validate_rewrite,
    validate_grammar,
    validate_subject,
)


class EmailService:

    @staticmethod
    def generate_email(
        purpose: str,
        recipient: str,
        context: str,
        tone: str,
        length: str,
    ) -> str:
        """
        Generate a complete email.
        """

        validate_generate_email(
            purpose,
            recipient,
            context,
            tone,
            length,
        )

        try:
            return email_chain.invoke(
                {
                    "purpose": purpose,
                    "recipient": recipient,
                    "context": context,
                    "tone": tone,
                    "length": length,
                }
            )

        except Exception as e:
            raise RuntimeError(
                f"Email generation failed: {e}"
            )

    @staticmethod
    def rewrite_email(
        email: str,
        instruction: str,
    ) -> str:
        """
        Rewrite an existing email.
        """

        validate_rewrite(email, instruction)

        try:
            return rewrite_chain.invoke(
                {
                    "email": email,
                    "instruction": instruction,
                }
            )

        except Exception as e:
            raise RuntimeError(
                f"Email rewriting failed: {e}"
            )

    @staticmethod
    def correct_grammar(
        text: str,
    ) -> str:
        """
        Correct grammar in an email.
        """

        validate_grammar(text)

        try:
            return grammar_chain.invoke(
                {
                    "text": text,
                }
            )

        except Exception as e:
            raise RuntimeError(
                f"Grammar correction failed: {e}"
            )

    @staticmethod
    def generate_subject(
        text: str,
    ) -> str:
        """
        Generate an email subject.
        """

        validate_subject(text)

        try:
            return subject_chain.invoke(
                {
                    "text": text,
                }
            )

        except Exception as e:
            raise RuntimeError(
                f"Subject generation failed: {e}"
            )