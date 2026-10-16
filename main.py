# Secondary CLI entrypoint for testing (Root entrypoint)import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()


def initialize_agent():
    """Initialize the LLM, tools, and agent."""
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0,
    )
    tools = [TavilySearch(max_results=2)]
    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are a helpful assistant. Use Tavily Search when current or "
            "up-to-date information is needed."
        ),
    )


def main():
    load_environment()
    agent_executor = initialize_agent()
    
    print("--- LangChain Agent CLI ---")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        response = agent_executor.invoke(
            {"messages": [{"role": "user", "content": user_input}]}
        )
        print(f"\nAgent: {response['messages'][-1].content}\n")


if __name__ == "__main__":
    main()