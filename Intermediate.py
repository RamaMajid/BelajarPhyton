users = {}
profiles = {}
friends_list = {} 


def register():
    nim = input("Masukkan NIM: ")
    if nim in users:
        print("NIM sudah terdaftar, silahkan login.")
        return
    password = input("Masukkan password: ")
    users[nim] = password
    
    profiles[nim] = {}
    friends_list[nim] = []
    
    print(f"Registrasi berhasil untuk NIM {nim}")
    pilihan = input("Apakah Anda ingin mengisi profil dan teman sekarang? (y/n): ").lower()
    if pilihan == "y":
        isi_profil(nim)
        isi_friends_list(nim)
    else:
        print("Anda bisa mengisi profil dan teman pada menu user.")



def login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")

    if nim in users and users[nim] == password:
        if nim in profiles and "nama" in profiles[nim]:
            nama_pengguna = profiles[nim]["nama"]
            print(f"Login berhasil! Selamat datang, {nama_pengguna}")
        else:
            print(f"Login berhasil! Selamat datang, {nim}")
        
        user_menu(nim)
    else:
        print("NIM atau password salah!")



def isi_profil(nim):
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    umur = input("Masukkan umur: ")
    profiles[nim] = {"nama": nama, "alamat": alamat, "umur": umur}
    print("Profil berhasil disimpan!")


def isi_friends_list(nim):
    if nim not in friends_list:
        friends_list[nim] = []
    
    while True:
        teman = input("Masukkan nama teman (ketik 'done' untuk selesai): ")
        if teman.lower() == 'done':
            break
        friends_list[nim].append(teman)
    print("List teman berhasil diperbarui!")


def lihat_profil(nim):
    print("\n--- Profil Anda ---")
    if nim in profiles:
        for key, value in profiles[nim].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Profil belum diisi.")

    print("\n--- Daftar Teman Anda ---")
    if nim in friends_list:
        for teman in friends_list[nim]:
            print(f"- {teman}")
    else:
        print("Anda belum menambahkan teman.")


def edit_profil(nim):
    isi_profil(nim)



def edit_friends_list(nim):
    if nim in friends_list:
        isi_friends_list(nim)
    else:
        print("Anda belum menambahkan teman.")


def hapus_data(nim):
    pilihan = input("Apa yang ingin Anda hapus? (profil/teman): ").lower()
    if pilihan == "profil":
        if nim in profiles:
            del profiles[nim]
            print("Profil berhasil dihapus.")
        else:
            print("Profil tidak ditemukan.")
    elif pilihan == "teman":
        if nim in friends_list:
            del friends_list[nim]
            print("List teman berhasil dihapus.")
        else:
            print("Daftar teman tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")


def user_menu(nim):
    while True:
        print("\n--- User Menu ---")
        print("1. Lihat Profil dan Daftar Teman")
        print("2. Tambah/Edit Profil")
        print("3. Tambah/Edit Daftar Teman")
        print("4. Hapus Profil atau Daftar Teman")
        print("5. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_profil(nim)
        elif pilihan == "2":
            edit_profil(nim)
        elif pilihan == "3":
            edit_friends_list(nim)
        elif pilihan == "4":
            hapus_data(nim)
        elif pilihan == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
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
