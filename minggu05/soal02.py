angka1 = int(input("Masukan angka: "))
angka2 = int(input("Masukan angka: "))
angka3 = int(input("Masukan angka: "))

def cek_digit_belakang(a, b ,c):
    if angka1 % 10 == angka2 % 10 or angka2 % 10 == angka3 % 10 or angka3 % 10 == angka1 % 10:
        return True
    else:
        return False    

print(cek_digit_belakang(angka1, angka2, angka3))