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
    ["Home", "Text-To-Speech", "Project 2", "Project 3", "Project 4", "Project 5"]
)

# Display content based on the selected project
if project_choice == "Home":
    st.title("Welcome to Pavansai's Project Portfolio!")
    st.write("Select a project from the sidebar to get started.")
    
elif project_choice == "Text-To-Speech":
    st.write("### Welcome to Xara")
    st.write("This project uses text-to-speech to create a chatbot voice.")

    # Define the language options alphabetically sorted
    indian_languages = {
        "Assamese": 'as',
        "Bengali": 'bn',
        "Gujarati": 'gu',
        "Hindi": 'hi',
        "Kannada": 'kn',
        "Konkani": 'gom',
        "Malayalam": 'ml',
        "Marathi": 'mr',
        "Odia": 'or',
        "Punjabi": 'pa',
        "Sanskrit": 'sa',
        "Tamil": 'ta',
        "Telugu": 'te',
        "Urdu": 'ur',
        "Bodo": 'brx',  
        "Dogri": 'doi',  
        "Maithili": 'mai',  
        "Manipuri": 'mni',  
        "Santali": 'sat',  
        "Rajasthani": 'raj',  
        "Sindhi": 'sd',  
        "Nepali": 'ne',  
        "Meitei": 'mni',  
        "Tulu": 'tcy',  
        "Mizo": 'lus',  
        "Kashmiri": 'ks',  
        "Santhali": 'sat'  
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

    # Determine chosen language code and default text based on selection
    chosen_language = None
    default_text = "Hello, I am Xara, Pavan's chatbot."

    # Assign language code and default text based on selection
    if indian_language_choice != "None":
        chosen_language = indian_languages[indian_language_choice]
        default_text = f"Hello, I am Pavan's chatbot, My name is Xara, I can also speak {indian_language_choice}."
    elif international_language_choice != "None":
        chosen_language = international_languages[international_language_choice]
        default_text = f"Hello, I am Pavan's chatbot, My name is Xara, I can also speak {international_language_choice}."

    # File uploader for text input
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    # Text to be spoken, starts with the default language sample
    mytext = default_text

    # If a file is uploaded, read its content
    if uploaded_file is not None:
        mytext = uploaded_file.read().decode("utf-8")
        st.success("File uploaded successfully!")

    # Text area for display and editing
    user_input_text = st.text_area("Text to be read aloud:", mytext, height=100)

    # Buttons for Translate and Code
    col1, col2 = st.columns(2)

    # Translate button (first column)
    with col1:
        if st.button("Translate"):
            if user_input_text and chosen_language:
                try:
                    translator = Translator()
                    translated_text = translator.translate(user_input_text, dest=chosen_language).text
                    
                    # Display the translated text
                    st.write("### Translated Text:")
                    st.write(translated_text)
                    
                    st.success(f"Text translated to {indian_language_choice or international_language_choice}!")

                    # Generate audio in the selected language
                    output = gTTS(text=translated_text, lang=chosen_language, slow=False)

                    # Save the audio file
                    output_file = "translated_output.mp3"
                    output.save(output_file)

                    # Play the audio file
                    st.audio(output_file)  # Streamlit method to play audio
                except Exception as e:
                    st.error(f"An error occurred during translation: {e}")

    # Code button (second column)
    with col2:
        if st.button("Code!"):
            github_url = "https://github.com/Pavansai20054/gTTS/blob/main/app.py"  # Replace with your GitHub URL
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
