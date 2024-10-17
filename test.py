import streamlit as st
import pandas as pd
import numpy as np

# Function to recommend songs based on user input
def recommend_songs(user_input):
    # Mock recommendation logic
    # In a real application, this could connect to an API or database
    recommendations = [f"{user_input} Song {i+1}" for i in range(5)]
    return recommendations

# Function to generate random data for demonstration
def generate_random_data(num_points):
    data = pd.DataFrame(
        np.random.randn(num_points, 3),
        columns=["A", "B", "C"]
    )
    return data

# Streamlit app title
st.title("Music Recommendation Chatbot")

# User input for song recommendation
user_input = st.text_input("Enter a music genre or artist for recommendations:")

# Button to trigger song recommendation
if st.button("Get Recommendations"):
    if user_input:
        recommendations = recommend_songs(user_input)
        st.write("Recommended Songs:")
        st.write(", ".join(recommendations))
    else:
        st.write("Please enter a genre or artist.")

# Slider to choose the number of random data points to generate
num_points = st.slider("Select number of random data points:", 1, 100, 10)

# Button to generate random data
if st.button("Generate Data"):
    random_data = generate_random_data(num_points)
    st.write("Generated Random Data:")
    st.dataframe(random_data)

# Display a line chart of random data
if st.button("Show Chart"):
    random_data = generate_random_data(num_points)
    st.line_chart(random_data)
