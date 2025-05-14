import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.tools.youtube_tools import YouTubeTools
from dotenv import load_dotenv

load_dotenv()

groq_model = Groq(id="meta-llama/llama-4-scout-17b-16e-instruct")

duckduckgo_agent = Agent(
    model=groq_model, 
    name="Web Search Agent", 
    role="Search for the information", 
    tools=[DuckDuckGo()], 
    instructions=["Always include the source of the information you find."], 
    show_tool_calls=True
)

googlesearch_agent = Agent(
    model=groq_model,
    tools=[GoogleSearch()],
    description="You are a news agent that helps users find the latest news.",
    instructions=["Always include the source of the information you find."],
    show_tool_calls=True,
)

youtube_agent = Agent(
    model=groq_model,
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

st.title("🔎 Search Agent App")
st.markdown("Ask a question below and get **accurate results** with **sources**, powered by smart search agents. 🌐📽️")

st.divider()

st.sidebar.title("⚙️ Search Settings")
st.sidebar.info("💡 Select the preferred search engine.\n\nYou can search the web, get the latest news, or summarize a YouTube video.")

options = st.sidebar.radio(
    "🔍 Choose your search method:",
    options=["DuckDuckGo", "Google Search", "Youtube Video Summary"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.success("✅ Tip: Use specific keywords for better results!")

question = st.text_area(
    label="🧠 Ask your question:", 
    placeholder="Type here..."
)

if st.button("🚀 Search Now"):
    if question:
        with st.spinner(f"Searching with **{options}**..."):
            if options == "DuckDuckGo":
                response = duckduckgo_agent.run(question)
                st.subheader("🌍 DuckDuckGo Search Results")
                st.markdown(response.content)
                
                with st.expander("🔎 See detailed tool usage"):
                    if hasattr(response, 'tool_calls') and response.tool_calls:
                        for i, tool_call in enumerate(response.tool_calls):
                            st.write(f"🛠️ Tool Call {i+1}: {tool_call['name']}")
                            st.json(tool_call['args'])
                            if 'response' in tool_call:
                                st.write("📩 Response:")
                                st.text(tool_call['response'])

            elif options == "Google Search":
                response = googlesearch_agent.run(question)
                st.subheader("📰 Google Search Results")
                st.markdown(response.content)
                
                with st.expander("🔎 See detailed tool usage"):
                    if hasattr(response, 'tool_calls') and response.tool_calls:
                        for i, tool_call in enumerate(response.tool_calls):
                            st.write(f"🛠️ Tool Call {i+1}: {tool_call['name']}")
                            st.json(tool_call['args'])
                            if 'response' in tool_call:
                                st.write("📩 Response:")
                                st.text(tool_call['response'])

            else:
                response = youtube_agent.run(question)
                st.subheader("📺 YouTube Summary Results")
                st.markdown(response.content)

                with st.expander("🔎 See detailed tool usage"):
                    if hasattr(response, 'tool_calls') and response.tool_calls:
                        for i, tool_call in enumerate(response.tool_calls):
                            st.write(f"🛠️ Tool Call {i+1}: {tool_call['name']}")
                            st.json(tool_call['args'])
                            if 'response' in tool_call:
                                st.write("📩 Response:")
                                st.text(tool_call['response'])
    else:
        st.error("⚠️ Please enter a question before clicking search.")
