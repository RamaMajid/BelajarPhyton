from datetime import datetime
from functools import reduce

data_penjualan = [
    {"id_produk": "GN123", "nama_produk": "Rak Sepatu", "harga": 50000, "quantity": 3, "tanggal": "2024-10-01"},
    {"id_produk": "GN456", "nama_produk": "Sepatu", "harga": 100000, "quantity": 1, "tanggal": "2024-10-01"},
    {"id_produk": "GN789", "nama_produk": "Baju", "harga": 75000, "quantity": 2, "tanggal": "2024-10-01"},
    {"id_produk": "GN321", "nama_produk": "Celana", "harga": 30000, "quantity": 4, "tanggal": "2024-10-02"},
    {"id_produk": "GN654", "nama_produk": "Gantungan Kunci", "harga": 120000, "quantity": 2, "tanggal": "2024-10-02"},
    {"id_produk": "GN987", "nama_produk": "Jam Tangan", "harga": 20000, "quantity": 6, "tanggal": "2024-10-02"},
    {"id_produk": "GN213", "nama_produk": "Jilbab", "harga": 45000, "quantity": 3, "tanggal": "2024-10-03"},
    {"id_produk": "GN546", "nama_produk": "Sunscreen", "harga": 110000, "quantity": 1, "tanggal": "2024-10-03"},
    {"id_produk": "GN879", "nama_produk": "Tas", "harga": 60000, "quantity": 4, "tanggal": "2024-10-03"},
    {"id_produk": "GN312", "nama_produk": "Jaket", "harga": 80000, "quantity": 2, "tanggal": "2024-10-04"},
    {"id_produk": "GN645", "nama_produk": "Parfum", "harga": 50000, "quantity": 5, "tanggal": "2024-10-04"},
    {"id_produk": "GN978", "nama_produk": "Koper", "harga": 150000, "quantity": 1, "tanggal": "2024-10-04"}
]


def hitung_pendapatan(data_penjualan):
    return list(map(lambda item: {**item, "total_pendapatan": item["harga"] * item["quantity"]}, data_penjualan))

# Fungsi deklaratif menggunakan filter dan reduce untuk total penjualan pada tanggal tertentu
def total_dan_rata_rata_penjualan_per_tanggal(data_penjualan, tanggal_input):
    penjualan_hari = list(filter(lambda item: item["tanggal"] == tanggal_input, data_penjualan))
    
    if not penjualan_hari:
        return None, None
    
    total_penjualan = reduce(lambda acc, item: acc + (item["harga"] * item["quantity"]), penjualan_hari, 0)
    total_quantity = reduce(lambda acc, item: acc + item["quantity"], penjualan_hari, 0)
    
    rata_rata_penjualan = total_penjualan / total_quantity if total_quantity > 0 else 0
    
    return total_penjualan, rata_rata_penjualan


# Generator yang tetap sesuai dengan paradigma deklaratif dan filter tanggal
def total_penjualan(data_hasil, tanggal_input):
    for item in filter(lambda i: i['tanggal'] == tanggal_input, data_hasil):
        yield {
            "tanggal": item['tanggal'],
            "produk": item['nama_produk'],
            "quantity": item['quantity'],
            "total_pendapatan": item['total_pendapatan']
        }

def main():
    # Menghitung total pendapatan dengan deklaratif (map)
    data_hasil = hitung_pendapatan(data_penjualan)
    
    print("Total pendapatan per produk:")
    for item in data_hasil:
        print(f"{item['nama_produk']} - Total Pendapatan: Rp {item['total_pendapatan']}")

    while True:
        tanggal_input = input("\nMasukkan tanggal (format YYYY-MM-DD) untuk melihat total penjualan (ketik 'q' untuk berhenti): ")
        
        if tanggal_input.lower() == 'q':
            print("Program dihentikan.")
            break
        
        total_penjualan_tanggal, rata_rata_penjualan = total_dan_rata_rata_penjualan_per_tanggal(data_penjualan, tanggal_input)
        
        if total_penjualan_tanggal is not None:
            print(f"\nTotal penjualan pada tanggal {tanggal_input}: Rp {total_penjualan_tanggal}")
            print(f"Rata-rata penjualan per produk pada tanggal {tanggal_input}: Rp {rata_rata_penjualan}")
        else:
            print(f"Tidak ada penjualan pada tanggal {tanggal_input}.")
        
        print(f"\n=== Detail Penjualan pada Tanggal {tanggal_input} ===")
        penjualan_ada = False
        for penjualan in total_penjualan(data_hasil, tanggal_input):
            print(f"Produk {penjualan['produk']} terjual sebanyak {penjualan['quantity']} unit dengan total pendapatan Rp {penjualan['total_pendapatan']}.")
            penjualan_ada = True

        if not penjualan_ada:
            print(f"Tidak ada data penjualan pada tanggal {tanggal_input}.")


main()
