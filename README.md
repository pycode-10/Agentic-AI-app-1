# 🤖 Agentic-AI-app

A smart multi-agent Streamlit app powered by `phi` and `Groq`.  
Easily search the web using **DuckDuckGo**, fetch the **latest news** via **Google**, or summarize **YouTube videos** — all in one place!

---

## 🚀 Features

- 🔍 **DuckDuckGo Agent** – Searches the web with source references.
- 📰 **Google Search Agent** – Finds the latest news articles.
- 📺 **YouTube Agent** – Summarizes YouTube videos and answers questions based on the video.
- 🌐 Powered by **Groq** and the `meta-llama/llama-4-scout-17b` model.
- 🧠 Built using `phi`, `Streamlit`, and multi-agent tool integration.

---

## 📦 Requirements

- Python 3.8+
- `pip` or `pipenv`
- Groq API access (via `.env`)
- Required Python libraries:
  - `streamlit`
  - `phi`
  - `python-dotenv`

---

## 🔧 Installation

### ✅ Clone the repository

```bash
git clone https://github.com/pycode-10/Agentic-AI-app-1.git
cd Agentic-AI-app-1
```

### ✅ Create and activate a virtual environment

Using `pip`:

```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```

Or use `pipenv`:

```bash
pipenv shell
```

---

### ✅ Install the dependencies

```bash
pip install -r requirements.txt
```

> Or use `pipenv install` if you're using Pipenv

---

### ✅ Set up your `.env` file

Update the `.env` file in the root folder and add your API keys. Currently, the `.env` file is empty. 


---

## 🧪 Run the app locally

```bash
streamlit run agent.py
```

> Replace `agent.py` with your actual file name if different.
