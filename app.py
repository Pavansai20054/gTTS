import streamlit as st
from gtts import gTTS
from googletrans import Translator
import os

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

    # Language options for different accents and languages
    language_options = {
        "US English": ('en', "Hello Everyone! I am Pavan's chatbot. My name is T-Rex."),
        "UK English": ('en', "Hello Everyone! I am Pavan's chatbot. My name is T-Rex."),
        "Australian English": ('en', "Hello Everyone! I am Pavan's chatbot. My name is T-Rex."),
        "Indian English": ('en', "Hello Everyone! I am Pavan's chatbot. My name is T-Rex."),
        "Hindi": ('hi', "नमस्ते सभी को! मैं पवन का चैटबॉट हूँ। मेरा नाम टी-रेक्स है।"),
        "Telugu": ('te', "అందరికీ నమస్కారం! నేను పవన్ యొక్క చాట్బాట్‌ని. నా పేరు టీ-రెక్స్."),
        "Marathi": ('mr', "नमस्कार सर्वांना! मी पवनचा चॅटबॉट आहे. माझं नाव टी-रेक्स आहे."),
        "Kannada": ('kn', "ಎಲ್ಲರಿಗೂ ನಮಸ್ಕಾರ! ನಾನು ಪವನನ ಚಾಟ್ಬಾಟ್. ನನ್ನ ಹೆಸರು ಟಿ-ರೆಕ್ಸ್."),
        "Tamil": ('ta', "வணக்கம் அனைவருக்கும்! நான் பவன் நாட்டு பேச்சாளர். என் பெயர் டி-ரெக்ஸ்.")
    }

    # Dropdown to choose the voice accent/language
    st.write("#### Voice Accent / Language")
    accent_choice = st.selectbox("Choose a voice/accent or language", list(language_options.keys()))

    # Set default language and sample text based on selected language
    language = language_options[accent_choice][0]
    default_text = language_options[accent_choice][1]

    # File uploader for text input
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    # Text to be spoken, starts with the default language sample
    mytext = default_text

    # If a file is uploaded, read its content
    if uploaded_file is not None:
        # Read the file contents
        mytext = uploaded_file.read().decode("utf-8")
        st.success("File uploaded successfully!")
        
        # Check if the text is in English, then translate to the chosen language
        translator = Translator()
        detected_lang = translator.detect(mytext).lang
        if detected_lang == 'en' and language != 'en':  # Only translate if it's English and the target language is not English
            translated_text = translator.translate(mytext, dest=language).text
            mytext = translated_text
            st.success(f"Text translated to {accent_choice}!")
        else:
            st.info(f"Text is in {detected_lang}, no translation needed.")

    # Text area for display and editing
    user_input_text = st.text_area("Text to be read aloud:", mytext, height=100)

    # Button to link to GitHub
    if st.button("Code!"):
        github_url = "https://github.com/Pavansai20054/gTTS/blob/main/app.py"  # Replace with your GitHub URL
        st.markdown(f"[Here you will get the code.]({github_url})", unsafe_allow_html=True)

    # Translate user input if provided
    if user_input_text:
        translator = Translator()
        translated_text = translator.translate(user_input_text, dest=language).text
        mytext = translated_text

        # Perform text-to-speech with the selected accent/language
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
