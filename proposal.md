# PROPOSAL PROYEK AKHIR ALGORITMA DAN PEMROGRAMAN
**Judul Proyek:** Program Kalkulator Luas dan Keliling Bangun Datar Berbasis Python untuk Siswa SMP Kelas VII

**Nama:** Nayla Solahiyah  
**NIM:** 2225250045  
**Program Studi:** Pendidikan Matematika  
**Universitas:** Universitas Sultan Ageng Tirtayasa  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Pertemuan:** 14

---

## 1. Judul Proyek
Program Kalkulator Luas dan Keliling Bangun Datar Berbasis Python untuk Siswa SMP Kelas VII

## 2. Latar Belakang
Luas dan keliling bangun datar merupakan materi matematika yang dipelajari siswa SMP kelas VII. Dalam mempelajari materi tersebut, siswa perlu memahami rumus yang digunakan serta cara memasukkan ukuran bangun datar ke dalam perhitungan. Siswa juga perlu membedakan penggunaan rumus luas dan keliling agar tidak keliru ketika menyelesaikan soal.
Berdasarkan kebutuhan tersebut, dibuat program kalkulator luas dan keliling bangun datar menggunakan bahasa pemrograman Python. Program ini dirancang dengan menu sederhana yang memungkinkan pengguna memilih bangun datar dan jenis perhitungan yang diinginkan. Program akan menampilkan rumus, langkah perhitungan, dan hasilnya agar siswa dapat memahami proses penyelesaian soal, bukan hanya melihat hasil akhir.
Program juga dilengkapi validasi input untuk mengurangi kesalahan saat memasukkan ukuran serta fitur penyimpanan riwayat perhitungan ke dalam file teks. Melalui program ini, siswa diharapkan dapat berlatih menghitung luas dan keliling bangun datar secara lebih terarah.

## 3. Pengguna dan Tujuan
### 3.1 Pengguna
Pengguna utama program ini adalah siswa SMP kelas VII yang sedang mempelajari materi luas dan keliling bangun datar. Guru matematika juga dapat menggunakan program sebagai alat bantu untuk memberikan contoh perhitungan dan latihan kepada siswa.
### 3.2 Tujuan
Tujuan pembuatan program ini adalah:
1. Membantu siswa menghitung luas dan keliling persegi, persegi panjang, segitiga, dan lingkaran.
2. Menampilkan rumus dan langkah perhitungan sesuai bangun datar yang dipilih.
3. Membantu siswa membedakan perhitungan luas dan keliling.
4. Melatih siswa menggunakan program sederhana berbasis Python.
5. Menyediakan fitur riwayat agar pengguna dapat melihat kembali hasil perhitungan sebelumnya.

## 4. Ruang Lingkup
### 4.1 Fitur yang Dikembangkan
Program memiliki fitur sebagai berikut:
1. Menampilkan menu utama untuk memilih bangun datar.
2. Menyediakan pilihan perhitungan luas, keliling, atau luas dan keliling sekaligus.
3. Meminta pengguna memasukkan ukuran yang diperlukan sesuai bangun datar dan jenis perhitungan.
4. Memeriksa input agar ukuran berupa angka positif dan sesuai dengan ketentuan bangun datar.
5. Menampilkan rumus, langkah perhitungan, dan hasil akhir.
6. Menyimpan hasil perhitungan ke dalam file teks.
7. Menampilkan riwayat perhitungan yang telah tersimpan.
8. Menyediakan pilihan untuk kembali ke menu utama atau keluar dari program.
### 4.2 Batasan Proyek
1. Program menggunakan bahasa pemrograman Python dan dijalankan melalui terminal atau console.
2. Bangun datar yang dihitung dibatasi pada persegi, persegi panjang, segitiga, dan lingkaran.
3. Ukuran yang dimasukkan harus berupa angka positif. Untuk segitiga, panjang ketiga sisinya juga harus memenuhi syarat pembentukan segitiga.
4. Perhitungan luas segitiga menggunakan alas dan tinggi, sedangkan perhitungan keliling segitiga menggunakan panjang ketiga sisinya.
5. Perhitungan luas dan keliling lingkaran menggunakan nilai π sebesar 3,14.
6. Program tidak menggunakan antarmuka grafis atau GUI.
7. Program ditujukan sebagai alat bantu belajar dan bukan pengganti penjelasan guru.

