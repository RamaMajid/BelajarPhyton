nilai = [ 
    {'matkul': 'Fungsional', 'nilai': 95},
    {'matkul': 'Mobile', 'nilai': 55} 
]

def tambah_nilai(nilai, nama_matkul, jumlah_nilai):
    nilai_baru = []
    for item in nilai:
        if item['matkul'] == nama_matkul:
            item_baru = item.copy()
            item_baru['nilai'] += jumlah_nilai
            nilai_baru.append(item_baru)
        else:
            nilai_baru.append(item)
    return nilai_baru


def cetak_nilai(nilai, nim):
    for item in nilai:
        yield f"NIM {nim}: Mata kuliah {item['matkul']} memiliki nilai {item['nilai']}"

nilai_update = tambah_nilai(nilai, 'Mobile', 15)


print("Nilai awal:", nilai)
print("Nilai update:", nilai_update)

nim_genap = 1037052

print(f"Nilai untuk NIM {nim_genap}:")
generator_nilai = cetak_nilai(nilai_update, nim_genap)

try:
    while True:
        print(next(generator_nilai))
except StopIteration:
    pass