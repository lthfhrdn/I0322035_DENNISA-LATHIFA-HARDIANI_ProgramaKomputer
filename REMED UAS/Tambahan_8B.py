import json
import os

def data_transaksi(idanggota):
    filename = f'tabungan{idanggota}.json'

    if os.path.isfile(filename):
        with open(filename) as file:
            data_tabungan = json.load(file)

        for tabungan in data_tabungan:
            print("=================================================")
            print("Tanggal Transaksi    :", tabungan['tanggal'])
            print("ID Transaksi         :", tabungan['idtransaksi'])
            print("Tipe Transaksi       :", tabungan['tipetransaksi'])
            print("Jumlah Transaksi     :", tabungan['total'])
            print("Saldo                :", tabungan['saldo'])
            print()
    else:
        print("Data tabungan tidak ditemukan")
        return
