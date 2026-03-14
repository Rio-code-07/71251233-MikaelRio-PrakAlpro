print("Program penghitung IPS Mahasiswa")
jumlah_mk = int(input("Berapa jumlah mata kuliah? "))

total_bobot = 0
sks_per_mk = 3

for i in range(1, jumlah_mk + 1):
    nilai = input(f"Nilai MK {i}: ").upper()
    
    if nilai == "A":
        bobot = 4
    elif nilai == "B":
        bobot = 3
    elif nilai == "C":
        bobot = 2
    elif nilai == "D":
        bobot = 1
    else:
        bobot = 0
    
    total_bobot += bobot * sks_per_mk

total_sks = jumlah_mk * sks_per_mk
ips = total_bobot / total_sks

print(f"Nilai IPS anda semester ini {ips:.2f}")
