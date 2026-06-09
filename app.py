import streamlit as stm
stm.title("Hello Everyone")
stm.write("Welcome to Streamlit")
if stm.button("Click Me"):
    stm.write("Button clicked!")