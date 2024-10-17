import streamlit as st

# Set the app title
st.title("My first streamlit app")

# streamlit run [filename].py

# text input
st.write("Welcome to my first streamlit app")
st.write("This is a text input")
st.write(st.text_input("Enter your name"))

# display a button
st.button("Reset", type="primary")
if st.button("Say Hello"): # if you click the button
  st.write("Hello")
else:
  st.write("Bye")
