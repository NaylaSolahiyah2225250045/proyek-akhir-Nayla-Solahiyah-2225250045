"""
Modul Utilitas
Berisi fungsi bantu untuk validasi input angka dan sisi segitiga.
"""

import math

def input_angka_positif(pesan):
    """Meminta angka yang valid dan lebih besar dari nol."""
    while True:
        try:
            nilai = float(input(pesan))

            if not math.isfinite(nilai):
                print(
                    "[Error] Masukkan angka yang valid dan terbatas."
                )
            elif nilai <= 0:
                print(
                    "[Error] Nilai harus lebih besar dari 0."
                )
            else:
                return nilai

        except ValueError:
            print(
                "[Error] Masukan harus berupa angka. "
                "Silakan coba lagi."
            )

def validasi_sisi_segitiga(s1, s2, s3):
    """Memeriksa apakah tiga sisi dapat membentuk segitiga."""
    return (
        s1 + s2 > s3
        and s1 + s3 > s2
        and s2 + s3 > s1
    )