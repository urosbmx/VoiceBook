# PDF to Audiobook Converter


This project is a command-line interface (CLI) tool built with [Typer](https://typer.tiangolo.com/) that converts PDF files into audiobooks in MP3 format. It utilizes [PyPDF3](https://pypi.org/project/PyPDF3/) and [pdfplumber](https://pypi.org/project/pdfplumber/) for PDF processing and [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech synthesis.

## Features

- Convert PDF files to audiobooks.
- Specify the output filename for the audiobook.
- Simple and intuitive CLI interface.
- Supports various operating systems (Linux, macOS, Windows).

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pdf-to-audiobook.git

2. Navigate to the project directory:
   ```bash
   cd pdf-to-audiobook
   
3. Install the required dependencies: 
   ```bash
   pip install -r requirements.txt

## Usage

To convert a PDF file into an audiobook, use the following command:

```bash
 python audio_book.py  /path/to/pdf_file.pdf
```
Replace /path/to/pdf_file.pdf with the actual path to your PDF file.

The audiobook will be saved as name_of_your_pdf_file.mp3 by default.