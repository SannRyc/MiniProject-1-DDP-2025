print("-"*45)
print("Nama    : Muhammad Ihsan Kamil")
print("NIM     : 2509116035")
print("Kelas   : Sistem Informasi A 2025")
print("Program : Mini Project 1 (Praktikum DDP)")
print("Tema    : Sistem Menejemen Order Jahitan")
print("-"*45)

list_order = [
    "billie - kemeja - biru - 25 sep 25",
    "herry - celana - merah - 26 sep 25",
    "samsul - jubah - putih - 30 sep 25"
]

#Menu
print()
print("Selamat datang")
print("Apa yang ingin anda lakukan hari ini?")
print()
print("1. Tambah order")
print("2. Lihat Semua Order")
print("3. Hapus Order")
print("4. Keluar")
print()

try:
    pilih = int(input("Pilih menu antara 1 - 4: "))
    print()
    #Fungsi untuk menampilkan list dengan rapi

    def tampilkan_order():
        if not list_order:
            print("Belum ada order")
        else:
            nomor = 1
            for order in list_order:
                print(str(nomor) + ". " + order)
                nomor += 1


    #Tambah order
    if pilih == 1:
        nama  = input("Nama pelanggan     : ")
        jenis = input("Jenis pakaian      : ")
        warna = input("Warna pakaian      : ")
        ambil = input("Tanggal pengambilan: ")
        print()

        order = nama + " - " + jenis + " - " + warna + " - " + ambil
        list_order.append(order)

        print("Order berhasil ditambahkan, berikut list terbaru:")
        print()
        tampilkan_order()

    #Lihat semua order
    elif pilih == 2:
        print("Daftar Order:")
        tampilkan_order()

    #Hapus order
    elif pilih == 3:
        print("Daftar Order:")
        tampilkan_order()
        print()
        try:
            hapus = int(input("Masukkan nomor order yang ingin dihapus: "))
            if 1 <= hapus <= len(list_order):
                del list_order[hapus-1]
                print("Order telah dihapus, berikut list terbaru:")
                tampilkan_order()
            else:
                print("Input tidak valid, nomor order tidak tersedia")
        except:
            print("Input tidak valid, harus berupa angka int")

    #Keluar
    elif pilih == 4:
        print("Keluar dari program")

    else:
        print("Input tidak valid")

except:
    print("Input tidak valid, harus berupa angka int")