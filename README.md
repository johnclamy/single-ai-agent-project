# Minimal LangChain Agent Demo

A lightweight, modern LangChain-based agent project designed for experimentation, learning, and rapid prototyping. It features a dual-interface setup (CLI and Streamlit UI) powered by Google's Gemini and Tavily Search, managed entirely with the modern `uv` Python package manager.

## ✨ Features

- 🚀 **Modern LangChain Architecture**: Uses the latest `create_agent` API (LangGraph-based) with native message history handling, replacing legacy `AgentExecutor` patterns.
- 🔍 **Real-Time Web Search**: Integrated `TavilySearch` tool for accurate, up-to-date information retrieval.
- 💻 **Dual Interface**: 
  - Interactive web UI via **Streamlit** (`app.py`).
  - Clean terminal-based CLI for quick testing (`main.py`).
- 📓 **Research Notebook**: Includes a Jupyter notebook (`src/single_ai_agent_sys/single_ai_agent.ipynb`) for iterative testing, debugging, and development notes.
- ⚡ **Modern Python Workflow**: Built from the ground up with **`uv`** for blazing-fast dependency resolution, virtual environment management, and reproducible builds.

## 🛠️ Tech Stack

- **Python**: `>=3.10`
- **Package Manager**: `uv`
- **LLM**: Google Gemini (`gemini-3.8-flash`) via `langchain-google-genai`
- **Tools**: Tavily Search via `langchain_tavily`
- **Frameworks**: `langchain`, `langchain-core`, `streamlit`
- **Environment**: `python-dotenv`

## 📋 Prerequisites

1. Install `uv` (if you haven't already):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
