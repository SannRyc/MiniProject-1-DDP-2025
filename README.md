# Mini Project 1 DDP 2025

# Profil
Nama  : Muhammad Ihsan Kamil\
NIM   : 2509116035\
Kelas : Sistem Informasi A 2025\
Tugas Praktikum, Mini Project 1 DDP

# Deskripsi
Sistem Menejemen Order Jahitan dibuat untuk membantu pengguna dalam menyimpan orderan jahitan.\
Dalam program ini terdapat beberapa menu seperti:
- Tambah Order
- Lihat Semua Order
- Hapus Order
- Keluar\
- 
# BERIKUT PROGRAM SECARA KESELURUHAN
![CODING MINPRO DDP 1 FINAL](https://github.com/user-attachments/assets/7061d1bb-a0ee-45cb-bf90-6e1150be04c1)
# Penjelasan Program
**1. List Order**
![1 list ](https://github.com/user-attachments/assets/3c3e8d00-889b-45af-92e8-5f448b0ffafd)
list_order adalah sebuah list atau daftar di Python yang berisi beberapa data order jahitan.
Tiap order ditulis dalam bentuk string (teks) yang dipisahkan dengan tanda strip "-".
data yang tersimpan didalam list ini saya urutkan menjadi\
nama pelanggan – jenis pakaian – warna – tanggal pengambilan.

**2. Menu**
![2 menu](https://github.com/user-attachments/assets/91da9682-b607-434a-9f5f-df716dbff9cb)
Pada bagian ini program akan menampilkan daftar menu yang tersedia didalam program ini.

**3. Membuat list order lebih rapi**
![3 membuat list rapi](https://github.com/user-attachments/assets/6f727675-92b7-4928-a16c-437e4a369774)
Pada bagian ini saya menggunakan "try" untuk mencegah program error ketika input yang dimasukkan tidak bisa diubah menjadi angka seperti huruf atau karakter. Tujuan diibuatnya fungsi "tampilkan_order()" supaya daftar order yang ditampilkan lebih rapi dan tidak perlu menulis kode berulang. Di dalam fungsi ini ada "if not list_order" untuk mengecek apakah list kosong, jika list tidak kosong maka perulangan "for order in list_order" dipakai untuk menampilkan setiap item dalam list satu per satu. Variabel "nomor" digunakan untuk memberi nomor urut pada setiap order, dan "str(nomor)" dipakai agar nomor (yang berupa angka) bisa digabung dengan teks saat ditampilkan. Semua bagian ini membantu program jadi lebih aman, rapi, dan mudah dipahami.

**4. Tambah Order**
![4 tambah order](https://github.com/user-attachments/assets/162b923c-ed8a-418a-b368-ebe4f45c0609)
Pada bagian ini, program meminta input dari pengguna berupa nama, jenis pakaian, warna, dan tanggal pengambilan, lalu semua data itu digabung menjadi satu string dengan tanda pemisahnya "-". String hasil gabungan tersebut disimpan ke variabel "order", kemudian ditambahkan ke dalam "list_order" dengan "append()". Setelah itu, program menampilkan pesan bahwa order berhasil ditambahkan dan langsung memanggil fungsi "tampilkan_order()" untuk menampilkan daftar order terbaru.

**5. Lihat Semua Order**
![5 lihat semua order](https://github.com/user-attachments/assets/33ca8352-8933-4bfc-a4b6-fbc8cd308033)
Pada bagian ini, jika pengguna memilih menu nomor 2 maka program akan menampilkan tulisan "Daftar Order:" kemudian memanggil fungsi "tampilkan_order()", sehingga semua isi "list_order" ditampilkan secara rapi sesuai urutan.

**6. Hapus Order**
![6 hapus order](https://github.com/user-attachments/assets/29c89721-26f1-4f08-a03f-e72761a1a95d)
Pada bagian ini, program pertama menampilkan daftar order dengan memanggil "tampilkan_order()", lalu meminta pengguna memasukkan nomor order yang ingin dihapus. Input tersebut dibungkus dalam "try" agar jika pengguna mengetik selain angka, program tidak error melainkan menampilkan pesan "Input tidak valid, harus berupa angka int". Jika input berupa angka, dicek apakah nomor tersebut ada dalam indeks list_order, dan jika valid maka order dihapus dengan "del list_order[hapus-1]" serta ditampilkan ulang daftar order terbaru, sedangkan jika nomor tidak sesuai maka muncul pesan "Input tidak valid, nomor order tidak tersedia".

**7. Keluar**
![6 keluar program](https://github.com/user-attachments/assets/fb8868a7-1e77-470f-8ac0-92567c42d335)
Pada bagian ini, jika pengguna memilih menu nomor 4 maka program akan menampilkan pesan "Keluar dari program" dan keluar dari program, sedangkan jika pengguna memasukkan angka di luar pilihan (selain 1–4), maka program akan menampilkan pesan "Input tidak valid". Seluruh input dibungkus dengan "try ... except", sehingga jika user memasukkan huruf atau karakter lain yang bukan angka, program tidak error melainkan akan menampilkan pesan "Input tidak valid, harus berupa angka int".

# HASIL/OUTPUT DARI PROGRAM YANG SAYA BUAT
**1. Jika Kondisi Input benar**
![FOTO CODING INPUT BENAR](https://github.com/user-attachments/assets/93109d71-c6c7-432c-aca5-387e607beb8f)
Pada gambar ini menunjukkan output dan alur apabila input yang diberikan pengguna benar.

**2. Jika Kondisi Input Salah**
![FOTO CODING INPUT SALAH](https://github.com/user-attachments/assets/df771000-3182-4f87-871d-a47651dd63a4)
Pada gambar ini menunjukkan output dan alur apabila input yang diberikan pengguna salah.

**3. Jika list_order kosong**
<img width="1703" height="943" alt="Screenshot 2025-09-14 223747" src="https://github.com/user-attachments/assets/13db4437-6d4e-45ae-99f9-8f4c7b7b05d1" />
Pada gambar ini menunjukkan output dan alur apabila list_order kosong atau tidak menyimpan data.

# MEMBUAT FLOWCHART
![MINPRO DDP 1-FLOWCHART MINPRO DDP 1 FINAL](https://github.com/user-attachments/assets/6e28a85a-47e7-4546-ae09-38738e9cdedd)
Pada awalan saya membuat "Mulai", program dimulai dengan menampilkan menu lalu pengguna diminta untuk meng-input nomor menu yang ingin ditampilkan. Jika input yang diberikan berupa angka namun diluar dari indeks list_order, maka program akan menampilkan "Input tidak valid", apabila input yang diberikan selain angka maka program akan menampilkan "Input tidak valid, harus berupa angka int".\

**Input == 1**\
Jika input yang diberikan 1, maka pengguna akan diminta meng-input nama pelanggan, jenis pakaian, warna pakaian, dan tanggal pengambilan. Program akan memproses data yang telah diberikan dan disimpan kedalam list_order, program akan menampilkan "Order berhasil ditambahkan, berikut list terbaru:", lalu menampilkan list order yang telah diperbarui.

**Input == 2**\
Jika input yang diberikan 2, maka program akan menampilkan list_order. Namun, apabila list_order masih kosong, maka program akan menampilkan "Belum ada order"

**Input == 3**\
Jika input yang diberikan 3, maka program akan menampilkan list_order. Apabila list_order kosong, maka program akan menampilkan "Belum ada order" lalu "Belum ada order untuk dihapus" setelah input nomor order yang ingin dihapus. Jika list_order terisi, maka program akan meminta pengguna untuk meng-input nomor order yang ingin dihapus. Apabila input yang diberikan selain angka maka program akan menampilkan "Input tidak valid, harus berupa angka int". Namun, apabila input yang diberikan berupa angka namun diluar dari indeks list_order, maka program akan menampilkan "Input tidak valid".\

Jika input yang diberikan valid, maka program akan memproses data yang akan dihapus, lalu menampilkan "Order berhasil dihapus, berikut list terbaru:" dan menampilkan list order yang telah diperbarui.

**Input == 4**\
Jika input yang diberikan 4, maka program akan memproses untuk keluar dari program itu sendiri, lalu menampilkan "Keluar dari program"

**Jika input selain dari 1/2/3/4**\
Jika input yang diberikan selain dari nomor 1/2/3/4, maka ada 2 kondisi, yaitu:

-Kondisi 1
Apabila input yang diberikan berupa angka namun diluar dari angka 1/2/3/4, maka program akan menampilkan "Input tidak valid".

-Kondisi 2
Apabila input yang diberikan berupa huruf/karakter/input selain angka, maka program akan menampilkan "Input tidak valid, harus berupa angka int"

**Sekian penjelasan dari program yang saya buat, terimakasih.**
