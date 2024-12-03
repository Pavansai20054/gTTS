import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
import easyocr
from PIL import Image
import numpy as np
import PyPDF2
from docx import Document
import chardet

st.title("Xara! Text-To-Speech Project by Tech T-Rex")
st.write("### Welcome to Xara! Text-To-Speech Bot")

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
        # Read and decode the text file using chardet
        raw_data = uploaded_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        mytext = raw_data.decode(encoding)
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

# Add a variable to store the translated text
translated_text = ""

col1, col2 = st.columns(2)

with col1:
    if st.button("Translate and speak"):
        if not user_input_text:
            st.warning("Please enter text to translate.")
        elif indian_language_choice == "None" and international_language_choice == "None":
            st.warning("Please select a language to translate.")
        else:
            try:
                # Ensure the text is not empty
                if not user_input_text.strip():
                    st.warning("The text is empty. Please upload a valid file or provide text.")
                else:
                    # Choose the correct language code
                    chosen_language = indian_languages.get(indian_language_choice) or international_languages.get(international_language_choice)
                    
                    if not chosen_language:
                        st.warning("Language selection is invalid.")
                    else:
                        # Split the text into chunks of less than 5000 characters
                        chunk_size = 5000
                        chunks = []
                        start = 0

                        # Split text carefully to avoid cutting in the middle of a word
                        while start < len(user_input_text):
                            end = min(start + chunk_size, len(user_input_text))
                            if end < len(user_input_text) and user_input_text[end] != ' ':
                                end = user_input_text.rfind(' ', start, end)
                            chunks.append(user_input_text[start:end].strip())
                            start = end

                        # Log the chunk sizes to verify they are under the limit
                        st.write(f"Total chunks: {len(chunks)}")
                        for i, chunk in enumerate(chunks):
                            st.write(f"Chunk {i+1} size: {len(chunk)} characters")
                        
                        # Loop through each chunk and convert to speech
                        for chunk in chunks:
                            if chunk.strip():  # Ensure there's text to process
                                try:
                                    # Translate the text
                                    translated_chunk = GoogleTranslator(source='auto', target=chosen_language).translate(chunk)
                                    translated_text += translated_chunk + " "  # Append each chunk to the translated text

                                    # Convert the translated text to speech
                                    output = gTTS(text=translated_chunk, lang=chosen_language, slow=False)
                                    output_file = "translated_output.mp3"
                                    output.save(output_file)

                                    st.audio(output_file)  # Play the audio

                                except Exception as e:
                                    st.error(f"An error occurred during translation or speech generation: {e}")
            except Exception as e:
                st.error(f"An error occurred during translation: {e}")

        # Display the translated text in a text box after translation
        st.text_area("Translated Text:", translated_text, height=200)

with col2:
    if st.button("Code!"):
        github_url = "https://github.com/Pavansai20054/gTTS/blob/main/pages/2_Text-To-Speech.py"

st.markdown("""
    <footer style="text-align: center; padding: 10px;">
        <p>Copyright (c) 2024 Pavansai. All rights reserved.</p>
        <p>Licensed under the MIT License. See LICENSE file for details.</p>
    </footer>
    """, unsafe_allow_html=True)
