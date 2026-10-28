"""
Modul Analisis Geometri
Berisi fungsi perhitungan luas, keliling, dan langkah penyelesaian
bangun datar.
"""

PI = 3.14

def hitung_persegi(sisi):
    """Menghitung luas dan keliling persegi."""
    luas = sisi * sisi
    keliling = 4 * sisi

    langkah_luas = (
        f"Rumus Luas = sisi × sisi\n"
        f"           = {sisi:g} × {sisi:g}\n"
        f"           = {luas:g} cm²"
    )

    langkah_keliling = (
        f"Rumus Keliling = 4 × sisi\n"
        f"               = 4 × {sisi:g}\n"
        f"               = {keliling:g} cm"
    )

    return luas, keliling, langkah_luas, langkah_keliling

def hitung_persegi_panjang(panjang, lebar):
    """Menghitung luas dan keliling persegi panjang."""
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    langkah_luas = (
        f"Rumus Luas = panjang × lebar\n"
        f"           = {panjang:g} × {lebar:g}\n"
        f"           = {luas:g} cm²"
    )

    langkah_keliling = (
        f"Rumus Keliling = 2 × (panjang + lebar)\n"
        f"               = 2 × ({panjang:g} + {lebar:g})\n"
        f"               = {keliling:g} cm"
    )

    return luas, keliling, langkah_luas, langkah_keliling

def hitung_segitiga(alas, tinggi, s1=0, s2=0, s3=0):
    """Menghitung luas dan keliling segitiga."""
    luas = 0.5 * alas * tinggi
    keliling = s1 + s2 + s3

    langkah_luas = (
        f"Rumus Luas = ½ × alas × tinggi\n"
        f"           = ½ × {alas:g} × {tinggi:g}\n"
        f"           = {luas:g} cm²"
    )

    langkah_keliling = (
        f"Rumus Keliling = sisi 1 + sisi 2 + sisi 3\n"
        f"               = {s1:g} + {s2:g} + {s3:g}\n"
        f"               = {keliling:g} cm"
    )

    return luas, keliling, langkah_luas, langkah_keliling

def hitung_lingkaran(r):
    """Menghitung luas dan keliling lingkaran dengan pi = 3.14."""
    luas = PI * r * r
    keliling = 2 * PI * r

    langkah_luas = (
        f"Rumus Luas = π × r × r\n"
        f"           = 3.14 × {r:g} × {r:g}\n"
        f"           = {luas:.2f} cm²"
    )

    langkah_keliling = (
        f"Rumus Keliling = 2 × π × r\n"
        f"               = 2 × 3.14 × {r:g}\n"
        f"               = {keliling:.2f} cm"
    )

    return luas, keliling, langkah_luas, langkah_keliling