import PyPDF3
import pdfplumber
import typer
import pyttsx3
from rich import print

app = typer.Typer()

def extract_book_content(file):
    """
      Extracts text content from all pages of a PDF file.

      Parameters:
          file (str): Path to the PDF file.

      Returns:
          str: Concatenated text content from all pages of the PDF file.
      """
    book=open(file, 'rb')
    read_book = PyPDF3.PdfFileReader(book)
    finalText = ""
    print(":bulb: [bold green]Your book is start to converting[/bold green] :bulb:")
    with pdfplumber.open(file) as pdf:
        for i in range(0, read_book.numPages):
            page = pdf.pages[i]
            text = page.extract_text()
            finalText +=text

    return finalText

def create_audio_book(book: str, name: str):
    """
      Converts text content of a book into an audio book in MP3 format.

      Parameters:
          book (str): Text content of the book.

      Returns:
          None
      """
    engine = pyttsx3.init()
    engine.save_to_file(book,f"{name}.mp3")
    engine.runAndWait()
    print(":book: [bold purple]Book is read to listen[/bold purple] :book:")


@app.command()
def pdf_to_audiobook(file:str):
    book = extract_book_content(file)
    head, sep, name = file.partition('.')
    create_audio_book(book, head)


if __name__ == "__main__":
    app()
