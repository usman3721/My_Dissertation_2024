
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv() 
from datetime import datetime, timedelta
import json
import os
from streamlit_chat import message
import google.generativeai as genai
from PIL import Image
import base64
from io import BytesIO

print(genai.configure(api_key=os.getenv("GOOGLE_API_KEY")))
# print(genai.configure(api_key=st.secrets.GOOGLE_API_KEY))

model = genai.GenerativeModel("gemini-1.5-flash-latest")
chat = model.start_chat(history=[])


# Initialize session state variables if they don't exist
import streamlit as st
from datetime import datetime, timedelta

# Initialize session state variables if they don't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []



if "messages" not in st.session_state:
    st.session_state["messages"] = []

if 'level' not in st.session_state:
    st.session_state['level'] = 'Beginner'

# Add initial assistant message if chat history is empty
if not st.session_state["messages"]:
    st.session_state["messages"].append({"role": "assistant", "content": "Ask Me Anything About Electrical and Electronics Engineering"})

def get_electrical_response(question, level):
    level_instructions = {
        "Beginner": "Explain in simple terms with basic details.",
        "Intermediate": "Provide more detailed explanations with some technical terms.",
        "Professional": "Include advanced technical details and professional jargon."
    }

    prompt = (
        f"You are an AI Assistant specializing in answering all electrical and electronics engineering questions. "
        f"You are used by professionals in the field and laymen. Be explicit, informative, and explain technical concepts in a clear manner. "
        f"If any question apart from electrical and electronics engineering is asked, kindly say 'I'm sorry, I answer electrical and electronics engineering related questions only.' "
        f"Always provide references. "
        f"{level_instructions[level]}"
    )

    response = chat.send_message(prompt + question, stream=True)
    return response


import re
import requests

def extract_urls(text):
    # Regular expression to find URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return url_pattern.findall(text)

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        # Consider a URL valid if the status code is less than 400
        return response.status_code < 400
    except requests.RequestException:
        return False

def validate_and_update_references(response_text):
    urls = extract_urls(response_text)
    valid_urls = {url: check_url(url) for url in urls}
    
    updated_response = response_text
    
    for url, is_valid in valid_urls.items():
        if not is_valid:
            updated_response = updated_response.replace(url, "[Invalid URL]")

    return updated_response

def format_timestamp(timestamp):
    now = datetime.now()
    if timestamp.date() == now.date():
        return "today"
    elif timestamp.date() == (now - timedelta(days=1)).date():
        return "yesterday"
    else:
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def format_response(response):
    response_text = "".join(chunk.text for chunk in response)
  # Split lines and handle empty or single-line responses gracefully
    
    return response_text

def image_to_base64(image_path):
        img = Image.open(image_path)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return img_str

def main():
    # st.set_page_config(layout="wide")
    c1, c2, c3 = st.columns([1, 2, 1])
    pth = "Images/pic1.jpg"
    c1.image(pth, width=200)
    c2.title("Electrical & Electronics Engineering Chatbot")

    # Custom CSS for sidebar
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #d3f5ea;
        }
        .sidebar .sidebar-content a {
            display: block;
            padding: 10px 0;
            color: #000000;
            text-decoration: none;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    level = st.sidebar.selectbox('Select Level:', ['Beginner', 'Intermediate', 'Professional'], key='level')


    # Sidebar for chat history and dropdowns
    st.sidebar.title("Chat History")
    for entry in st.session_state['chat_history']:
        role, content, timestamp = entry
        if role == "You":
            st.sidebar.write(f"{content} ({format_timestamp(timestamp)})")
    # st.sidebar.title("Chat History")
    # for i, entry in enumerate(st.session_state['chat_history']):
    #     role, content, timestamp = entry
    #     if role == "You":
    #         st.sidebar.markdown(f"[{content}](#{i}) ({format_timestamp(timestamp)})")
    #     else:
    #         st.sidebar.markdown(f"[{content}](#{i}) ({format_timestamp(timestamp)})")


    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    chat_container = st.container()
    input_container = st.container()



    if prompt := st.chat_input():
        with input_container:
            if prompt:
                response = get_electrical_response(prompt,st.session_state['level'])
                response_text =format_response(response)

                # response_text = "".join(chunk.text for chunk in response)

                timestamp = datetime.now()
                st.session_state['chat_history'].append(("You", prompt, timestamp))
                st.session_state['chat_history'].append(("Bot", response_text, timestamp))

                st.session_state["messages"].append({"role": "user", "content": prompt})
                st.session_state["messages"].append({"role": "assistant", "content": response_text})

                st.experimental_rerun()

    user_avatar_style = "identicon"
    user_seed = "12345"

    bot_logo_base64 = image_to_base64("Images\pic1.jpg")
    bot_logo_html1 = f"data:image/png;base64,{bot_logo_base64}"





    with chat_container:
        if st.session_state.messages:
            for i, msg in enumerate(st.session_state.messages):
                if isinstance(msg, dict) and msg.get("role") == "user" and "content" in msg:
                    message(msg["content"], is_user=True, key=f"user_{i}",avatar_style=user_avatar_style,seed=user_seed)
                
                elif isinstance(msg, dict) and msg.get("role") == "assistant" and "content" in msg:
                    # Custom HTML for displaying the company logo
                    st.markdown(f"""
                    <div id='{i}' style='text-align: left; color: black; background-color: #f4f4f4; padding: 10px; border-radius: 10px; margin: 10px 0;'>
                        <img src='{bot_logo_html1}' alt='Bot Avatar' style='width: 50px; height: 50px; border-radius: 50%; display: inline-block; vertical-align: middle; margin-right: 10px;' /
                        <span style='vertical-align: middle;'>{msg['content']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                elif not isinstance(msg, dict) or "role" not in msg or "content" not in msg:
                    st.error("Invalid message format")
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Ask Me Anything About ELE"}]
    st.session_state['chat_history'] = []
    # st.experimental_rerun()

if __name__ == "__main__":
    main()










