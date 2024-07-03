def convert_to_binary(input_file_path, output_file_path):
    # Чтение данных из входного файла
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Удаление пробельных символов (если есть)
    lines = [line.strip() for line in lines]

    # Преобразование строк в байты и запись в бинарный файл
    with open(output_file_path, 'wb') as binary_file:
        for line in lines:
            # Конвертация строки в байты и запись в файл
            binary_data = bytes.fromhex(line)
            binary_file.write(binary_data)

# Путь к входному и выходному файлам
input_file_path = r'C:\Users\lp85d\Desktop\pairs_combinations.txt'
output_file_path = r'C:\Users\lp85d\Desktop\pairs_combinations.bin'

# Запуск функции конвертации
convert_to_binary(input_file_path, output_file_path)
