import streamlit as st
import requests

QUERY_API_URL = "http://localhost:8000/nl-query-hf"

st.title("HealthDAX AI Analytics")

query = st.text_input("Ask a question to healthcare analytics AI")

if st.button("Run query"):
    response = requests.post(QUERY_API_URL, json={"query":query})

    data = response.json()

    if data['success']:
        st.subheader("Result")
        st.json(data['data'])

        st.subheader('Structured Query')
        st.json(data['structured_query'])

        st.write(f"Execution Time : {data['execution_time']} in ms")
    else:
        st.error(data['error'])