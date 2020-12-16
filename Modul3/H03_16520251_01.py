'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 15 November 2020
Deskripsi   : Program ini untuk mengoutputkan urutan angka secara terbalik

Variable Dictionary:
n = int, input user sebagai batasan indeks array, indeks array terbesar = n - 1
                                                  indeks array terkecil = 0
array = array 1 dimensi yang berisi sebuah nilai integer
i = int
'''

#algorithm
n = int(input("Masukkan N: "))
array = [0 for i in range(n)]  # membuat array 1 dimensi dengan isi default int = 0

# loop untuk menginputkan nilai int ke dalam array 1 dimensi secara satu per satu
for i in range(n):
    array[i] = int(input())  

print("Hasil dibalik: ")
# loop untuk mengoutputkan isi nilai array dari indeks array terbesar hingga terkecil
for i in range(n-1, -1, -1):
    print(array[i])