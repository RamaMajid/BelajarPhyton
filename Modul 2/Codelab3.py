tanggal_lahir = int(input("Masukkan tanggal lahir : "))

kelipatan_generator = (i for i in range(1000) if i % tanggal_lahir == 0)

hasil_kelipatan = list(kelipatan_generator)[:10]

print("10 data pertama kelipatan dari tanggal lahir:")
print(hasil_kelipatan)