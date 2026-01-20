def element_order(a, P):
    value = 1
    for k in range(1, P):
        value = (value * a) % P
        if value == 1:
            return k
    return None


def orders_table(P):
    print(f"Порядки элементов по модулю {P}")
    print("+--------+--------+------------+")
    print("|   a    | order  | generator  |")
    print("+--------+--------+------------+")

    for a in range(1, P):
        ord_a = element_order(a, P)
        is_gen = "= p - 1" if ord_a == P - 1 else ""

        print(f"| {a:>6} | {ord_a:>6} | {is_gen:>10} |")

    print("+--------+--------+------------+")


P = 7
orders_table(P)