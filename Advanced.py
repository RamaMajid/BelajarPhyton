admin_account = ("admin", "admin")
users = {}
courses = []

def register():
    nim = input("Masukkan NIM: ")
    if nim in users:
        print("NIM sudah terdaftar, silahkan login.")
        return
    password = input("Masukkan password: ")
    nama = input("Masukkan nama Anda: ")
    
    users[nim] = {"password": password, "nama": nama, "courses": []}
    print(f"Registrasi berhasil untuk User NIM {nim}")

def login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")

    if nim == admin_account[0] and password == admin_account[1]:
        print(f"Login berhasil! Selamat datang, Admin")
        admin_menu()
    elif nim in users and users[nim]["password"] == password:
        print(f"Login berhasil! Selamat datang, {users[nim]['nama']}")
        user_menu(nim)
    else:
        print("NIM atau password salah!")


def tambah_kursus():
    id_kursus = input("Masukkan ID Kursus: ")
    for kursus in courses:
        if kursus[0] == id_kursus:
            print("Kursus dengan ID tersebut sudah ada.")
            return

    nama_kursus = input("Masukkan nama kursus: ")
    instruktur = input("Masukkan nama instruktur: ")
    durasi = int(input("Masukkan durasi kursus (dalam jam): "))
    courses.append([id_kursus, nama_kursus, instruktur, durasi])
    print(f"Kursus '{nama_kursus}' berhasil ditambahkan!")


def lihat_kursus():
    if courses:
        print("Daftar Kursus:")
        for kursus in courses:
            print(f"ID Kursus: {kursus[0]}")
            print(f"  Nama Kursus: {kursus[1]}")
            print(f"  Instruktur: {kursus[2]}")
            print(f"  Durasi: {kursus[3]} jam")
    else:
        print("Belum ada kursus yang ditambahkan.")


def edit_kursus():
    id_kursus = input("Masukkan ID Kursus yang ingin diedit: ")
    for kursus in courses:
        if kursus[0] == id_kursus:
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
            nama_kursus = input("Nama Kursus baru: ")
            instruktur = input("Instruktur baru: ")
            durasi = input("Durasi baru (dalam jam): ")

            if nama_kursus:
                kursus[1] = nama_kursus
            if instruktur:
                kursus[2] = instruktur
            if durasi:
                kursus[3] = int(durasi)

            print(f"Kursus dengan ID '{id_kursus}' berhasil diperbarui!")
            return
    print("Kursus tidak ditemukan.")


def hapus_kursus():
    id_kursus = input("Masukkan ID Kursus yang ingin dihapus: ")
    for kursus in courses:
        if kursus[0] == id_kursus:
            courses.remove(kursus)
            print(f"Kursus dengan ID '{id_kursus}' berhasil dihapus!")
            return
    print("Kursus tidak ditemukan.")


def ambil_kursus(nim):
    id_kursus = input("Masukkan ID Kursus yang ingin diambil: ")
    for kursus in courses:
        if kursus[0] == id_kursus:
            if id_kursus in users[nim]["courses"]:
                print(f"Kursus '{kursus[1]}' sudah pernah Anda ambil sebelumnya.")
            else:
                users[nim]["courses"].append(id_kursus)
                print(f"Kursus '{kursus[1]}' berhasil diambil!")
            return
    print("Kursus tidak ditemukan.")


def lihat_kursus_diambil(nim):
    if users[nim]["courses"]:
        print(f"Kursus yang diambil oleh {users[nim]['nama']}:")
        for id_kursus in users[nim]["courses"]:
            for kursus in courses:
                if kursus[0] == id_kursus:
                    print(f"- {kursus[1]} (Instruktur: {kursus[2]}, Durasi: {kursus[3]} jam)")
    else:
        print("Anda belum mengambil kursus apapun.")


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Lihat Kursus")
        print("2. Tambah Kursus")
        print("3. Edit Kursus")
        print("4. Hapus Kursus")
        print("5. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_kursus()
        elif pilihan == "2":
            tambah_kursus()
        elif pilihan == "3":
            edit_kursus()
        elif pilihan == "4":
            hapus_kursus()
        elif pilihan == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")


def user_menu(nim):
    while True:
        print("\n--- User Menu ---")
        print("1. Lihat Kursus")
        print("2. Ambil Kursus")
        print("3. Lihat Kursus yang Diambil")
        print("4. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_kursus()
        elif pilihan == "2":
            ambil_kursus(nim)
        elif pilihan == "3":
            lihat_kursus_diambil(nim)
        elif pilihan == "4":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register User")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid!")


main_menu()
