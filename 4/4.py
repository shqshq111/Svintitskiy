import os

BLOCK_SIZE = 16  

def generate_block_key(filename, size=16):
    key = os.urandom(size)
    with open(filename, 'wb') as f:
        f.write(key)
    print(f"Ключ ({size*8} бит) сохранён в '{filename}'")


def block_cipher_file(input_file, key_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    with open(key_file, 'rb') as f:
        key = f.read()

    if len(key) != BLOCK_SIZE:
        print(f"Ошибка: ключ должен быть {BLOCK_SIZE} байт")
        return

    output = bytearray()
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i+BLOCK_SIZE]
        if len(block) < BLOCK_SIZE:
            block += bytes([BLOCK_SIZE - len(block)] * (BLOCK_SIZE - len(block)))
        encrypted_block = bytes([b ^ k for b, k in zip(block, key)])
        output.extend(encrypted_block)

    with open(output_file, 'wb') as f:
        f.write(output)

    print(f"Файл '{output_file}' успешно обработан!")


def main_menu():
    while True:
        print("1. Сгенерировать ключ")
        print("2. Зашифровать/расшифровать файл")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Имя файла для ключа (bin): ")
            generate_block_key(filename, BLOCK_SIZE)

        elif choice == '2':
            input_file = input("Файл для обработки: ")
            key_file = input("Файл ключа: ")
            output_file = input("Имя выходного файла: ")
            block_cipher_file(input_file, key_file, output_file)

        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()