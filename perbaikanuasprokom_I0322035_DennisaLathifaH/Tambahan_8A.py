import json

def bubble_sort(anggota_list):
    n = len(anggota_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if anggota_list[j]['idanggota'] > anggota_list[j+1]['idanggota']:
                anggota_list[j], anggota_list[j+1] = anggota_list[j+1], anggota_list[j]

# Membaca data anggota dari file JSON
with open("anggotas.json") as file:
    data_anggota = json.load(file)
    anggota_list = list(data_anggota.values())

# Mengurutkan data anggota menggunakan Bubble Sort
bubble_sort(anggota_list)
