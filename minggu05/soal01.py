def cek_angka(a, b, c):
    if (a != b and b != c and c != a) and (a + b == c or b + c == a or c + a == b):
        return True
    else:
        return False

print(cek_angka(1, 2, 3))
print(cek_angka(1, 2, 4))
print(cek_angka(3, 3, 3))