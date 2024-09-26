from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import SQLDatabase

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

load_dotenv()

st.set_page_config(page_title='Chat with Mysql', page_icon=":speech_balloon:")
st.title("Chat with Mysql")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a Bot application to chat with Mysql DB. Connect to DB & start Conversation")
    
    host = st.text_input("Host", value="localhost", key='Host')
    port = st.text_input("Port", value=3306, key='Port')
    user = st.text_input("User", value="root", key='User')
    password = st.text_input("Password", type="password", value="rohan2939", key='Password')
    database = st.text_input("Database", value="practise", key='DatabaseInput')
    
    if st.button("Connect to DB"):
        with st.spinner("Connecting to the database.."):
            db = init_database(user, password, host, port, database)
            st.session_state['Database'] = db
            st.success("Connected to database!!!")

st.chat_input("Type a message")
