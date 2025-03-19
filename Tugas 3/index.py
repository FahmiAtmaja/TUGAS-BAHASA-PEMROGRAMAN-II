# Menyimpan data pegawai dalam list
pegawai_list = []

jumlah_pegawai = int(input("Masukkan jumlah pegawai: "))

for i in range(jumlah_pegawai):
    print(f"\nData Pegawai ke-{i+1}")
    nama = input("Masukkan Nama: ")
    nik = input("Masukkan NIK: ")
    status = input("Masukkan Status Pekerjaan (Tetap/Honor): ").lower()
    golongan = input("Masukkan Golongan (A/B/C): ").lower()

    if status == "tetap":
        gaji_pokok = 1000000
        bonus = {"a": 200000, "b": 400000, "c": 550000}.get(golongan, 0)
    elif status == "honor":
        gaji_pokok = 750000
        bonus = {"a": 150000, "b": 275000, "c": 480000}.get(golongan, 0)
    else:
        print("Status pegawai tidak valid! Data tidak disimpan.")
        continue  # Melanjutkan ke iterasi berikutnya

    gaji_total = gaji_pokok + bonus

    # Menyimpan data pegawai dalam list
    pegawai_list.append({
        "Nama": nama,
        "NIK": nik,
        "Status": status.capitalize(),
        "Golongan": golongan.upper(),
        "Gaji Pokok": gaji_pokok,
        "Bonus": bonus,
        "Gaji Total": gaji_total
    })

# Menampilkan data seluruh pegawai
print("\n--- Data Pegawai ---")
for pegawai in pegawai_list:
    print("\nNama:", pegawai["Nama"])
    print("NIK:", pegawai["NIK"])
    print("Status:", pegawai["Status"])
    print("Golongan:", pegawai["Golongan"])
    print("Gaji Pokok: Rp{:,}".format(pegawai["Gaji Pokok"]))
    print("Bonus: Rp{:,}".format(pegawai["Bonus"]))
    print("Gaji Total: Rp{:,}".format(pegawai["Gaji Total"]))