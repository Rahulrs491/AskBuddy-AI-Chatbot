from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(model="openai/gpt-oss-120b")

st.title(" AskBuddy :: AI Qna Bot") # Here is web page title.
st.markdown("My Qna Bot using Langchain and Groq !")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # messages is a key in session storage to store


# For displaying previous meassage
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

# Get user input
query = st.chat_input("Ask anything ?")
if query:
    # Store user message
    st.session_state.messages.append({"role":"user", "content":query})
    # Display user message
    st.chat_message("user").markdown(query)
    # Get response using complete conversation history
    res = llm.invoke(st.session_state.messages)
    # Display AI response
    st.chat_message("ai").markdown(res.content)
    # Store AI response
    st.session_state.messages.append({"role":"ai", "content":res.content})



