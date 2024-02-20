from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

TEXT1 = "text1.txt"
TEXT2 = "text2.txt"


def pdf_to_mp3(file_path="test.pdf", language="en"):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        # return 'File exists!'
        print(f"[+] Original file: {Path(file_path).name}")
        print("[+] Processing...")

        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = "".join(pages)

        # temporatily
        with open(TEXT1, "w") as file:
            file.write(text)

        text = text.replace("\n", "")

        # temporatily
        with open(TEXT2, "w") as file:
            file.write(text)

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")

        return f"[+] {file_name}.mp3 saved successfully\n...Have a good day"

    else:
        return "File does not exist, check the file path!"


def main():
    tprint("PDF>>TO>>MP3", font="")
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example, 'en' or 'ru'")
    print(
        pdf_to_mp3(
            file_path=("./1.pdf" if file_path == "" else file_path),
            language="en" if language == "" else language,
        )
    )


if __name__ == "__main__":
    if Path(TEXT1).exists():
        Path(TEXT1).unlink()
    if Path(TEXT2).exists():
        Path(TEXT2).unlink()
    main()
