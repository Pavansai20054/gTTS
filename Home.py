import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Pavansai's Project Portfolio", layout="wide")

# Main content
st.title("Welcome to Pavansai's Project Portfolio")
st.write("Explore various projects showcasing skills in Python, Machine Learning, and more.")
st.write("Use the sidebar to navigate between projects.")

# Footer
st.markdown("""
<footer style="text-align: center; padding: 10px;">
    <p>Copyright (c) 2024 Pavansai. All rights reserved.</p>
    <p>Licensed under the MIT License. See LICENSE file for details.</p>
</footer>
""", unsafe_allow_html=True)
