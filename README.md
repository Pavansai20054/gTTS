# Pavansai's Project Portfolio

Here you can find several projects, mainly on **Text-to-Speech** and **Language Translation**. In this project, the user can upload different types of files (text, PDF, Word, or image), extract the text, and listen to the text being read aloud in different languages.

## Features

### 1. Text-to-Speech Bot (Xara)

- Uploading a **text file**, **PDF**, **Word document**, or **image** to extract the text.
- Reading the text out loud by the app, after extraction using the **Google Text-to-Speech (gTTS)** API
- **Translation**: Choose from languages either as **Indian** or **International** for translation.
- Listen to the text after translation in the chosen language
- Supported Languages
    Indian and International languages
 There are many of them including Hindi and English, French, Arabic, many more.
  
### 2. **File Upload Support**
File Type Allowed.
- This file type: **Text files** (.txt)
- **PDF files** (`.pdf`)
  - **Word documents** (`.docx`)
  - **Images** (`.jpg`, `.jpeg`, `.png`) using **EasyOCR** for text extraction.

### 3. **Select Language**
- Indian languages - Hindi, Tamil, Telugu, etc.
- International languages - English, French, Spanish, etc.
App translates and does text-to-speech for selected language

## Getting Started

This project can be run locally with the following steps:

### Prerequisites :
Requirements
Python 3.6 or above
Streamlit
gTTS (Google Text-to-Speech)
Googletrans
(for translation)
EasyOCR
PyPDF2
python-docx
Pillow
chardet

### Step 1: Clone the repository

```bash
git clone https://github.com/Pavansai20054/Pavansais-Project-Portfolio.git
cd Pavansais-Project-Portfolio
```

### Step 2: Create a Python virtual environment

```bash
conda create --name pavansai-env python=3.10
conda activate pavansai-env
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: If you don’t have a requirements.txt, manually install dependencies using:
>```bash
>conda install streamlit
>pip install gTTS googletrans easyocr PyPDF2 python-docx Pillow chardet
>```

### Step 4: Run the App
```bash
streamlit run app.py
```

## How to Use
**Home Page:** On the home page, you can select from a variety of projects. Select Text-To-Speech to use the Text-to-Speech functionality.
Upload a File: Upload a text, PDF, Word document, or image.
Text Extraction: The app will extract the text from the uploaded file.
Select Language: Choose the language in which you want the text to be translated (Indian or International).
Translate and Speak: Press the "Translate" button to translate the text and listen to it via text-to-speech.
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or feedback, you can reach me at:

Email: pavansai.20066@gmail.com

GitHub: https://github.com/Pavansai20054

