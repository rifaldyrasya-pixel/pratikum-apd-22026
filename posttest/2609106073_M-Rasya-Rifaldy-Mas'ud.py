import os

users = {
    "rasya": {"pin": "073", "role": "admin"},
    "smk": {"pin": "123", "role": "user"}
}
antrean_servis = {}
id_counter = 1

def cetak_header(teks_judul):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print(f"       {teks_judul}          ")
    print("==========================================")

def tampilkan_daftar():
    cetak_header("DAFTAR ANTREAN SERVIS BENGKEL")
    if len(antrean_servis) == 0:
        print("Belum ada antrean motor saat ini.")
    else:
        for key_id, val in antrean_servis.items():
            print(f"ID [{key_id}] | [{val['status']}] {val['nama']} - {val['merk']} ({val['plat']}) | Keluhan: {val['keluhan']}")

def get_total_users():
    total = len(users)
    return total

def validasi_login(input_user, input_pin):
    data_user = users.get(input_user)
    if data_user and data_user["pin"] == input_pin:
        return data_user["role"]
    return None

def hitung_antrean_rekursif(daftar_id):
    if not daftar_id:
        return 0
    return 1 + hitung_antrean_rekursif(daftar_id[1:])

while True:
    user_login = ""
    role_login = ""

    while True:
        cetak_header("MOTOCARE MANAGER - LOGIN")
        print("1. Login Akun")
        print("2. Register Akun Baru")
        print("3. Keluar Program")
        print(f"Info: Total Akun Terdaftar = {get_total_users()}")
        print("==========================================")
        
        try:
            pilihan_auth = int(input("Pilih menu (1-3): "))
        except ValueError:
            print("\n>> Error: Masukkan angka yang valid (1-3)!")
            input("Tekan Enter untuk melanjutkan...")
            continue

        if pilihan_auth == 1:
            cetak_header("SILAHKAN LOGIN")
            lokal_user = input("Masukkan Username : ")
            lokal_pin = input("Masukkan PIN      : ")
            
            hasil_role = validasi_login(lokal_user, lokal_pin)
            if hasil_role:
                user_login = lokal_user
                role_login = hasil_role
                print(f"\n>> Login Berhasil! Selamat datang, {user_login} ({role_login}).")
                input("Tekan Enter untuk masuk ke menu utama...")
                break
            else:
                print("\n>> Username atau PIN salah!")
                input("Tekan Enter untuk melanjutkan...")

        elif pilihan_auth == 2:
            cetak_header("REGISTER AKUN BARU")
            reg_user = input("Buat Username baru : ")
            if reg_user in users:
                print(">> Username tersebut sudah digunakan!")
            else:
                reg_pin = input("Buat PIN baru      : ")
                users[reg_user] = {"pin": reg_pin, "role": "user"}
                print(">> Akun berhasil didaftarkan!")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan_auth == 3:
            cetak_header("PROGRAM DIHENTIKAN")
            print("Terima kasih telah menggunakan program!")
            exit()
        else:
            print("\n>> Pilihan tidak ada di menu.")
            input("Tekan Enter untuk melanjutkan...")

    while True:
        cetak_header(f"BENGKEL MOTOCARE [User: {user_login}]")
        print("1. Lihat Daftar Antrean (Read)")
        if role_login == "admin":
            print("2. Tambah Antrean Motor (Create)")
            print("3. Update Status Pengerjaan (Update)")
            print("4. Motor Selesai / Hapus Antrean (Delete)")
        print("5. Logout / Ganti Akun")
        print("6. Keluar Program")
        print("==========================================")

        try:
            pilihan_menu = int(input("Pilih menu: "))
        except ValueError:
            print("\n>> Error: Harap masukkan angka menu!")
            input("Tekan Enter untuk melanjutkan...")
            continue

        if pilihan_menu == 1:
            tampilkan_daftar()
            jumlah_rekursif = hitung_antrean_rekursif(list(antrean_servis.keys()))
            print(f"\n[Info Rekursif] Total antrean aktif saat ini: {jumlah_rekursif} motor.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == 2 and role_login == "admin":
            cetak_header("TAMBAH ANTREAN MOTOR BARU")
            lokal_nama = input("Nama pemilik  : ")
            lokal_plat = input("Plat nomor    : ")
            lokal_merk = input("Merk motor    : ")
            lokal_keluhan = input("Keluhan       : ")

            str_id = str(id_counter)
            antrean_servis[str_id] = {
                "nama": lokal_nama,
                "plat": lokal_plat,
                "merk": lokal_merk,
                "keluhan": lokal_keluhan,
                "status": "Antri"
            }
            id_counter += 1
            print("\n>> Data antrean motor berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == 3 and role_login == "admin":
            tampilkan_daftar()
            if len(antrean_servis) > 0:
                pilih_id = input("\nMasukkan ID antrean yang mau diubah: ")
                if pilih_id in antrean_servis:
                    print(f"Status sekarang: {antrean_servis[pilih_id]['status']}")
                    print("1. Dikerjakan")
                    print("2. Selesai")
                    st = input("Pilih status baru (1/2): ")
                    if st == "1":
                        antrean_servis[pilih_id]["status"] = "Dikerjakan"
                        print(">> Status diubah jadi 'Dikerjakan'")
                    elif st == "2":
                        antrean_servis[pilih_id]["status"] = "Selesai"
                        print(">> Status diubah jadi 'Selesai'")
                    else:
                        print(">> Pilihan tidak valid.")
                else:
                    print(">> ID tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == 4 and role_login == "admin":
            tampilkan_daftar()
            if len(antrean_servis) > 0:
                pilih_id = input("\nMasukkan ID antrean yang ingin dihapus: ")
                if pilih_id in antrean_servis:
                    data_hapus = antrean_servis.pop(pilih_id)
                    print(f">> Data motor {data_hapus['merk']} milik {data_hapus['nama']} dihapus.")
                else:
                    print(">> ID tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == 5:
            print("\n>> Berhasil Logout.")
            input("Tekan Enter untuk kembali...")
            break

        elif pilihan_menu == 6:
            cetak_header("TERIMA KASIH")
            exit()
        else:
            print("\n>> Pilihan tidak valid atau akses ditolak.")
            input("Tekan Enter untuk melanjutkan...")