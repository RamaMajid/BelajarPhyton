from functools import reduce

books = [
    {'judul':'Matematika', 'penulis': 'Febri', 'halaman': 50},
    {'judul':'Biologi', 'penulis': 'Anisa.', 'halaman': 254},
    {'judul':'Sosiologi', 'penulis': 'Faizal', 'halaman': 448},
    {'judul':'Kimia', 'penulis': 'Syulit', 'halaman': 157},
    {'judul':'Sejarah', 'penulis': 'Gayin', 'halaman': 600},
    {'judul':'PJOK', 'penulis': 'Atika', 'halaman': 254},
    {'judul':'Seni Budaya', 'penulis': 'Mel', 'halaman': 2000},
]

def filter_books(books):
    return [book for book in books if book['judul'].startswith('K')]

filtered_books = filter_books(books)

print("Buku yang judulnya diawali dengan huruf 'K':")
for book in filtered_books:
    print(f"Judul: {book['judul']}, Penulis: {book['penulis']}, Halaman: {book['halaman']}")
print()

# Membuat daftar yang berisi hanya judul buku saja menggunakan map
def judul_buku(book):
    return book['judul']

judul_buku_list = list(map(judul_buku, books))

print("Daftar judul buku:")
for judul in judul_buku_list:
    print(judul)
print()

# Filter halaman buku
def halaman(book):
    return book['halaman'] > 200

books_200 = list(filter(halaman, books))

print("Buku dengan halaman lebih dari 200:")
for book in books_200:
    print(f"Judul: {book['judul']}, Penulis: {book['penulis']}, Halaman: {book['halaman']}")
print()

# Menghitung total jumlah halaman semua buku
def hitung_halaman(total, book):
    return total + book['halaman']

total_halaman = reduce(hitung_halaman, books, 0)

print(f"Total jumlah halaman dari semua buku: {total_halaman}")
