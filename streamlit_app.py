"""
streamlit_app.py
----------------

Streamlit interface for the AI Email Writer.
"""

import streamlit as st

from config import VALID_LENGTHS, VALID_TONES
from services.email_services import EmailService


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Email Writer",
    page_icon="📧",
    layout="wide",
)

st.title("📧 AI Email Writer")
st.write(
    "Generate, rewrite, proofread, and improve professional emails using AI."
)


# -------------------------------------------------
# Tabs
# -------------------------------------------------

generate_tab, rewrite_tab, grammar_tab, subject_tab = st.tabs(
    [
        "✍️ Generate",
        "🔄 Rewrite",
        "📝 Grammar",
        "📌 Subject",
    ]
)


# =================================================
# Generate Email
# =================================================

with generate_tab:

    st.header("Generate an Email")

    purpose = st.text_input(
        "Purpose",
        placeholder="e.g. Apply for an AI internship",
    )

    recipient = st.text_input(
        "Recipient",
        placeholder="e.g. Hiring Manager",
    )

    context = st.text_area(
        "Context",
        height=180,
        placeholder="Provide the important details...",
    )

    col1, col2 = st.columns(2)

    with col1:
        tone = st.selectbox(
            "Tone",
            VALID_TONES,
        )

    with col2:
        length = st.selectbox(
            "Length",
            VALID_LENGTHS,
        )

    if st.button(
        "Generate Email",
        use_container_width=True,
    ):

        try:

            response = EmailService.generate_email(
                purpose,
                recipient,
                context,
                tone,
                length,
            )

            st.success("Email generated successfully!")

            st.subheader("Generated Email")

            st.text_area(
                "Output",
                response,
                height=350,
            )

        except Exception as e:
            st.error(str(e))


# =================================================
# Rewrite
# =================================================

with rewrite_tab:

    st.header("Rewrite an Email")

    email = st.text_area(
        "Original Email",
        height=250,
    )

    instruction = st.text_input(
        "Rewrite Instructions",
        placeholder="e.g. Make it more formal",
    )

    if st.button(
        "Rewrite Email",
        use_container_width=True,
    ):

        try:

            response = EmailService.rewrite_email(
                email,
                instruction,
            )

            st.success("Email rewritten successfully!")

            st.subheader("Generated Email")

            st.text_area(
                "Output",
                response,
                height=350,
            )

        except Exception as e:
            st.error(str(e))


# =================================================
# Grammar
# =================================================

with grammar_tab:

    st.header("Grammar Correction")

    text = st.text_area(
        "Paste your email",
        height=250,
    )

    if st.button(
        "Correct Grammar",
        use_container_width=True,
    ):

        try:

            response = EmailService.correct_grammar(text)

            st.success("Grammar corrected!")

            st.subheader("Generated Email")

            st.text_area(
                "Output",
                response,
                height=350,
            )

        except Exception as e:
            st.error(str(e))


# =================================================
# Subject Generator
# =================================================

with subject_tab:

    st.header("Generate Subject")

    subject_context = st.text_area(
        "Email Context",
        height=200,
    )

    if st.button(
        "Generate Subject",
        use_container_width=True,
    ):

        try:

            response = EmailService.generate_subject(
                subject_context,
            )

            st.success("Subject generated!")

            st.subheader("Generated Subject")

            st.text_area(
                "Output",
                response,
                height=100,
            )

        except Exception as e:
            st.error(str(e))