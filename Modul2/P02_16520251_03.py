'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 4 November 2020
Deskripsi   : Program untuk mencetak pola persegi dengan isi bilangan mengurut

Variable Dictionary:
n = int, 2n sebagai batas kolom dan baris
'''
n = int(input("Masukkan bilangan: "))
print("Pola yang terbentuk: ")

# loop untuk membentuk pola persegi
for j in range(1, ((n+1)*2)-1):     # j sebagai baris (sesuai vektor)
    for i in range(1, ((n+1)*2)-1):         # i sebagai kolom (sesuai vektor)
        if i == 1 or j == 1 or i == (n*2) or j == (n*2):
            print("0", end="")
        else:
            print(end=" ")
    print("")