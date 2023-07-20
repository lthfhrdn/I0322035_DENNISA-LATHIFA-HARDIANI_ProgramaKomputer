import json
import os
import datetime
import random
from anggota import cari_anggota_by_id


def generate_idtransaksi(idanggota): #Membuat ID dengan sytanx random 7 digit
    idtransaksi = "KK" + str(random.randint(10000, 99999))
    return idtransaksi

def cari_harga(idsampah): #Mencari harga satuan sampah dari kode yang diinputkan
    with open('produksampah.json') as file:
        data_sampah = json.load(file)
    for kode, sampah in data_sampah.items():
        if kode == idsampah:
            return float(sampah['hargasatuan'])
    return 0.0

def get_saldo(idanggota): #Mendapatkan saldo pada transaksi terakhir seorang anggota.
    with open(f'tabungan{idanggota}.json') as file:
        data_tabungan = json.load(file)
    if data_tabungan:
        return data_tabungan[-1]['saldo']
    return 0

def tambah_tabungan(idanggota): #Menambah data transaksi setoran sampah seorang anggota.
    filename = f'tabungan{idanggota}.json'

    if os.path.isfile(filename): # Memastikan data
        with open(filename) as file:
            data_tabungan = json.load(file)
    else:
        data_tabungan = []

    with open(filename, 'w') as file:
        json.dump(data_tabungan, file, indent=4)

    data_anggota = cari_anggota_by_id(idanggota) #Menampilkan data
    print(f"IDAnggota: {idanggota} | Nama : {data_anggota['nama']} | Telepon: {data_anggota['telepon']} | Alamat: {data_anggota['alamat']}")
    print("=============================================")
    print("Kode | Jenis Sampah       | Harga Satuan (Rp)")
    print("---------------------------------------------")
    print("1    | Kardus             | 500")
    print("2    | Botol plastic      | 300")
    print("3    | Logam besi         | 800")
    print("4    | Tembaga            | 950")
    print("---------------------------------------------")

    while True:
        # Meminta input kode sampah dan kuantitas sampah
        kode_sampah = input("Pilih jenis sampah (Masukkan Kode 1-4): ")
        kuantitas = float(input("Kuantitas sampah : "))

        # Cari harga satuan sampah dari kode sampah yang diinputkan
        hargasatuan = cari_harga(kode_sampah)

        if hargasatuan == 0:
            print("Kode sampah tidak valid. Silakan coba lagi.")
        else:
            break

    # Proses pembuatan data tabungan
    idtransaksi = generate_idtransaksi(idanggota)
    tanggal = datetime.datetime.now().strftime('%Y-%m-%d')
    tipetransaksi = "K"
    total = kuantitas * hargasatuan
    saldo = get_saldo(idanggota) + total

    data_tabungan.append({
        "tanggal": tanggal,
        "idtransaksi": idtransaksi,
        "tipetransaksi": tipetransaksi,
        "sampah": kode_sampah,
        "kuantitas": kuantitas,
        "nilaisatuan": hargasatuan,
        "total": total,
        "saldo": saldo
    })

    with open(f'tabungan{idanggota}.json', 'w') as file: #menyimpan file
        json.dump(data_tabungan, file, indent=4)

    print("Pencatatan transaksi tabungan sampah berhasil.")

    pilihan = input("Ada jenis sampah lain akan ditabung (Y/y = Ya, T/t = Tidak)? ")
    if pilihan.lower() == 'y':
        tambah_tabungan(idanggota)

def tarik_tabungan(idanggota):
    filename = f'tabungan{idanggota}.json'

    if os.path.isfile(filename):
        with open(filename) as file:
            data_tabungan = json.load(file)
    else:
        print("Data tabungan tidak ditemukan.")
        return

    total_saldo = get_saldo(idanggota)

    # Tampilkan data anggota
    data_anggota = cari_anggota_by_id(idanggota)
    print(f"IDAnggota: {idanggota} | Nama : {data_anggota['nama']} | Telepon: {data_anggota['telepon']} | Alamat: {data_anggota['alamat']}")
    print("="*40)
    print(f"Total Saldo: {total_saldo}")
    print("="*40)
    tarik = input("Apakah ingin menarik tabungan?(Y/y = Ya, T/t = Tidak) ")
    if tarik == 'y':
        # Membentuk data tabungan
        idtransaksi = generate_idtransaksi(idanggota)
        tanggal = datetime.datetime.now().strftime('%Y-%m-%d')
        tipetransaksi = "D"
        kuantitas = 1
        nilaisatuan = int(input("Jumlah penarikan tabungan : "))
        kode_sampah = 0
        total = nilaisatuan
        saldo = get_saldo(idanggota) - total

        data_tabungan.append({
            "tanggal": tanggal,
            "idtransaksi": idtransaksi,
            "tipetransaksi": tipetransaksi,
            "sampah": kode_sampah,
            "kuantitas": kuantitas,
            "nilaisatuan": nilaisatuan,
            "total": total,
            "saldo": saldo
        })

        # Menyimpan perubahan ke dalam file JSON
        with open(f'tabungan{idanggota}.json', 'w') as file:
            json.dump(data_tabungan, file, indent=4)
        print("Penarikan tabungan berhasil.")
    else:
        print("Penarikan dibatalkan")

def tampilkan_tabungan(idanggota):
    # Mengecek apakah data anggota ditemukan
    data_anggota = cari_anggota_by_id(idanggota)
    if not data_anggota:
        print("Data anggota tidak ditemukan.")
        return

    # Menampilkan informasi anggota
    print("=============================================")
    print(f"IDAnggota: {idanggota}              | Nama : {data_anggota['nama']}")
    print(f"Telepon: {data_anggota['telepon']}  | Alamat: {data_anggota['alamat']}")
    print("=============================================")

    # Mengecek apakah data tabungan ditemukan
    filename = f"tabungan{idanggota}.json"
    if not os.path.isfile(filename):
        print("Data tabungan tidak ditemukan.")
        return

    # Membaca data tabungan dari file JSON
    with open(filename) as file:
        data_tabungan = json.load(file)

    # Mengecek apakah data tabungan kosong
    if not data_tabungan:
        print("Tidak ada transaksi tabungan.")
        return

    # Mendapatkan informasi transaksi terakhir
    transaksi_terakhir = data_tabungan[-1]

    # Menampilkan informasi transaksi terakhir
    print(f"Tanggal Transaksi Terakhir  : {transaksi_terakhir['tanggal']}")
    print(f"Kode Transaksi Terakhir     : {transaksi_terakhir['idtransaksi']}")
    jenis_transaksi = "Tabungan" if transaksi_terakhir['tipetransaksi'] == 'K' else "Penarikan"
    print(f"Jenis Transaksi Terakhir    : {jenis_transaksi}")
    print(f"Nilai Transaksi Terakhir    : {transaksi_terakhir['total']}")
    print(f"Saldo Tabungan              : {transaksi_terakhir['saldo']}")