## 5. Kebutuhan Program
### 5.1 Kebutuhan Fungsional
| Kode | Kebutuhan |
|---|---|
| F01 | Program menampilkan menu utama dan pilihan bangun datar. |
| F02 | Program menerima pilihan jenis perhitungan berupa luas, keliling, atau keduanya. |
| F03 | Program menerima ukuran yang diperlukan sesuai bangun datar dan jenis perhitungan. |
| F04 | Program memvalidasi input dan menolak ukuran yang tidak valid. |
| F05 | Program menghitung luas dan keliling sesuai rumus bangun datar yang dipilih. |
| F06 | Program menampilkan rumus, langkah perhitungan, dan hasil akhir. |
| F07 | Program menyimpan hasil perhitungan ke dalam file teks. |
| F08 | Program membaca dan menampilkan riwayat perhitungan. |
| F09 | Program menyediakan pilihan untuk kembali ke menu utama atau keluar. |
### 5.2 Kebutuhan Nonfungsional
1. Program menggunakan bahasa yang mudah dipahami siswa SMP kelas VII.
2. Tampilan menu dan hasil perhitungan disusun secara rapi.
3. Program menggunakan fungsi dan modul agar kode lebih terstruktur.
4. Kesalahan input ditangani dengan pesan yang jelas tanpa membuat program berhenti secara tiba-tiba.
5. Program dapat dijalankan melalui terminal dengan Python yang telah terpasang.

## 6. IPO (Input, Process, Output)
| Bagian | Keterangan |
|---|---|
| Input | Pilihan bangun datar, pilihan perhitungan, serta ukuran yang diperlukan seperti sisi, panjang, lebar, alas, tinggi, dan jari-jari. |
| Process | Memeriksa pilihan dan ukuran, menentukan rumus, menghitung luas atau keliling, menampilkan langkah perhitungan, serta menyimpan hasil ke file riwayat. |
| Output | Rumus, langkah perhitungan, hasil luas dan/atau keliling, pesan validasi, serta riwayat perhitungan. |
**Contoh IPO**
- Input: Persegi panjang, pilihan luas dan keliling, panjang = 10 cm, lebar = 5 cm.
- Process:
  - Luas = panjang × lebar = 10 × 5 = 50 cm².
  - Keliling = 2 × (panjang + lebar) = 2 × (10 + 5) = 30 cm.
- Output: Luas = 50 cm² dan keliling = 30 cm.

## 7. Algoritma
### 7.1 Pseudocode
```text
MULAI

ULANGI
    Tampilkan menu utama:
        1. Persegi
        2. Persegi panjang
        3. Segitiga
        4. Lingkaran
        5. Riwayat perhitungan
        0. Keluar

    Baca pilihan pengguna

    JIKA pilihan = 0
        Tampilkan pesan penutup
        SELESAI DARI PERULANGAN

    JIKA pilihan = 1, 2, 3, ATAU 4
        Tentukan bangun datar yang dipilih

        Tampilkan pilihan perhitungan:
            1. Luas
            2. Keliling
            3. Luas dan keliling
            0. Kembali

        Baca pilihan perhitungan

        JIKA pilihan perhitungan = 0
            Kembali ke menu utama

        JIKA pilihan perhitungan tidak valid
            Tampilkan pesan kesalahan

        JIKA pilihan perhitungan = luas
            Minta ukuran yang diperlukan untuk luas

        JIKA pilihan perhitungan = keliling
            Minta ukuran yang diperlukan untuk keliling

        JIKA pilihan perhitungan = luas dan keliling
            Minta seluruh ukuran yang diperlukan untuk
            menghitung luas dan keliling

        Periksa input yang dimasukkan

        SELAMA input tidak valid
            Tampilkan pesan kesalahan
            Minta pengguna memasukkan ulang ukuran

        Hitung hasil sesuai rumus bangun datar

        Tampilkan rumus, langkah perhitungan,
        dan hasil akhir

        Simpan hasil perhitungan ke file riwayat

    JIKA pilihan = 5
        Baca file riwayat

        JIKA riwayat tersedia
            Tampilkan riwayat perhitungan
        JIKA tidak
            Tampilkan pesan bahwa riwayat masih kosong

    JIKA pilihan menu utama tidak valid
        Tampilkan pesan kesalahan

SAMPAI pengguna memilih keluar

SELESAI
```

### 7.2 Ketentuan Perhitungan
| Bangun datar | Luas | Keliling |
|---|---|---|
| Persegi | sisi × sisi | 4 × sisi |
| Persegi panjang | panjang × lebar | 2 × (panjang + lebar) |
| Segitiga | ½ × alas × tinggi | sisi 1 + sisi 2 + sisi 3 |
| Lingkaran | 3,14 × jari-jari × jari-jari | 2 × 3,14 × jari-jari |

