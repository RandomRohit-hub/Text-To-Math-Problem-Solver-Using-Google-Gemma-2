import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Streamlit App Setup
st.set_page_config(page_title="Text to Math Solver & Knowledge Assistant", page_icon="🧮")
st.title("🧮 Math & Knowledge Assistant using Google Gemma 2")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in environment. Please check your .env file.")
    st.stop()

# Initialize the LLM with Groq API
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=GROQ_API_KEY)

# Define tools
wikipedia_tool = Tool(
    name="Wikipedia",
    func=WikipediaAPIWrapper().run,
    description="Search for general knowledge topics using Wikipedia."
)

math_tool = Tool(
    name="Calculator",
    func=LLMMathChain.from_llm(llm=llm).run,
    description="Solve mathematical expressions and arithmetic problems."
)

reasoning_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are an intelligent agent that solves math and logic problems. 
Provide a clear, step-by-step explanation in bullet points.

Question: {question}
Answer:
"""
)

reasoning_chain = LLMChain(llm=llm, prompt=reasoning_prompt)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func=reasoning_chain.run,
    description="Solve logic-based and reasoning questions with detailed steps."
)

# Initialize the agent with tools
agent = initialize_agent(
    tools=[wikipedia_tool, math_tool, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm your math and knowledge assistant. Ask me anything!"}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input area
user_input = st.text_area(
    "Enter your question:",
    value="I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?"
)

# Button to trigger response
if st.button("Find My Answer"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.chat_message("user").write(user_input)

            callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = agent.run(st.session_state.messages, callbacks=[callback])

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.success(response)
    else:
        st.warning("⚠️ Please enter a question before submitting.")
