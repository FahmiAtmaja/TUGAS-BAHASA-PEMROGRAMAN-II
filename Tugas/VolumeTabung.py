import math

def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi

jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))
print(f"Volume tabung: {volume_tabung(jari_jari, tinggi)}cm³")