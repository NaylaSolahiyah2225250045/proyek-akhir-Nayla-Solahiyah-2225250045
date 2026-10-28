# Dokumen Pengujian (Test Case) - Kalkulator Geometri SMP
Dokumen ini digunakan untuk menguji perhitungan luas dan keliling bangun datar, validasi input, serta penyimpanan dan pembacaan riwayat perhitungan.

| ID | Kategori | Input / Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Persegi, sisi 5 cm, pilih luas | Luas = 25 cm² | Belum diuji | Belum diuji |
| TC02 | Normal | Persegi panjang, panjang 8 cm dan lebar 3 cm, pilih keliling | Keliling = 22 cm | Belum diuji | Belum diuji |
| TC03 | Normal | Segitiga, alas 4 cm dan tinggi 3 cm, pilih luas | Luas = 6 cm² tanpa meminta tiga sisi | Belum diuji | Belum diuji |
| TC04 | Normal | Segitiga, sisi 3 cm, 4 cm, dan 5 cm, pilih keliling | Keliling = 12 cm | Belum diuji | Belum diuji |
| TC05 | Normal | Lingkaran, jari-jari 7 cm, pilih luas | Luas = 153,86 cm² | Belum diuji | Belum diuji |
| TC06 | Normal | Persegi, sisi 5 cm, pilih luas dan keliling | Luas = 25 cm² dan keliling = 20 cm | Belum diuji | Belum diuji |
| TC07 | Batas | Persegi, sisi 0,5 cm | Luas = 0,25 cm² dan keliling = 2 cm | Belum diuji | Belum diuji |
| TC08 | Tidak Valid | Ukuran berupa 0 atau -5 | Input ditolak dan diminta memasukkan angka positif | Belum diuji | Belum diuji |
| TC09 | Tidak Valid | Ukuran berupa teks `abc` | Input ditolak dan diminta memasukkan angka | Belum diuji | Belum diuji |
| TC10 | Tidak Valid | Sisi segitiga 2 cm, 3 cm, dan 6 cm | Sisi ditolak karena tidak memenuhi syarat segitiga | Belum diuji | Belum diuji |
| TC11 | Tidak Valid | Memilih menu utama selain 0–5 | Pesan pilihan tidak valid ditampilkan | Belum diuji | Belum diuji |
| TC12 | Normal | Melakukan perhitungan, lalu memilih menu riwayat | Hasil perhitungan sebelumnya ditampilkan | Belum diuji | Belum diuji |
| TC13 | Batas | Membuka riwayat sebelum ada perhitungan | Informasi bahwa riwayat belum tersedia atau masih kosong ditampilkan | Belum diuji | Belum diuji |
| TC14 | Tidak Valid | Memilih operasi selain 0–3 | Pesan pilihan operasi tidak valid ditampilkan | Belum diuji | Belum diuji |

## Catatan Pengujian
1. Pengujian dilakukan setelah program dijalankan melalui terminal VS Code.
2. Hasil aktual diisi berdasarkan hasil yang benar-benar muncul saat pengujian.
3. Status diisi "Berhasil" jika hasil sesuai dengan harapan dan "Gagal" jika tidak sesuai.
4. Pastikan riwayat tersimpan di folder `output`.
5. Ulangi pengujian jika ditemukan kesalahan setelah perbaikan kode.