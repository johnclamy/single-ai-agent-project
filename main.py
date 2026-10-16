# Secondary CLI entrypoint for testing (Root entrypoint)import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor, create_react_agent


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()
