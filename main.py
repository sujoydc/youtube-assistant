import my_langchain_helper as helper 
import streamlit as st 

st.title("Company Name Generator!")

company_type = st.sidebar.selectbox("What is your company type?", 
                                    ("AI", "Finance", "BioTech"))

response_number = st.sidebar.text_area(label="How many names to generate?",
                                       max_chars=1)

max_char = st.sidebar.text_area(label="How many maximum charater per name?",
                                       max_chars=1)

# gen_button = st.sidebar.button(label="Generate", 
#                                 on_click=generate)


if max_char:
    response = helper.generate_company_name(company_type=company_type,
                                 response_number=response_number,
                                 max_char=max_char)
    st.text(response['company_name'])
    