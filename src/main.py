"""
Program Utama Kalkulator Geometri SMP Kelas VII
Mengatur menu, input pengguna, hasil perhitungan, dan riwayat.
"""

from analisis import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran
)
from utilitas import (
    input_angka_positif,
    validasi_sisi_segitiga
)
from data_io import simpan_riwayat, baca_riwayat


def tampilkan_menu_utama():
    """Menampilkan menu utama program."""
    print("\n" + "=" * 45)
    print("  KALKULATOR LUAS & KELILING BANGUN DATAR SMP")
    print("=" * 45)
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Lihat Riwayat Perhitungan")
    print("0. Keluar Program")
    print("=" * 45)


def pilih_operasi():
    """Meminta pengguna memilih jenis perhitungan."""
    print("\nPilih Jenis Perhitungan:")
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print("3. Hitung Luas dan Keliling Sekaligus")
    print("0. Kembali ke Menu Utama")

    return input("Masukkan pilihan (0-3): ").strip()


def tampilkan_hasil(
    nama_bangun, luas, keliling,
    langkah_luas, langkah_keliling, pilihan
):
    """Menampilkan rumus dan hasil sesuai pilihan."""
    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Bangun datar: {nama_bangun}")

    if pilihan in ("1", "3"):
        print("\n" + langkah_luas)

    if pilihan in ("2", "3"):
        print("\n" + langkah_keliling)


def buat_teks_riwayat(
    nama_bangun, ukuran, luas, keliling, pilihan
):
    """Menyusun hasil perhitungan untuk disimpan."""
    teks = f"Bangun datar: {nama_bangun}\n{ukuran}"

    if pilihan in ("1", "3"):
        teks += f"\nLuas: {luas:.2f} cm²"

    if pilihan in ("2", "3"):
        teks += f"\nKeliling: {keliling:.2f} cm"

    return teks


def main():
    """Menjalankan alur utama program."""
    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "0":
            print(
                "\nTerima kasih telah menggunakan program ini. "
                "Semangat belajarnya!"
            )
            break

        if pilihan == "5":
            baca_riwayat()
            continue

        if pilihan not in ("1", "2", "3", "4"):
            print(
                "[Error] Pilihan menu tidak valid. "
                "Masukkan angka 0-5."
            )
            continue

        sub_pilihan = pilih_operasi()

        if sub_pilihan == "0":
            continue

        if sub_pilihan not in ("1", "2", "3"):
            print("[Error] Pilihan operasi tidak valid!")
            continue

        nama_bangun = ""
        ukuran = ""
        luas = 0.0
        keliling = 0.0
        langkah_luas = ""
        langkah_keliling = ""

        # 1. Persegi
        if pilihan == "1":
            nama_bangun = "Persegi"
            sisi = input_angka_positif(
                "Masukkan panjang sisi (cm): "
            )

            luas, keliling, langkah_luas, langkah_keliling = (
                hitung_persegi(sisi)
            )

            ukuran = f"Sisi: {sisi:g} cm"

        # 2. Persegi panjang
        elif pilihan == "2":
            nama_bangun = "Persegi Panjang"
            panjang = input_angka_positif(
                "Masukkan panjang (cm): "
            )
            lebar = input_angka_positif(
                "Masukkan lebar (cm): "
            )

            luas, keliling, langkah_luas, langkah_keliling = (
                hitung_persegi_panjang(panjang, lebar)
            )

            ukuran = (
                f"Panjang: {panjang:g} cm\n"
                f"Lebar: {lebar:g} cm"
            )

        # 3. Segitiga
        elif pilihan == "3":
            nama_bangun = "Segitiga"

            # Alas dan tinggi diperlukan untuk menghitung luas.
            if sub_pilihan in ("1", "3"):
                alas = input_angka_positif(
                    "Masukkan alas (cm): "
                )
                tinggi = input_angka_positif(
                    "Masukkan tinggi (cm): "
                )
            else:
                alas = 0.0
                tinggi = 0.0

            # Ketiga sisi diperlukan untuk menghitung keliling.
            if sub_pilihan in ("2", "3"):
                print(
                    "\nMasukkan panjang ketiga sisi segitiga:"
                )

                while True:
                    s1 = input_angka_positif("Sisi 1 (cm): ")
                    s2 = input_angka_positif("Sisi 2 (cm): ")
                    s3 = input_angka_positif("Sisi 3 (cm): ")

                    if validasi_sisi_segitiga(s1, s2, s3):
                        break

                    print(
                        "[Error] Ketiga sisi tidak dapat "
                        "membentuk segitiga. Jumlah dua sisi "
                        "harus lebih besar daripada sisi ketiga."
                    )
                    print("Silakan masukkan ketiga sisi kembali.")

            else:
                s1 = 0.0
                s2 = 0.0
                s3 = 0.0

            luas, keliling, langkah_luas, langkah_keliling = (
                hitung_segitiga(alas, tinggi, s1, s2, s3)
            )

            if sub_pilihan == "1":
                ukuran = (
                    f"Alas: {alas:g} cm\n"
                    f"Tinggi: {tinggi:g} cm"
                )
            elif sub_pilihan == "2":
                ukuran = (
                    f"Sisi 1: {s1:g} cm\n"
                    f"Sisi 2: {s2:g} cm\n"
                    f"Sisi 3: {s3:g} cm"
                )
            else:
                ukuran = (
                    f"Alas: {alas:g} cm\n"
                    f"Tinggi: {tinggi:g} cm\n"
                    f"Sisi 1: {s1:g} cm\n"
                    f"Sisi 2: {s2:g} cm\n"
                    f"Sisi 3: {s3:g} cm"
                )

        # 4. Lingkaran
        elif pilihan == "4":
            nama_bangun = "Lingkaran"
            r = input_angka_positif(
                "Masukkan jari-jari (cm): "
            )

            luas, keliling, langkah_luas, langkah_keliling = (
                hitung_lingkaran(r)
            )

            ukuran = f"Jari-jari: {r:g} cm"

        # Menampilkan hasil sesuai operasi yang dipilih.
        tampilkan_hasil(
            nama_bangun,
            luas,
            keliling,
            langkah_luas,
            langkah_keliling,
            sub_pilihan
        )

        # Menyimpan hasil perhitungan ke file riwayat.
        hasil_teks = buat_teks_riwayat(
            nama_bangun,
            ukuran,
            luas,
            keliling,
            sub_pilihan
        )

        simpan_riwayat(hasil_teks)
        print("\n[Sukses] Hasil perhitungan telah dicatat ke riwayat.")


if __name__ == "__main__":
    main()
