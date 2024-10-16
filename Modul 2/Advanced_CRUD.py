admin_account = ("admin", "admin")
users = {}
courses = []

def register(users, nim, password, nama):
    if nim in users:
        return "NIM sudah terdaftar, silahkan login.", users
    
    users[nim] = {"password": password, "nama": nama, "courses": []}
    return f"Registrasi berhasil untuk User NIM {nim}", users

def login(users, nim, password, admin_account):
    if nim == admin_account[0] and password == admin_account[1]:
        return "Login berhasil! Selamat datang, Admin", "admin"
    elif nim in users and users[nim]["password"] == password:
        return f"Login berhasil! Selamat datang, {users[nim]['nama']}", nim
    else:
        return "NIM atau password salah!", None

def tambah_kursus(courses, id_kursus, nama_kursus, instruktur, durasi):
    if any(kursus[0] == id_kursus for kursus in courses):
        return "Kursus dengan ID tersebut sudah ada.", courses

    new_course = [id_kursus, nama_kursus, instruktur, durasi]
    courses.append(new_course)
    return f"Kursus '{nama_kursus}' berhasil ditambahkan!", courses

def lihat_kursus(courses):
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
            if nama_kursus:
                kursus[1] = nama_kursus
            if instruktur:
                kursus[2] = instruktur
            if durasi:
                kursus[3] = int(durasi)
            return f"Kursus dengan ID '{id_kursus}' berhasil diperbarui!", courses
    return "Kursus tidak ditemukan.", courses

def hapus_kursus(courses, id_kursus):
    new_courses = [kursus for kursus in courses if kursus[0] != id_kursus]
    if len(new_courses) < len(courses):
        return f"Kursus dengan ID '{id_kursus}' berhasil dihapus!", new_courses
    return "Kursus tidak ditemukan.", courses

def ambil_kursus(users, nim, courses, id_kursus):
    for kursus in courses:
        if kursus[0] == id_kursus:
            if id_kursus in users[nim]["courses"]:
                return f"Kursus '{kursus[1]}' sudah pernah Anda ambil sebelumnya.", users
            else:
                users[nim]["courses"].append(id_kursus)
                return f"Kursus '{kursus[1]}' berhasil diambil!", users
    return "Kursus tidak ditemukan.", users

def lihat_kursus_diambil(users, nim, courses):
    if users[nim]["courses"]:
        return "\n".join(
            f"- {kursus[1]} (Instruktur: {kursus[2]}, Durasi: {kursus[3]} jam)"
            for id_kursus in users[nim]["courses"]
            for kursus in courses if kursus[0] == id_kursus
        )
    else:
        return "Anda belum mengambil kursus apapun."

def admin_menu(courses, action, *args):
    if action == "lihat":
        return lihat_kursus(courses)
    elif action == "tambah":
        return tambah_kursus(courses, *args)
    elif action == "edit":
        return edit_kursus(courses, *args)
    elif action == "hapus":
        return hapus_kursus(courses, args[0])

def user_menu(users, nim, courses, action, *args):
    if action == "lihat":
        return lihat_kursus(courses)
    elif action == "ambil":
        return ambil_kursus(users, nim, courses, *args)
    elif action == "lihat_diambil":
        return lihat_kursus_diambil(users, nim, courses)

def main_menu():
    print("Selamat datang di sistem kursus!")
    while True:
        print("\nMenu Utama:")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nim = input("Masukkan NIM: ")
            password = input("Masukkan Password: ")
            nama = input("Masukkan Nama: ")
            msg, _ = register(users, nim, password, nama)
            print(msg)

        elif pilihan == "2":
            nim = input("Masukkan NIM: ")
            password = input("Masukkan Password: ")
            msg, login_status = login(users, nim, password, admin_account)
            print(msg)
            if login_status == "admin":
                while True:
                    print("\nMenu Admin:")
                    print("1. Tambah Kursus")
                    print("2. Lihat Kursus")
                    print("3. Logout")
                    admin_pilihan = input("Pilih opsi: ")

                    if admin_pilihan == "1":
                        id_kursus = input("ID Kursus: ")
                        nama_kursus = input("Nama Kursus: ")
                        instruktur = input("Instruktur: ")
                        durasi = int(input("Durasi (jam): "))
                        msg, _ = tambah_kursus(courses, id_kursus, nama_kursus, instruktur, durasi)
                        print(msg)

                    elif admin_pilihan == "2":
                        print(lihat_kursus(courses))

                    elif admin_pilihan == "3":
                        print("Logout berhasil.")
                        break

            elif login_status:
                while True:
                    print("\nMenu User:")
                    print("1. Lihat Kursus")
                    print("2. Ambil Kursus")
                    print("3. Lihat Kursus yang Diambil")
                    print("4. Logout")
                    user_pilihan = input("Pilih opsi: ")

                    if user_pilihan == "1":
                        print(lihat_kursus(courses))

                    elif user_pilihan == "2":
                        id_kursus = input("Masukkan ID Kursus: ")
                        msg, _ = ambil_kursus(users, nim, courses, id_kursus)
                        print(msg)

                    elif user_pilihan == "3":
                        print(lihat_kursus_diambil(users, nim, courses))

                    elif user_pilihan == "4":
                        print("Logout berhasil.")
                        break

        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem kursus!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

    
main_menu()
