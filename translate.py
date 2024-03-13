import os
import re
from googletrans import Translator
from tqdm import tqdm

# Определение пути к директории с файлами VTT
DIRECTORY = '/Users/captions' write your path to the captions


# Чтение файла VTT
def read_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


# Перевод текста
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    try:
        # Пытаемся выполнить перевод
        translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
        # Проверяем, не вернул ли переводчик None
        if translated_text is None:
            raise ValueError("Translation returned None")
        return translated_text
    except Exception as e:
        # В случае возникновения исключения возвращаем оригинальный текст
        print(f"Error during translation: {e}")
        return text



# Обработка и сохранение файла
def process_vtt(file_path, dest_file_path, src_lang, dest_lang):
    content = read_vtt(file_path)
    translated_content = translate_text(content, src_lang, dest_lang)

    with open(dest_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_content)


# Обработка всех файлов VTT в папке
def process_all_vtt(directory, src_lang, dest_lang):
    for filename in tqdm(os.listdir(directory), desc='Processing files'):
        if filename.endswith('.vtt'):
            file_path = os.path.join(directory, filename)
            dest_file_path = os.path.join(directory, f'translated_{filename}')
            process_vtt(file_path, dest_file_path, src_lang, dest_lang)


# Запуск обработки файлов в заданной папке
process_all_vtt(DIRECTORY, 'en', 'ru')