Khusus segitiga, program meminta alas dan tinggi untuk menghitung luas. Untuk menghitung keliling, program meminta tiga panjang sisi. Jika pengguna memilih menghitung luas dan keliling sekaligus, program meminta alas, tinggi, dan ketiga panjang sisi.

## 8. Struktur Program
### 8.1 Struktur Folder
```text
kalkulator-geometri-smp/
├── README.md
├── proposal.md
├── .gitignore
├── src/
│   ├── main.py
│   ├── geometri.py
│   ├── validasi.py
│   └── data_io.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

File `riwayat_hitung.txt` akan dibuat ketika program mulai menyimpan hasil perhitungan. File tersebut digunakan untuk menyimpan riwayat dan tidak harus tersedia sejak awal.
### 8.2 Fungsi Setiap File
| File | Fungsi |
|---|---|
| `main.py` | Menjalankan program, menampilkan menu, menerima pilihan pengguna, dan mengatur alur program. |
| `geometri.py` | Menyediakan fungsi untuk menghitung luas dan keliling setiap bangun datar serta menyiapkan langkah perhitungannya. |
| `validasi.py` | Memeriksa pilihan menu, jenis perhitungan, ukuran positif, dan validitas panjang sisi segitiga. |
| `data_io.py` | Menyimpan hasil perhitungan ke file teks dan membaca riwayat perhitungan. |
| `test_case.md` | Mencatat skenario pengujian dan hasil yang diharapkan. |
| `README.md` | Menjelaskan tujuan, fitur, struktur folder, dan cara menjalankan program. |
| `proposal.md` | Menyimpan dokumen proposal proyek. |
| `.gitignore` | Menentukan file atau folder yang tidak perlu dilacak oleh Git. |
| `output/.gitkeep` | Mempertahankan folder `output` agar tetap tercatat di repository. |

## 9. Struktur Data
Struktur data dipilih sesuai kebutuhan program agar data mudah diolah dan disimpan.

| Struktur data | Penggunaan | Alasan |
|---|---|---|
| String | Menyimpan nama bangun datar, pilihan menu, rumus, pesan, dan hasil yang akan ditampilkan. | String sesuai untuk mengolah dan menampilkan teks. |
| Tuple | Mengembalikan dua hasil perhitungan, yaitu luas dan keliling, dari fungsi yang menghitung keduanya. | Tuple dapat mengelompokkan beberapa hasil yang berkaitan. |
| List | Menampung riwayat perhitungan selama program berjalan. | List memudahkan penyimpanan dan penelusuran sejumlah data. |
| Dictionary | Menyimpan informasi satu perhitungan dengan pasangan key dan value, seperti nama bangun datar, jenis perhitungan, ukuran, luas, dan keliling. | Dictionary memudahkan akses data berdasarkan nama key. |
| File teks | Menyimpan riwayat perhitungan agar tetap tersedia setelah program ditutup. | File teks memungkinkan data dibaca kembali pada penggunaan berikutnya. |

## 10. Test Case
Pengujian dirancang sebelum implementasi penuh agar program dapat diperiksa berdasarkan hasil yang diharapkan. Test case mencakup kondisi normal, batas, dan input tidak valid.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Persegi, sisi = 5 cm, pilih luas dan keliling. | Luas = 25 cm² dan keliling = 20 cm. |
| TC02 | Normal | Persegi panjang, panjang = 8 cm dan lebar = 3 cm, pilih luas dan keliling. | Luas = 24 cm² dan keliling = 22 cm. |
| TC03 | Normal | Segitiga, alas = 4 cm dan tinggi = 3 cm, pilih luas. | Luas = 6 cm². |
| TC04 | Normal | Segitiga, panjang sisi = 3 cm, 4 cm, dan 5 cm, pilih keliling. | Keliling = 12 cm. |
| TC05 | Normal | Lingkaran, jari-jari = 7 cm, pilih luas dan keliling dengan π = 3,14. | Luas = 153,86 cm² dan keliling = 43,96 cm. |
| TC06 | Batas | Persegi, sisi = 0,5 cm. | Input diterima dan luas = 0,25 cm² serta keliling = 2 cm. |
| TC07 | Tidak valid | Ukuran berupa angka 0 atau -5. | Input ditolak dan program meminta ukuran yang valid. |
| TC08 | Tidak valid | Ukuran dimasukkan menggunakan teks `abc`. | Program menampilkan pesan kesalahan dan meminta input ulang. |
| TC09 | Tidak valid | Panjang sisi segitiga = 2 cm, 3 cm, dan 6 cm. | Input sisi ditolak karena tidak memenuhi syarat pembentukan segitiga. |
| TC10 | Tidak valid | Pengguna memasukkan pilihan menu yang tidak tersedia. | Program menampilkan pesan bahwa pilihan tidak valid. |
| TC11 | Normal | Pengguna memilih menu riwayat setelah melakukan perhitungan. | Riwayat perhitungan yang tersimpan ditampilkan. |
| TC12 | Batas | Pengguna memilih menu riwayat saat belum ada perhitungan tersimpan. | Program menampilkan pesan bahwa riwayat masih kosong. |

## 11. Pembagian Tugas
Proyek ini direncanakan sebagai proyek individu. Seluruh bagian dikerjakan oleh satu orang dengan tanggung jawab yang dibagi berdasarkan fungsi pekerjaan agar proses pengembangan lebih terarah.

| Peran | PIC | Tanggung Jawab | Bukti Pekerjaan |
|---|---|---|---|
| Perancang/Koordinator | Nayla Solahiyah | Menentukan masalah, kebutuhan, ruang lingkup, dan alur program. | `proposal.md` |
| Programmer Logika | Nayla Solahiyah | Membuat fungsi perhitungan luas dan keliling bangun datar. | `src/geometri.py` |
| Programmer Validasi dan Data I/O | Nayla Solahiyah | Memeriksa input serta membuat fitur penyimpanan dan pembacaan riwayat. | `src/validasi.py` dan `src/data_io.py` |
| Integrator Program | Nayla Solahiyah | Menghubungkan seluruh fungsi melalui menu utama. | `src/main.py` |
| Tester | Nayla Solahiyah | Menjalankan test case, mencatat kesalahan, dan memperbaiki program. | `tests/test_case.md` |
| Dokumentasi | Nayla Solahiyah | Menyusun petunjuk penggunaan dan memperbarui dokumentasi proyek. | `README.md` |

Seluruh bagian akan diuji kembali setelah digabungkan untuk memastikan setiap fitur berjalan sesuai kebutuhan.

## 12. Jadwal Pelaksanaan
| Waktu | Kegiatan | Target |
|---|---|---|
| Pertemuan 14 | Menentukan masalah, pengguna, tujuan, ruang lingkup, kebutuhan, IPO, pseudocode, struktur program, struktur data, dan test case. Membuat repository GitHub dan mengunggah proposal. | Proposal dan struktur repository tersedia serta sudah di-commit. |
| Antara Pertemuan 14–15 | Membuat fungsi perhitungan, validasi input, menu utama, dan penyimpanan riwayat. | Implementasi awal fitur wajib tersedia. |
| Pertemuan 15 | Mengintegrasikan modul, menjalankan test case, memperbaiki kesalahan, dan melengkapi dokumentasi. | Program berjalan dan hasil pengujian tercatat. |
| Pertemuan 16 | Menyiapkan presentasi, demonstrasi program, penjelasan kode, dan evaluasi hasil proyek. | Proyek siap dipresentasikan dan didemonstrasikan. |

## 13. Repository
Repository proyek akan menggunakan nama:

`kalkulator-geometri-smp`

Repository digunakan untuk menyimpan proposal, kode program, test case, dokumentasi, dan riwayat perkembangan proyek melalui commit Git.

**URL Repository GitHub:**  
`https://github.com/NaylaSolahiyah2225250045/proyek-akhir-Nayla-Solahiyah-2225250045.git`

Repository akan berisi file `proposal.md`, `README.md`, struktur folder program, dan file pendukung sesuai rancangan. Perubahan akan dicatat melalui commit secara bertahap agar proses pengembangan dapat ditelusuri.

## Penutup
Program Kalkulator Luas dan Keliling Bangun Datar Berbasis Python untuk Siswa SMP Kelas VII dirancang sebagai alat bantu belajar yang sederhana dan mudah digunakan. Program ini diharapkan membantu siswa memahami rumus serta langkah perhitungan luas dan keliling bangun datar melalui tampilan menu, hasil perhitungan, validasi input, dan riwayat perhitungan.
Pelaksanaan proyek akan mengikuti ruang lingkup, kebutuhan, dan test case yang telah dirancang. Pada tahap berikutnya, program akan diimplementasikan, diuji, diperbaiki, dan didokumentasikan sebelum dipresentasikan pada Pertemuan 16.