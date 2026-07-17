# 📧 AI Email Writer

An AI-powered email writing assistant that generates, rewrites, proofreads, and improves professional emails using **Groq's Llama 3.3**, **LangChain**, and **Streamlit**.

The project is built with a modular architecture following software engineering best practices, making it easy to extend with memory, Retrieval-Augmented Generation (RAG), and AI agents.

---

## ✨ Features

### 📩 Generate Emails
Generate complete professional emails based on:

- Purpose
- Recipient
- Context
- Tone
- Length

---

### ✏ Rewrite Emails

Rewrite existing emails while preserving their meaning.

Examples:

- Make more professional
- Make more concise
- Make friendlier
- Improve readability

---

### 📝 Grammar Correction

Automatically fix:

- Grammar
- Spelling
- Punctuation
- Capitalization

without changing the intended meaning.

---

### 📌 Subject Generator

Generate concise and professional email subject lines based on the email context.

---

## 🏗 Project Structure

```text
AI_Email_Writer/
│
├── config.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
│
├── models/
│   └── llm.py
│
├── prompts/
│   ├── email_prompt.py
│   ├── rewrite_prompt.py
│   ├── grammar_prompt.py
│   └── subject_prompt.py
│
├── chains/
│   ├── email_chain.py
│   ├── rewrite_chain.py
│   ├── grammar_chain.py
│   └── subject_chain.py
│
├── services/
│   └── email_service.py
│
└── utils/
```

---

## ⚙ Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
Email Service
   │
   ▼
Validation Layer
   │
   ▼
LangChain Chains
   │
   ▼
Prompt Templates
   │
   ▼
Groq Llama 3.3
```

---

## 🛠 Tech Stack

- Python
- LangChain
- Groq
- Llama 3.3
- Streamlit
- python-dotenv

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/jalasamir21/AI-Email-Writer.git
```

Move into the project

```bash
cd AI-Email-Writer
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶ Run the Application

```bash
streamlit run streamlit_app.py
```

---

## 📂 Future Improvements

- Conversation memory
- Retrieval-Augmented Generation (RAG)
- Resume-aware email generation
- Job description personalization
- Company profile understanding
- AI reviewer for quality assurance
- Gmail API integration
- Multi-agent workflow with LangGraph

---
