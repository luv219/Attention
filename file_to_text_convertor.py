import os
from docx import Document
import fitz  # PyMuPDF
from tkinter import Tk, filedialog

# Function to extract text from a Word document
def extract_text_from_word(word_path):
    doc = Document(word_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to extract text from a PDF document
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text += page.get_text()
    return text

# Function to save text to a .txt file
def save_to_txt(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Function to ask the user for a file path
def ask_for_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Main function
def main():
    file_path = ask_for_file_path()

    if not file_path:
        print("File selection canceled.")
        return

    if file_path.lower().endswith('.docx'):
        text = extract_text_from_word(file_path)
    elif file_path.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        print("Unsupported file format. Please provide a valid image, Word document, or PDF.")
        return

    if text:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(script_directory, f'{file_name}_output.txt')
        save_to_txt(text, output_path)
        print(f"Text extracted and saved to {output_path}")

if __name__ == "__main__":
    main()