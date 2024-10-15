data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63}
]

# Nim Genap
nim_akhir = 1037052

def ambil_nilai(mahasiswa):
    return mahasiswa['nilai']

# Fungsi a: Menghitung rata-rata nilai mahasiswa
def rata_rata(data_mahasiswa):
    nilai_mahasiswa = list(map(ambil_nilai, data_mahasiswa))
    return sum(nilai_mahasiswa) / len(nilai_mahasiswa)

def status_kelulusan(nilai):
    if nilai >= 85:
        return 'sempurna'
    elif nilai >= 60:
        return 'memenuhi'
    else:
        return 'gagal'

# Fungsi untuk mengelompokkan kelulusan tiap mahasiswa
def proses_kelulusan(mahasiswa):
    mahasiswa_baru = mahasiswa.copy()
    mahasiswa_baru['status_kelulusan'] = status_kelulusan(mahasiswa['nilai'])
    return mahasiswa_baru

# Fungsi b: Mengelompokkan kelulusan
def kelulusan(data_mahasiswa):
    return list(map(proses_kelulusan, data_mahasiswa))

# Fungsi c: Generator untuk mencetak nilai sesuai NIM akhir
def cetak_nilai(data_mahasiswa, nim_akhir):
    for item in data_mahasiswa:
        if nim_akhir % 2 == 0 and item['nilai'] % 2 == 0:
            yield f"{item['nama']} mendapatkan nilai {item['nilai']} di mata kuliah {item['matkul']}"

print("Rata-rata nilai mahasiswa:", rata_rata(data_mahasiswa))

hasil_kelulusan = kelulusan(data_mahasiswa)
print("Hasil kelulusan mahasiswa:")
for mahasiswa in hasil_kelulusan:
    print(f"{mahasiswa['nama']} - Status: {mahasiswa['status_kelulusan']}")


print(f"Nilai yang sesuai dengan NIM akhir {nim_akhir}:")
generator_nilai = cetak_nilai(hasil_kelulusan, nim_akhir)

try:
    while True:
        print(next(generator_nilai))
except StopIteration:
    pass