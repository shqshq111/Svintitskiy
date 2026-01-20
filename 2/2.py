import math
import random
from collections import Counter

def symbol_frequencies(filename):
    with open(filename, "rb") as f:
        data = f.read()

    freq = Counter(data)
    total = len(data)

    print("Частоты:")
    for byte, count in freq.items():
        print(byte, ":", count / total)

    return freq, total


def file_entropy(filename):
    with open(filename, "rb") as f:
        data = f.read()

    freq = Counter(data)
    total = len(data)

    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)

    print("Энтропия:", entropy)
    return entropy


def generate_same(filename, size, byte_value):
    with open(filename, "wb") as f:
        f.write(bytes([byte_value] * size))


def generate_binary_random(filename, size):
    with open(filename, "wb") as f:
        data = [random.choice([0, 1]) for _ in range(size)]
        f.write(bytes(data))


def generate_full_random(filename, size):
    with open(filename, "wb") as f:
        data = [random.randint(0, 255) for _ in range(size)]
        f.write(bytes(data))


generate_same("same.txt", 100000, 65)
generate_binary_random("binary.txt", 100000)
generate_full_random("random.txt", 100000)

print("\nФайл same.txt")
symbol_frequencies("same.txt")
file_entropy("same.txt")

print("\nФайл binary.txt")
symbol_frequencies("binary.txt")
file_entropy("binary.txt")

print("\nФайл random.txt")
symbol_frequencies("random.txt")
file_entropy("random.txt")