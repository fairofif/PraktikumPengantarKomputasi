'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 1 November 2020
Deskripsi   : Program ini untuk mencacah bilangan dari 1 ke N

Variable Dictionary:
N = integer, dimasukkan user sebagai batas looping
i = integer, sebagai bilangan kondisi looping
'''

# algorithm
N = int(input("Masukkan N: "))  # input nilai integer ke variable N

if N > 0:   # kondisi N > 0
    for i in range(1, N+1):         # akan looping dari i = 1 diincrement (+1) hingga i = N
        print(str(i), end=" ")      # mengoutput nilai i dan menambahkan end spasi agar tidak membuat line baru
else:       # kondisi N <= 0
    for i in range(1, N-1, -1):     # akan looping dari i = 1 didecrement (-1) hingga i = N
        print(str(i), end=" ")      # mengoutput nilai i dan menambahkan end spasi agar tidak membuat line baru

print("") # sebagai endline (baris baru kosong) agar terlihat rapi di terminal