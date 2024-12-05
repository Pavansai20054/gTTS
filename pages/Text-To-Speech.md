# Xara! Text-To-Speech Project by Tech T-Rex 🚀💬

Welcome to **Xara**, a multilingual Text-To-Speech (TTS) application. This project allows users to convert text from uploaded files or images into speech in various Indian and international languages. 🌐🗣️

---

## Features ✨

- **Language Support**: Supports translation and speech generation in multiple Indian and international languages. 🌍
- **File Handling**: Supports text files, PDFs, Word documents, and images for extracting text. 📂🖼️
- **Image-to-Text**: Utilizes EasyOCR for text extraction from image files. 🖋️
- **Text Translation**: Integrates GoogleTranslator for multilingual translation. 🔄
- **Text-to-Speech**: Converts text to speech using Google Text-to-Speech (gTTS). 🗣️
- **Responsive UI**: Built with Streamlit, ensuring a user-friendly interface. 🖥️

---

## Installation 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/Pavansai20054/gTTS.git
   cd gTTS
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run pages/2_Text-To-Speech.py
   ```

---

## Usage 🎛️

1. **Launch the App**:
   Open the app in your browser after running the `streamlit` command. 🌐

2. **Choose a Language**:
   Select an Indian or international language from the dropdown menus. Only one language type can be selected at a time. 🗂️

3. **Upload Files**:
   - Supported file types: `.txt`, `.pdf`, `.docx`, `.jpg`, `.jpeg`, `.png`.
   - The app extracts text from the uploaded file. 📤

4. **Translate and Speak**:
   - Translate the extracted text to the selected language. 🌍
   - Listen to the translated text using the `Translate and Speak` button. 🔊

5. **Access the Code**:
   Click the `Code!` button to view the source code on GitHub. 🧑‍💻

---

## File Types Supported 📑

- **Text files (`.txt`)**: Automatically detects file encoding for accurate text extraction. 📝
- **PDFs (`.pdf`)**: Extracts text from all pages. 📄
- **Word documents (`.docx`)**: Extracts text from paragraphs. 📃
- **Images (`.jpg`, `.jpeg`, `.png`)**: Uses OCR to extract text from image files. 🖼️

---

## Dependencies 🧰

- **[Streamlit](https://streamlit.io/)**: For creating the user interface. 🖥️
- **[gTTS](https://pypi.org/project/gTTS/)**: For text-to-speech conversion. 🗣️
- **[Deep Translator](https://pypi.org/project/deep-translator/)**: For language translation. 🌍
- **[EasyOCR](https://pypi.org/project/easyocr/)**: For optical character recognition. 🖋️
- **[PyPDF2](https://pypi.org/project/PyPDF2/)**: For PDF text extraction. 📄
- **[python-docx](https://python-docx.readthedocs.io/en/latest/)**: For Word document processing. 📃
- **[chardet](https://pypi.org/project/chardet/)**: For text encoding detection. 🔍
- **[Pillow](https://pillow.readthedocs.io/en/stable/)**: For image file handling. 🖼️

Install all dependencies using `pip install -r requirements.txt`. 📥

---

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details. ✅

---

## Author 🖊️

Developed by **Pavansai**. 👨‍💻

GitHub: [Pavansai20054](https://github.com/Pavansai20054) 🌟

---

## Contributing 🤝

Contributions are welcome! Feel free to fork the repository and submit a pull request. 🔧

---

## Acknowledgements 🙏

- Thanks to the open-source community for providing the libraries and tools used in this project. 🌐
- Special mention to **Tech T-Rex** for inspiration and support. 🦖
