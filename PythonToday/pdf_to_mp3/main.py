from gtts import gTTS
import pdfplumber
from pathlib import Path

TEXT1='text1.txt'
TEXT2='text2.txt'

def pdf_to_mp3(file_path='test.pdf',language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix=='.pdf':
        # return 'File exists!'

        with pdfplumber.PDF(open(file=file_path,mode='rb')) as pdf:
            pages =  [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)

        with open(TEXT1,'w') as file:
            file.write(text)

        text=text.replace('\n','')

        with open(TEXT2,'w') as file:
            file.write(text)
    else:
        return 'File does not exist, check the file path!'

def main():
    print(pdf_to_mp3(file_path="./2.pdf"))

if __name__ == '__main__':
    if Path(TEXT1).exists(): Path(TEXT1).unlink()
    if Path(TEXT2).exists(): Path(TEXT2).unlink()
    main()