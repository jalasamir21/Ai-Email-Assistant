"""
config.py
---------

Centralized configuration for the AI Email Writer project.

Responsibilities:
- Load environment variables
- Validate required API keys
- Store configurable constants
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


def get_env_variable(name: str) -> str:
    """
    Retrieve an environment variable and raise an error if it's missing.

    Args:
        name: Name of the environment variable.

    Returns:
        The value of the environment variable.

    Raises:
        ValueError: If the variable is not found.
    """
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing environment variable: '{name}'. "
            "Please add it to your .env file."
        )

    return value


# ============================
# API Keys
# ============================

GROQ_API_KEY = get_env_variable("GROQ_API_KEY")


# ============================
# LLM Configuration
# ============================

DEFAULT_MODEL = "llama-3.3-70b-versatile"
DEFAULT_TEMPERATURE = 0.4


# ============================
# Email Generation Options
# ============================

VALID_TONES = [
    "Professional",
    "Friendly",
    "Formal",
    "Persuasive",
    "Apologetic",
    "Thank You",
    "Follow-up",
]

VALID_LENGTHS = [
    "Short",
    "Medium",
    "Long",
]