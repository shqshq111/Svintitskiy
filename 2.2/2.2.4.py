def mod_inv(a, p):
    return pow(a, -1, p)


def point_add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        l = (3 * x1 * x1 + a) * mod_inv(2 * y1, p) % p
    else:
        l = (y2 - y1) * mod_inv(x2 - x1, p) % p

    x3 = (l * l - x1 - x2) % p
    y3 = (l * (x1 - x3) - y1) % p

    return (x3, y3)


def list_points(a, b, p):
    points = []
    for x in range(p):
        for y in range(p):
            if (y * y - (x * x * x + a * x + b)) % p == 0:
                points.append((x, y))
    return points


p = 7
a = 1
b = 3

points = list_points(a, b, p)
print("Точки кривой:", points)

print("\nТаблица сложения:")
for P in points:
    row = []
    for Q in points:
        row.append(point_add(P, Q, a, p))
    print(row)