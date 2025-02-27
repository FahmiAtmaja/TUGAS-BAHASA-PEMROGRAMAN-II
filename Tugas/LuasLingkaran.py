import math

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
print(f"Luas lingkaran: {luas_lingkaran(jari_jari)}cm²")