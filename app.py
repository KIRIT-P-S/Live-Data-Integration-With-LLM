import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(search=True)],
    instructions=[
        "Always provide detailed explanations.",
        "Include multiple sources with proper citations.",
        "Break down complex answers into step-by-step explanations.",
        "Use bullet points, headings, and tables for clarity.",
    ],
    show_tool_calls=True,  
    markdown=True,
    debug_mode=True, 
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Provide detailed financial analysis.",
        "Use tables to display stock prices, fundamentals, and trends.",
        "Include analyst recommendations with context.",
        "Break down financial metrics into simple terms.",
    ],
    debug_mode=True,
)


agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=[
        "Always provide in-depth answers with structured explanations.",
        "Use tables, bullet points, and headings for better readability.",
        "For finance questions, provide detailed stock fundamentals and recommendations.",
        "Always include sources with citations.",
        "Summarize key takeaways at the end of the response.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Streamlit UI
st.set_page_config(page_title="Smart Assistant", layout="wide")
st.title("🔍 Smart AI Assistant")

st.markdown("Ask your question about **finance, stocks, or general knowledge**, and get a detailed response with sources.")

user_question = st.text_area("Enter your question:")

if st.button("Ask"):
    with st.spinner("Fetching response..."):
        response = agent_team.run(user_question)

        # Display Response
        st.markdown("## 📌 Response")
        if hasattr(response, 'content'):
            st.markdown(response.content, unsafe_allow_html=True)
        else:
            st.markdown(f"**{str(response)}**")

        # Display Sources
        st.markdown("---")
        st.markdown("## 🔗 Sources")
        if hasattr(response, 'sources'):
            for source in response.sources:
                st.markdown(f"- [{source['title']}]({source['url']})")
        else:
            st.markdown("No sources available.")

st.sidebar.header("🔧 Debug Info")
st.sidebar.write("Debug mode is enabled for detailed agent responses.")
