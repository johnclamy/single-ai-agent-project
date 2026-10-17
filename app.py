# Primary Streamlit UI application (Root entrypoint)
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()


# Load environment variables
load_environment()

# Page configuration
st.set_page_config(page_title="Minimal LangChain Agent", page_icon="🤖")
st.title("🤖 Minimal LangChain Agent")
st.caption("Powered by Gemini & Tavily Search")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


@st.cache_resource
def get_agent():
    """Initialize and cache the agent to prevent reloading on every interaction."""
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


# Chat input logic
if prompt := st.chat_input("What would you like to research today?"):
    # Add user message to state and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking and searching..."):
            agent = get_agent()
            response = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
            output = response["messages"][-1].content

        st.markdown(output)

    # Add assistant message to state
    st.session_state.messages.append({"role": "assistant", "content": output})