import my_langchain_helper as helper 
import streamlit as st 
import textwrap

st.title("YouTube Assistant!")

with st.sidebar:
    with st.form(key = "my_form"):
        youtube_url = st.sidebar.text_area(
            label="Paste the YoutTube URL",
            max_chars=80
        )
        query = st.sidebar.text_area(
            label="What is your question?",
            max_chars=100,
            key="query"
        )

        submit_button = st.form_submit_button(label="Enter")


if query and youtube_url:
    db = helper.create_vector_db_from_youtube_link(youtube_url)
    response, docs = helper.get_response_from_query(db, query)
    st.subheader("Answer: ")
    st.text(textwrap.fill(response, width=80))

