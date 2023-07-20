from anggota import tampilkan_anggota, cari_anggota_by_id, tambah_anggota, edit_anggota, clear
from TabunganSampah import tambah_tabungan, tarik_tabungan, tampilkan_tabungan
from Tambahan_8A import bubble_sort, anggota_list
from Tambahan_8B import data_transaksi

# Program utama
def main():
    while True:
        clear()
        print("="*41)
        print("** Program Pengelolaan Tabungan Sampah **")
        print("="*41)
        print("Pilihan menu:")
        print("1. Pengelolaan Keanggotaan")
        print("   1a. Penambahan Data Anggota")
        print("   1b. Pencarian Data Anggota")
        print("   1c. Pengubahan Data Anggota")
        print("2. Pengelolaan Tabungan Anggota")
        print("   2a. Penambahan Tabungan")
        print("   2b. Penarikan Tabungan")
        print("   2c. Menampilkan Data Tabungan")
        print("3. Urutan Data Anggota")
        print("4. Pelaporan Transaksi")
        print("0. Exit")
        print("="*41)
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1a":
            clear()
            print("="*25)
            print("Penambahan Data Anggota")
            print("="*25)
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            telepon = input("Telepon: ")
            tambah_anggota(nama=nama, alamat=alamat, telepon=telepon)

        elif pilihan == "1b":
            clear()
            print("="*25)
            print("Pencarian Data Anggota")
            print("="*25)
            idanggota = input("Masukkan ID Anggota: ")
            data_anggota = cari_anggota_by_id(idanggota)               
            if data_anggota:
                print(data_anggota)
            else:
                print("{}")
            tampilkan_anggota(data_anggota)
            input("Tekan tombol ENTER untuk kembali ke menu utama")

        elif pilihan == "1c":
            clear()
            print("="*25)
            print("Pengubahan Data Anggota")
            print("="*25)
            edit_anggota()
            input("Tekan tombol ENTER untuk kembali ke menu utama")

        elif pilihan == "2a":
            print("="*25)
            print("Penambahan Tabungan Sampah.")
            print("="*25)
            idanggota = input("Input ID Anggota : ")

            # Mencari data anggota berdasarkan ID Anggota
            data_anggota = cari_anggota_by_id(idanggota)

            if not data_anggota:
                print("Data anggota tidak ditemukan!")
                pilihan = input("Cari lagi (Y/y = Ya, T/t = Tidak)? ")
                if pilihan.lower() == 'y':
                    main()
                return

            # Menambah data transaksi tabungan sampah
            tambah_tabungan(idanggota)   
                
        elif pilihan == "2b":
            clear()
            print("="*25)
            print("Penarikan Tabungan Sampah")
            print("="*25)
            idanggota = input("Input ID Anggota : ")
            tarik_tabungan(idanggota)
            pilihan = input("Apakah ingin melakukan penarikan lagi? (Y/y = Ya, T/t = Tidak)? ")
            if pilihan.lower() == 'y':
                tarik_tabungan(idanggota)
            else:
                main()

        elif pilihan == "2c":
            clear()
            print("="*25)
            print("Menampilkan Data Tabungan.")
            print("="*25)
            idanggota = input("Input ID Anggota : ")
            tampilkan_tabungan(idanggota)
            input("Tekan tombol ENTER untuk melanjutkan...")
        
        elif pilihan == "3" :
            clear()
            print("="*25)
            print("Data Anggota Terurut:")
            print("="*25)
            bubble_sort(anggota_list)
            for anggota in anggota_list:
                print(f"ID      : {anggota['idanggota']}")
                print(f"Nama    : {anggota['nama']}")
                print(f"Alamat  : {anggota['alamat']}")
                print(f"Tanggal : {anggota['tanggal']}")
                print(f"Telepon : {anggota['telepon']}\n")
            input("Tekan tombol ENTER untuk melanjutkan...")

        elif pilihan == "4" :
            clear()
            print("="*25)
            print("Pelaporan Transaksi")
            print("="*25)
            idanggota = input("Masukkan ID Anggota: ")
            data_transaksi(idanggota)
            input("Tekan tombol ENTER untuk melanjutkan...")


        elif pilihan == "0":
            clear()
            print("="*50)
            print("Terima kasih telah menggunakan program ini")
            print("="*50)
            exit()

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
            input("Tekan tombol ENTER untuk melanjutkan...")

if __name__ == '__main__':
    main()

