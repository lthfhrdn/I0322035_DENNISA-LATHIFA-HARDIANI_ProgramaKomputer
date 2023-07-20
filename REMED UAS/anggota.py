import json
import random
import string
import datetime
import os

# Nomor 2.a => Fungsi untuk menambahkan anggota baru
def tambah_anggota(nama, alamat, telepon):
    with open('anggotas.json') as file:
        data = json.load(file)

    idanggota = str(random.randint(10000, 99999))

    anggota_tambahan = {
        idanggota: {
            "idanggota": idanggota,
            "nama": nama,
            "alamat": alamat,
            "tanggal": datetime.datetime.now().strftime('%Y-%m-%d'),
            "telepon": telepon
        }
    }
    data.update(anggota_tambahan)

    with open("anggotas.json", "w") as file:
        json.dump(data, file, indent=4)

    print("="*40)
    print("Berhasil Menambahkan Data Anggota.")
    print("="*40)
    bridge = input("Tekan tombol ENTER untuk kembali ke menu utama")
    if bridge == " ":
        pass

# Nomor 2.b => Fungsi untuk mencari anggota berdasarkan ID
def cari_anggota_by_id(idanggota):
    with open("anggotas.json") as file:
        data_anggota = json.load(file)

    if idanggota in data_anggota:
        return data_anggota[idanggota]
    else:
        return {}

# Nomor 2.c => Fungsi untuk menampilkan anggota yang telah dicari
def tampilkan_anggota(data):
    if data:
        print("ID Anggota   :", data['idanggota'])
        print("Nama         :", data['nama'])
        print("Alamat       :", data['alamat'])
        print("Telepon      :", data['telepon'])
        print("Tanggal Daftar:", data['tanggal'])
    else:
        print("Tidak Ada Data Anggota!")

# Nomor 2.d = > Fungsi untuk mengubah anggota
def edit_anggota():
    while True:
        print("Ketik ID anggota yang akan diedit:  ")
        idanggota = input()
        
        # Mencari dan Memperoleh Data
        data_anggota = cari_anggota_by_id(idanggota)
        
        if data_anggota:
            print("Nama       :", data_anggota['nama'])
            print("Alamat     :", data_anggota['alamat'])
            print("Telepon    :", data_anggota['telepon'])
            
            # Melakukan Pengubahan Data
            nama_baru = input("Nama       : (" + data_anggota['nama'] + ") -> ")
            alamat_baru = input("Alamat     : (" + data_anggota['alamat'] + ") -> ")
            telepon_baru = input("Telepon    : (" + data_anggota['telepon'] + ") -> ")
            
            # Memperbarui data anggota
            if nama_baru:
                data_anggota['nama'] = nama_baru
            if alamat_baru:
                data_anggota['alamat'] = alamat_baru
            if telepon_baru:
                data_anggota['telepon'] = telepon_baru
            
            # Menyimpan perubahan pada file anggotas.json
            with open('anggotas.json', 'w') as file:
                json.dump(data_anggota, file, indent=4)
            print("="*20)
            print("Data berhasil diubah.")
            print("="*20)
        else:
            print("Data anggota tidak ditemukan!")
        
        pilihan = input("Cari lagi? (Y/y = Ya, T/t = Tidak): ")
        if pilihan.lower() != 'y' or " ":
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menghasilkan ID anggota secara acak
def generate_idanggota():
    idanggota = ''.join(random.choices(string.digits, k=5))
    return idanggota

def clear():
    print("\033[H\033[J")


