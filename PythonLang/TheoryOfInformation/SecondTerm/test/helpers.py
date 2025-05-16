def text_to_binary(text):
    """
    Преобразует текст в двоичную строку
    """
    if not text:
        return ""
    
    try:
        # Преобразуем каждый символ в ASCII-код, затем в двоичное представление
        binary = ''
        for char in text:
            # Берем ASCII-код символа
            ascii_code = ord(char)
            # Форматируем в 8-битное двоичное представление
            binary_char = format(ascii_code, '08b')
            binary += binary_char
        return binary
    except Exception as e:
        print(f"Ошибка при преобразовании текста в бинарный код: {e}")
        # В случае ошибки возвращаем пустую строку
        return ""

def binary_to_text(binary):
    """
    Преобразует двоичную строку в текст
    """
    if not binary:
        return ""
    
    # Удаляем пробелы и другие невидимые символы, если они есть
    binary = ''.join(binary.split())
    
    # Проверяем, что строка содержит только 0 и 1
    if not all(bit in '01' for bit in binary):
        binary = ''.join(bit for bit in binary if bit in '01')
    
    # Проверяем, что длина бинарной строки кратна 8
    if len(binary) % 8 != 0:
        # Дополняем нулями до кратности 8
        padding = 8 - (len(binary) % 8)
        binary += '0' * padding
    
    try:
        # Разбиваем бинарную строку на 8-битные блоки и преобразуем в символы
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            # Преобразуем 8-битный блок в число
            ascii_code = int(byte, 2)
            
            # Проверяем, является ли код печатаемым ASCII-символом (32-126)
            # или одним из стандартных управляющих символов
            if 32 <= ascii_code <= 126 or ascii_code in (9, 10, 13):  # TAB, LF, CR
                char = chr(ascii_code)
            else:
                # Заменяем непечатаемые символы на точку
                char = '.'
            
            text += char
        return text
    except Exception as e:
        print(f"Ошибка при преобразовании бинарного кода в текст: {e}")
        # В случае ошибки возвращаем пустую строку
        return "" 