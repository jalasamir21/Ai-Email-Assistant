
from config import VALID_LENGTHS, VALID_TONES
from services.email_services import EmailService

import streamlit as st
from pathlib import Path


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Email Writer",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.markdown("""
<div class="sidebar-logo">
AI EMAIL<br>WRITER
</div>
""", unsafe_allow_html=True)

st.sidebar.divider()

# st.sidebar.markdown("### MENU")

css = Path("assets/style.css").read_text()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True,
)
st.markdown("""
<div class="hero-title">

THE AI EMAIL WRITER

</div>

<div class="hero-line"></div>

""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">

Every great email starts with context.

Generate, rewrite, proofread and improve professional emails.

</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Tabs
# -------------------------------------------------

page = st.sidebar.radio(
    "MENU",
    [
        "Generate Email",
        "Rewrite Email",
        "Grammar Check",
        "Subject Generator",
    ],
)


# =================================================
# Generate Email
# =================================================

if page == "Generate Email":

    st.markdown(
        '<div class="section-title">GENERATE EMAIL</div>',
        unsafe_allow_html=True,
    )
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

    left, right = st.columns([1, 1])
    with left:
        tone = st.selectbox(
            "Tone",
            VALID_TONES,
        )

    with right:
        length = st.selectbox(
            "Length",
            VALID_LENGTHS,
        )

    if st.button(
        "Generate Email",
        use_container_width=True,
    ):

        try:

            with st.spinner("Generating email..."):
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
                "",
                value = response,
                height=450,
            )

        except Exception as e:
            st.error(str(e))


# =================================================
# Rewrite
# =================================================

if page == "Rewrite Email":

    st.markdown(
    '<div class="section-title">REWRITE EMAIL</div>',
    unsafe_allow_html=True,
)

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
                "",
                value = response,
                height=450,
            )

        except Exception as e:
            st.error(str(e))


# =================================================
# Grammar
# =================================================

if page == "Grammar Check":

    st.markdown(
        '<div class="section-title">GRAMMAR CHECK</div>',
        unsafe_allow_html=True,
    )

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
                "",
                value = response,
                height=450,
            )

        except Exception as e:
            st.error(str(e))


# =================================================
# Subject Generator
# =================================================

if page == "Subject Generator":

    st.markdown(
        '<div class="section-title">SUBJECT GENERATOR</div>',
        unsafe_allow_html=True,
    )

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
                "",
                value = response,
                height=100,
            )

        except Exception as e:
            st.error(str(e))

st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:60px;
        color:#5e84ff;
        font-family:'IBM Plex Mono';
        font-size:13px;
    ">
    © 2026 AI EMAIL WRITER · POWERED BY GROQ + LANGCHAIN + STREAMLIT
    </div>
    """,
    unsafe_allow_html=True,
)
