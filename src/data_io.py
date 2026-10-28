"""
Modul Data I/O
Menyimpan riwayat perhitungan ke file teks dan membacanya kembali.
"""

import os

FOLDER_PROYEK = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

FOLDER_OUTPUT = os.path.join(FOLDER_PROYEK, "output")
FILE_RIWAYAT = os.path.join(
    FOLDER_OUTPUT, "riwayat_hitung.txt"
)

def simpan_riwayat(teks_hasil):
    """Menyimpan hasil perhitungan ke file teks."""
    os.makedirs(FOLDER_OUTPUT, exist_ok=True)

    with open(FILE_RIWAYAT, "a", encoding="utf-8") as file:
        file.write(teks_hasil + "\n")
        file.write("-" * 40 + "\n")

def baca_riwayat():
    """Membaca dan menampilkan riwayat perhitungan."""
    if not os.path.exists(FILE_RIWAYAT):
        print("\n[Info] Belum ada riwayat perhitungan.")
        return

    with open(FILE_RIWAYAT, "r", encoding="utf-8") as file:
        isi = file.read()

    print("\n" + "=" * 10 + " RIWAYAT PERHITUNGAN " + "=" * 10)

    if isi.strip():
        print(isi)
    else:
        print("Riwayat masih kosong.")

    print("=" * 41)