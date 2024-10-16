admin_account = ("admin", "admin")
users = {}
courses = []

def register(users, nim, password, nama):
    if nim in users:
        return "NIM sudah terdaftar, silahkan login."
    
    password = input("Masukkan password: ")
    nama = input("Masukkan nama Anda: ")
    
    users[nim] = {"password": password, "nama": nama, "courses": []}
    return f"Registrasi berhasil untuk User NIM {nim}"

def login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")

    if nim == admin_account[0] and password == admin_account[1]:
        admin_menu()
        return f"Login berhasil! Selamat datang, Admin"
    elif nim in users and users[nim]["password"] == password:
        user_menu(nim)
        return f"Login berhasil! Selamat datang, {users[nim]['nama']}"
    else:
        return "NIM atau password salah!"

def tambah_kursus():
    id_kursus = input("Masukkan ID Kursus: ")
    if any(kursus[0] == id_kursus for kursus in courses):
        return "Kursus dengan ID tersebut sudah ada."

    nama_kursus = input("Masukkan nama kursus: ")
    instruktur = input("Masukkan nama instruktur: ")
    durasi = int(input("Masukkan durasi kursus (dalam jam): "))
    courses.append([id_kursus, nama_kursus, instruktur, durasi])
    return f"Kursus '{nama_kursus}' berhasil ditambahkan!"

def lihat_kursus():
    if courses:
        return "\n".join(
            f"ID Kursus: {kursus[0]}\n  Nama Kursus: {kursus[1]}\n  Instruktur: {kursus[2]}\n  Durasi: {kursus[3]} jam"
            for kursus in courses
        )
    else:
        return "Belum ada kursus yang ditambahkan."

def edit_kursus(courses, id_kursus, nama_kursus=None, instruktur=None, durasi=None):
    for kursus in courses:
        if kursus[0] == id_kursus:
            nama_kursus = input("Nama Kursus baru: ")
            instruktur = input("Instruktur baru: ")
            durasi = input("Durasi baru (dalam jam): ")

            if nama_kursus:
                kursus[1] = nama_kursus
            if instruktur:
                kursus[2] = instruktur
            if durasi:
                kursus[3] = int(durasi)

            return f"Kursus dengan ID '{id_kursus}' berhasil diperbarui!"
    return "Kursus tidak ditemukan."

def hapus_kursus():
    id_kursus = input("Masukkan ID Kursus yang ingin dihapus: ")
    for kursus in courses:
        if kursus[0] == id_kursus:
            courses.remove(kursus)
            return f"Kursus dengan ID '{id_kursus}' berhasil dihapus!"
    return "Kursus tidak ditemukan."

def ambil_kursus(nim):
    id_kursus = input("Masukkan ID Kursus yang ingin diambil: ")
    for kursus in courses:
        if kursus[0] == id_kursus:
            if id_kursus in users[nim]["courses"]:
                return f"Kursus '{kursus[1]}' sudah pernah Anda ambil sebelumnya."
            else:
                users[nim]["courses"].append(id_kursus)
                return f"Kursus '{kursus[1]}' berhasil diambil!"
    return "Kursus tidak ditemukan."

def lihat_kursus_diambil(nim):
    if users[nim]["courses"]:
        return "\n".join(
            f"- {kursus[1]} (Instruktur: {kursus[2]}, Durasi: {kursus[3]} jam)"
            for id_kursus in users[nim]["courses"]
            for kursus in courses if kursus[0] == id_kursus
        )
    else:
        return "Anda belum mengambil kursus apapun."

def admin_menu():
    while True:
        pilihan = input("\n--- Admin Menu ---\n1. Lihat Kursus\n2. Tambah Kursus\n3. Edit Kursus\n4. Hapus Kursus\n5. Logout\nPilih menu: ")
        if pilihan == "1":
            print(lihat_kursus())
        elif pilihan == "2":
            print(tambah_kursus())
        elif pilihan == "3":
            print(edit_kursus())
        elif pilihan == "4":
            print(hapus_kursus())
        elif pilihan == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

def user_menu(nim):
    while True:
        pilihan = input("\n--- User Menu ---\n1. Lihat Kursus\n2. Ambil Kursus\n3. Lihat Kursus yang Diambil\n4. Logout\nPilih menu: ")
        if pilihan == "1":
            print(lihat_kursus())
        elif pilihan == "2":
            print(ambil_kursus(nim))
        elif pilihan == "3":
            print(lihat_kursus_diambil(nim))
        elif pilihan == "4":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")

def main_menu():
    while True:
        pilihan = input("\n--- Main Menu ---\n1. Register User\n2. Login\n3. Keluar\nPilih menu: ")
        if pilihan == "1":
            print(register())
        elif pilihan == "2":
            print(login())
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid!")

main_menu()
