#  Создание виртуального окружения (в терминале или командной строке)
# python -m venv myenv
#  Активация виртуального окружения (для Windows)
# myenv\Scripts\activate
#  Установка библиотеки python-docx
# pip install python-docx
from docx import Document

def create_word_file(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save('output_document.docx')
    print('Word файл успешно создан.')

if __name__ == "__main__":
    user_input = input("Введите текст для создания Word файла: ")
    create_word_file(user_input)
