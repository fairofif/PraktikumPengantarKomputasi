'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 4 November 2020
Deskripsi   : Program untuk mencacah i, dan menguji kelipatan kepada 3 bilangan

Variable Dictionary:
n = int, batasan angka yang akan di tes
a = int, bilangan A
b = int, bilangan B
c = int, bilangan C
spasi = bool, untuk menentukan space
'''

# algorithm
n = int(input("Masukkan N: "))
a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))
spasi = False

# proses mencacah dan menentukan apakah i kelipatan A,B,C atau tidak
for i in range(1, n+1):
    if i%a == 0:
        print("Siap", end="")
    else:
        spasi = True            #spasi akan berubah jadi True jika tidak memenuhi kondisi uji terakhir
    if i%b == 0:                    
        print("Bang", end="")
    else:
        spasi = True            #spasi akan berubah jadi True jika tidak memenuhi kondisi uji terakhir
    if i%c == 0:
        print("Jago", end="")
    else:
        spasi = True            #spasi akan berubah jadi True jika tidak memenuhi kondisi uji terakhir
    if i%a != 0 and i%b != 0 and i%c != 0:
        print(i, end="")
    else:
        spasi = True            #spasi akan berubah jadi True jika tidak memenuhi kondisi uji terakhir
    if spasi == True:           #jika spasi True maka akan memberikan space
        print(end=" ")
    