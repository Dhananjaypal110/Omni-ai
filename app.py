Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import os
... import streamlit as st
... from google import genai
... 
... # Set page styling
... st.set_page_config(page_title="My AI Web App", page_icon="🤖")
... st.title("🤖 My AI Assistant")
... 
... # Initialize Gemini Client (Reads key automatically from Vercel/Streamlit secrets)
... client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
... 
... # Initialize chat memory
... if "messages" not in st.session_state:
...     st.session_state.messages = []
... 
... # Display previous conversation messages
... for message in st.session_state.messages:
...     with st.chat_message(message["role"]):
...         st.markdown(message["content"])
... 
... # User Input Box
... if prompt := st.chat_input("Ask me anything..."):
...     # Display user input
...     st.session_state.messages.append({"role": "user", "content": prompt})
...     with st.chat_message("user"):
...         st.markdown(prompt)
... 
...     # Generate and display AI response
...     with st.chat_message("assistant"):
...         response = client.models.generate_content(
...             model="gemini-2.5-flash",
...             contents=prompt,
...         )
...         st.markdown(response.text)
