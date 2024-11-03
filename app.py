import streamlit as st
from gtts import gTTS
from googletrans import Translator
import easyocr
import os
from PIL import Image
import numpy as np
import PyPDF2
from docx import Document

# Set up the page layout
st.set_page_config(page_title="Pavansai's Project Portfolio", layout="wide")

# Sidebar with project buttons
st.sidebar.title("Projects")
project_choice = st.sidebar.selectbox(
    "Choose a project", 
    ["Home", "Text-To-Speech", "Project 2", "Project 3", "Project 4", "Project 5"]
)

# Display content based on the selected project
if project_choice == "Home":
    st.title("Welcome to Pavansai's Project Portfolio!")
    st.write("Select a project from the sidebar which will be appeared by clicking on arrow beside to get started.")
    
elif project_choice == "Text-To-Speech":
    st.write("### Welcome to Xara! Text-To-Speech bot")
    st.write("This project uses text-to-speech to create a chatbot voice.")

    # Define the language options
    indian_languages = {
        "Bengali": 'bn',
        "Gujarati": 'gu',
        "Hindi": 'hi',
        "Kannada": 'kn',
        "Malayalam": 'ml',
        "Marathi": 'mr',
        "Punjabi": 'pa',
        "Tamil": 'ta',
        "Telugu": 'te',
        "Urdu": 'ur',
        "Nepali": 'ne',  
    }

    international_languages = {
        "Arabic": 'ar',
        "Chinese": 'zh-cn',
        "Dutch": 'nl',
        "English": 'en',
        "French": 'fr',
        "German": 'de',
        "Italian": 'it',
        "Japanese": 'ja',
        "Korean": 'ko',
        "Portuguese": 'pt',
        "Russian": 'ru',
        "Spanish": 'es',
        "Swedish": 'sv',
        "Turkish": 'tr',
        "Thai": 'th',  
        "Vietnamese": 'vi',  
        "Persian": 'fa',  
        "Swahili": 'sw',  
        "Filipino": 'tl',  
        "Finnish": 'fi',  
        "Hungarian": 'hu',  
        "Hebrew": 'iw',  
        "Malay": 'ms',  
        "Ukrainian": 'uk'  
    }

    # Dropdowns for Indian and International languages
    st.write("#### Select Language")
    indian_language_choice = st.selectbox("Choose an Indian Language", ["None"] + list(indian_languages.keys()))
    international_language_choice = st.selectbox("Choose an International Language", ["None"] + list(international_languages.keys()))

    # Logic to handle selection
    if indian_language_choice != "None":
        international_language_choice = "None"  # Reset international selection
        st.warning("You have selected an Indian language. The international language selection has been reset.")
        
    elif international_language_choice != "None":
        indian_language_choice = "None"  # Reset Indian selection
        st.warning("You have selected an International language. The Indian language selection has been reset.")

    # File uploader for text input
    uploaded_file = st.file_uploader("Upload a text file, PDF, Word document, or image", type=["txt", "pdf", "docx", "jpg", "jpeg", "png"])

    # Variable to store the text to be read
    mytext = ""

    if uploaded_file is not None:
        # Handling different file types
        if uploaded_file.type == "text/plain":
            mytext = uploaded_file.read().decode("utf-8")
            st.success("Text file uploaded successfully!")
        
        elif uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            mytext = ""
            for page in pdf_reader.pages:
                mytext += page.extract_text() + "\n"
            st.success("PDF file uploaded successfully!")

        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            mytext = "\n".join([para.text for para in doc.paragraphs])
            st.success("Word document uploaded successfully!")

        elif uploaded_file.type in ["image/jpeg", "image/png"]:
            # Open the image file with PIL
            image = Image.open(uploaded_file)

            # Convert the image to a NumPy array
            image_np = np.array(image)

            # Initialize EasyOCR reader
            reader = easyocr.Reader(['en'])  # Specify the language
            result = reader.readtext(image_np)

            # Extract and concatenate text from image
            mytext = " ".join([text[1] for text in result])
            st.success("Image file uploaded successfully!")

        # Display the text to be translated
        st.write("### Extracted Text:")
        st.write(mytext)

    # Text area for display and editing
    user_input_text = st.text_area("Text to be read aloud:", mytext, height=100)

    # Buttons for Translate and Code
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Translate"):
            if not user_input_text:
                st.warning("Please enter text to translate.")
            elif indian_language_choice == "None" and international_language_choice == "None":
                st.warning("Please select a language to translate.")
            else:
                try:
                    translator = Translator()
                    chosen_language = indian_languages.get(indian_language_choice) or international_languages.get(international_language_choice)
                    translated_text = translator.translate(user_input_text, dest=chosen_language).text
                    
                    st.write("### Translated Text:")
                    st.write(translated_text)
                    
                    st.success(f"Text translated to {indian_language_choice or international_language_choice}!")

                    output = gTTS(text=translated_text, lang=chosen_language, slow=False)
                    output_file = "translated_output.mp3"
                    output.save(output_file)

                    st.audio(output_file)  # Play the audio
                except Exception as e:
                    st.error(f"An error occurred during translation: {e}")

    with col2:
        if st.button("Code!"):
            github_url = "https://github.com/Pavansai20054/gTTS/blob/main/app.py"
            st.markdown(f"[Here you will get the code.]({github_url})", unsafe_allow_html=True)

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
