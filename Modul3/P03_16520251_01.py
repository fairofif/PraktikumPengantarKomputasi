'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 18 November 2020
Deskripsi   : Program untuk membagikan mobil menggunakan konsep sisa dan array

Variable Dictionary:
m = int, jumlah mobil
n = int, jumlah anak
pelat = array dengan elemen int
sisa = array dengan elemen int
count = array dengan elemen int
'''

# algorithm
m = int(input("Masukkan M: "))
pelat = [0 for i in range(m)]
sisa = [0 for i in range(m)]
#loop untuk input no pelat ke array pelat
for i in range(m):
    pelat[i] = int(input("Masukkan pelat nomor mobil ke-" + str(i+1) + ": "))
n = int(input("Masukkan N: "))
#loop untuk menentukan sisa bagi pelat dengan N
for i in range(m):
    sisa[i] = pelat[i]%n
#array count berfungsi untuk menjumlahkan mobil dengan no pelat sisa yang sama dengan i-1
count = [0 for i in range(n)]
#loop untuk menentukan seberapa banyak mobil dengan pelat sisa sama dengan i-1
for i in range(n):
    for j in range(m):
        if sisa[j] == i:
            count[i] += 1
            sisa[j] == -1   # sisa yang sudah sama dengan i diubah ke bilangan -1 agar tidak bisa dibanding lagi
for i in range(n):
    print("Anak ke-" + str(i+1) + " mendapatkan " + str(count[i]) + " mobil")