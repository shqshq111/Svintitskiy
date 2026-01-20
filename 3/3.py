import random
import string
import os


def generate_random_file(filename, size):
    with open(filename, 'wb') as f:
        for _ in range(size):
            f.write(random.randint(0, 255).to_bytes(1, 'big'))
    print(f"Файл ключа '{filename}' с {size} байтами успешно создан!")



def generate_plaintext_file(filename, size):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(size):
            f.write(random.choice(string.ascii_letters + string.digits + ' '))
    print(f"Файл для шифрования '{filename}' создан ({size} символов).")


# Шифр Вернама 

def vernam_cipher(input_file, key_file, output_file):
    with open(input_file, 'rb') as f_input, open(key_file, 'rb') as f_key, open(output_file, 'wb') as f_output:
        input_bytes = f_input.read()
        key_bytes = f_key.read()

        if len(key_bytes) < len(input_bytes):
            print("Ошибка: ключ меньше размера входного файла!")
            return

        cipher_bytes = bytes([b ^ k for b, k in zip(input_bytes, key_bytes)])
        f_output.write(cipher_bytes)
    print(f"Файл '{output_file}' успешно создан!")


# RC4

def rc4(key, data):
    S = list(range(256))
    j = 0
    out = bytearray()
    key = [k for k in key]

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(byte ^ K)
    return bytes(out)

def rc4_file(input_file, key_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    with open(key_file, 'rb') as f:
        key = f.read()
    encrypted = rc4(key, data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    print(f"Файл '{output_file}' успешно создан!")


def main_menu():
    while True:
        print("\n=== Поточные шифры ===")
        print("1. Сгенерировать случайный ключ")
        print("2. Создать случайный файл для шифрования")
        print("3. Шифрование/расшифрование шифром Вернама")
        print("4. Шифрование/расшифрование RC4")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Имя файла для ключа (bin): ")
            size = int(input("Размер ключа (в байтах): "))
            generate_random_file(filename, size)

        elif choice == '2':
            filename = input("Имя файла для создания (txt): ")
            size = int(input("Размер файла (кол-во символов): "))
            generate_plaintext_file(filename, size)

        elif choice == '3':
            input_file = input("Файл для шифрования/расшифрования: ")
            key_file = input("Файл ключа: ")
            output_file = input("Имя выходного файла (bin): ")
            vernam_cipher(input_file, key_file, output_file)

        elif choice == '4':
            input_file = input("Файл для шифрования/расшифрования: ")
            key_file = input("Файл ключа: ")
            output_file = input("Имя выходного файла (bin): ")
            rc4_file(input_file, key_file, output_file)

        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()