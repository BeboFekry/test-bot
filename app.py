import streamlit as st
# st.logo("images/Logo.png")

home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
chat = st.Page("chatbot.py", title="Chatbot", icon=":material/smart_toy:")
scan = st.Page("scan.py", title="Scan", icon=":material/radiology:")
ecg = st.Page("ecg.py", title="ECG Scan", icon=":material/ecg_heart:")
mbti = st.Page("mbti.py", title="MBTI", icon=":material/psychology:")

pg = st.navigation([home, chat, scan, ecg, mbti])
pg.run()
