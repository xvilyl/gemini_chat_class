#main.py
import streamlit as st
import google.generativeai as genai
from MethodClass import MethodClass as mc
from ConstantClass import ConstantClass as cc

def main():
    st.title("Chat - Gemini Bot")
    
    # Set Google API key
    # method to configure API key retrieved from class
    # Code here
    mc.set_key()

    # Create the Model
    # Code here
    model = mc.create_model()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role":"assistant",
                "content":"Ask me Anything!"
            }
        ]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    query = st.chat_input("What is up?")

    # Calling the Function when Input is Provided
    if query:
        # Displaying the User Message
        with st.chat_message("user"):
            st.markdown(query)

        # method to process and store Query and Response retrieved from class
        # Code here
        mc.llm_function(query,model)
        
if __name__ == "__main__":
    main()