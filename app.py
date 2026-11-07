import streamlit as st

st.set_page_config(page_title="Binary Lab", page_icon="🔢")
st.title("Binary Lab")
st.caption("Binary / Decimal converter")

st.subheader("Decimal to Binary")
value = st.number_input("Enter a decimal number", min_value=0, step=1, value=42)
st.code(format(value, "b"))

st.subheader("Binary to Decimal")
binary_text = st.text_input("Enter binary value", value="101010")
try:
    decimal_value = int(binary_text, 2)
    st.code(f"{decimal_value}")
except ValueError:
    st.warning("Please enter a valid binary number using only 0 and 1.")

st.subheader("About")
st.write("This app is a simple binary tool for demos and testing on Streamlit Cloud.")
