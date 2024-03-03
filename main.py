import streamlit as st
import langchain_helper as lc
st.title("Restaurant Name generator")

cusine = st.sidebar.selectbox("Pick a Cusine", ("Indian", "Italian", "Mexican", "Arabic"))

if cusine:
    response = lc.generate_restaurent_name_and_items(cusine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items :
        st.write("-", item)

