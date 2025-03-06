import os  # Для работы с файловой системой
import sys  # Для работы с аргументами командной строки
import json  # Для работы с JSON-форматом
from datetime import datetime  # Для работы с датой и временем

def find_files(fragment_path, fragment_name):
    """
    Ищет файлы в указанной директории, имя которых содержит фрагмент, переданный в аргументе fragment_name.
    Параметры:
    fragment_path (str): Путь к директории, в которой нужно искать файлы.
    fragment_name (str): Фрагмент имени файла, который нужно найти.
    Возвращает:
    list: Список словарей с информацией о найденных файлах (имя, путь, размер и дата создания).
    """
    results = []  # Список для хранения найденных файлов
    # Проходим по всем директориям и файлам, начиная с fragment_path
    for root, _, files in os.walk(fragment_path):
        for file in files:
            # Если фрагмент имени файла присутствует в имени файла
            if fragment_name in file:
                file_path = os.path.join(root, file)  # Полный путь к файлу
                file_info = {
                    "name": file,  # Имя файла
                    "path": file_path,  # Путь к файлу
                    "size": os.path.getsize(file_path),  # Размер файла в байтах
                    "created": datetime.fromtimestamp(os.path.getctime(file_path)).isoformat()  # Дата и время создания файла в формате ISO
                }
                results.append(file_info)  # Добавляем информацию о файле в результат
    return results  # Возвращаем список найденных файлов

if __name__ == "__main__":  # Проверка, если скрипт запускается как main
    # Проверяем, что передано достаточное количество аргументов (путь и имя файла)
    if len(sys.argv) < 3:
        print("Некорректный ввод, необходимо ввести в формате: python mcp_server.py <Фрагмент пути> <Имя файла>")
        sys.exit(1)  # Завершаем выполнение с кодом ошибки

    search_path = sys.argv[1]  # Путь для поиска файлов
    file_name = sys.argv[2]  # Имя или фрагмент имени файла для поиска

    # Проверяем, существует ли указанный путь
    if not os.path.exists(search_path):
        print(f"Ошибка: путь '{search_path}' не найден!")
        sys.exit(1)  # Завершаем выполнение с кодом ошибки

    # Вызываем функцию для поиска файлов
    found_files = find_files(search_path, file_name)

    # Выводим результат в формате JSON с отступами для читаемости
    print(json.dumps(found_files, indent=2, ensure_ascii=False))
