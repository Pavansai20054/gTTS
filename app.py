import streamlit as st
import os
from gtts import gTTS

# Set up the page layout
st.set_page_config(page_title="Pavansai's Project Portfolio", layout="wide")

# Sidebar with project buttons
st.sidebar.title("Projects")
project_choice = st.sidebar.selectbox(
    "Choose a project", 
    ["Home", "Project 1", "Project 2", "Project 3", "Project 4", "Project 5"]
)

# Display content based on the selected project
if project_choice == "Home":
    st.title("Welcome to Pavansai's Project Portfolio!")
    st.write("Select a project from the sidebar to get started.")
    
elif project_choice == "Project 1":
    st.write("### Project 1 Page")
    st.write("This project uses text-to-speech to create a chatbot voice.")
    
    # File uploader for text input
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    
    # Initialize the text variable with default text
    default_text = """Hello Everyone!
I am Pavan's chatbot.
My name is T-Rex."""
    
    # Set mytext to default text
    mytext = default_text

    # If a file is uploaded, read its content
    if uploaded_file is not None:
        # Read the file contents
        mytext = uploaded_file.read().decode("utf-8")
        st.success("File uploaded successfully!")

    # Button to show the code
    if st.button("Code!"):
        code = """# Importing required modules
from gtts import gTTS
import os

# Initialize the text
mytext = "Hello Everyone! I am Pavan's chatbot. My name is T-Rex."

language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)

# Save the file
output.save("output.mp3")

# Play the file 
os.system("start output.mp3")"""
        st.code(code, language='python')

    # Perform text-to-speech with the text
    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)

    # Save the audio file
    output_file = "output.mp3"
    output.save(output_file)

    # Play the audio file
    st.audio(output_file)  # Streamlit method to play audio

elif project_choice == "Project 2":
    st.write("### Project 2 Page")
    # Add details or navigation here for Project 2
elif project_choice == "Project 3":
    st.write("### Project 3 Page")
    # Add details or navigation here for Project 3
elif project_choice == "Project 4":
    st.write("### Project 4 Page")
    # Add details or navigation here for Project 4
elif project_choice == "Project 5":
    st.write("### Project 5 Page")
    # Add details or navigation here for Project 5
else:
    st.write("### Select a project from the sidebar to view its page.")
