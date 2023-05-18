import streamlit as st
import openai
from streamlit_chat import message

openai.api_key = "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"

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

def get_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        temperature=0
    )

    text = response.choices[0].text.strip()
    return text

st.title("Mental Health Chatbot")

history_display = st.empty()

user_input = st.text_input("Let us know how you're feeling today")

if st.button("Send"):
    if user_input:
        st.session_state['conversation'].append({'sender': 'user', 'text': user_input})
        bot_response = get_response(user_input)
        st.session_state['conversation'].append({'sender': 'bot', 'text': bot_response})

user = "You: "
bot = "Bot: "

def printMessage(x, is_user):
    if is_user:
        message(x, is_user=True)
    else:
        message(x)

for i, message1 in enumerate(st.session_state['conversation']):
    user = ""
    bot = ""
    if message1['sender'] == 'user':
        user = user + message1['text']
        printMessage(user, is_user=True)
    else:
        bot = bot + message1['text']
        printMessage(bot, is_user=False)
