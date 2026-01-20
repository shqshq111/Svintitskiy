def multiplication_table(P):
    elements = list(range(1, P))

    print(f"Демонстрация группового закона для умножения по модулю P={P}")
    print("+----" * (P) + "+")

    header = "| *  |"
    for a in elements:
        header += f"{a:>4}|"
    print(header)
    print("+----" * (P) + "+")

    for a in elements:
        row = f"| {a:>2} |"
        for b in elements:
            row += f"{(a * b) % P:>4}|"
        print(row)

    print("+----" * (P) + "+")


P = 7
multiplication_table(P)