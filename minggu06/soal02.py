def ganjil(batas_bawah, batas_atas):
    if batas_bawah < batas_atas:
        hasil = []
        for i in range(batas_bawah, batas_atas +1):
            if i % 2 != 0:
                hasil.append(i)
        print(f"bawah = {batas_bawah}, atas = {batas_atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah: ", end="")
        print(*hasil, sep=", ", end=".\n")

    else:
        hasil = []
        for i in range(batas_bawah, batas_atas - 1, -1):
            if i % 2 != 0:
                hasil.append(i)
        print(f"bawah = {batas_bawah}, atas = {batas_atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah: ", end="")
        print(*hasil, sep=", ", end=".\n")

batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

ganjil(batas_bawah, batas_atas)






