# Matriks A dan Matriks B yang akan dikalikan
matriks_a = [
    [5, 7, 9, 11, 13],
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [11, 13, 15, 17, 19],
    [10, 12, 14, 16, 18],
]

matriks_b = [
    [5, 8, 11, 14, 17],
    [2, 5, 8, 11, 14],
    [6, 10, 14, 18, 22],
    [10, 15, 20, 25, 30],
    [5, 7, 9, 11, 13],
]

# Inisialisasi list untuk menyimpan hasil perkalian
hasil_matriks = []

# Perkalian matriks A dan matriks B
for i in range(len(matriks_a)):
    baris_hasil = []  # Menyimpan hasil untuk baris ke-i
    for j in range(len(matriks_b[0])):
        nilai = 0
        for k in range(len(matriks_b)):
            nilai += matriks_a[i][k] * matriks_b[k][j]
        baris_hasil.append(nilai)
    hasil_matriks.append(baris_hasil)

# Menampilkan hasil perkalian matriks
print("Hasil perkalian matriks:")
for baris in hasil_matriks:
    print(baris)
