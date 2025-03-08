nama = input("\nNama: ")
nik = input("NIK: ")
status = input("Status (Pegawai Tetap/Honor): ")
golongan = input("Golongan (A/B/C): ")

if status == "Pegawai Tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
elif status == "Pegawai Honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000

gaji_total = gaji + bonus

print(f"Gaji: {gaji}")
print(f"Bonus: {bonus}")
print(f"Gaji Total: {gaji_total}\n")
