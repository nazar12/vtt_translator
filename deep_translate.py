import os
import re
from deep_translator import GoogleTranslator
from tqdm import tqdm

# Определение пути к директории с файлами VTT
DIRECTORY = '/Users/captions'


# Чтение файла VTT
def read_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


# Перевод текста
def translate_text(text, src_lang, dest_lang):
    translator = GoogleTranslator(source=src_lang, target=dest_lang)
    translated_blocks = []

    for block in text.split('\n\n'):
        if '-->' in block:
            lines = block.split('\n')
            for i in range(1, len(lines)):
                lines[i] = translator.translate(lines[i])
            translated_blocks.append('\n'.join(lines))
        else:
            translated_blocks.append(block)

    return '\n\n'.join(translated_blocks)


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
