'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 2 Desember 2020
Deskripsi   : Program untuk mencari total jarak antar kota
'''

def getKoordinat():
    # fungsi untuk mengambil data koordinat kota
    # Kamus Lokal #
    # n_kota = int, jumlah kota
    # koor_x = array of int, kumpulan koordinat x
    # koor_y = array of int, kumpulan koordinat y
    n_kota = int(input("Masukkan jumlah kota: "))
    koor_x = [0 for i in range(n_kota)]
    koor_y = [0 for i in range(n_kota)]
    for i in range(n_kota):
        koor_x[i] = int(input("Masukkan koordinat x kota ke " + str(i+1) + ": "))
        koor_y[i] = int(input("Masukkan koordinat y kota ke " + str(i+1) + ": "))
    return koor_x, koor_y, n_kota

def hitungJarakAntarKota(koor_x, koor_y, n_kota):
    # fungsi untuk menghitung jarak antar kota
    # Kamus Lokal #
    # jarak = array of float, kumpulan jarak antar kota
    # jarak_x = int, jarak x antar kota
    # jarak_y = int, jarak y antar kota
    # jarak_kota = float, jarak antar kota
    jarak = [0 for i in range(n_kota-1)]
    for i in range(n_kota-1):   # loop untuk menentukan jarak antar kota
        if koor_x[i] > koor_x[i+1]: 
            jarak_x = koor_x[i] - koor_x[i+1]
        else: # x di kota b lebih besar dari x di kota a
            jarak_x = koor_x[i+1] - koor_x[i]
        if koor_y[i] > koor_y[i+1]:
            jarak_y = koor_y[i] - koor_y[i+1]
        else: # y di kota b lebih besar dari y di kota a
            jarak_y = koor_y[i+1] - koor_y[i]
        jarak_kota = ((jarak_x**2) + (jarak_y**2))**0.5 
        jarak[i] = jarak_kota # jarak antar kota ditambahkan ke array jarak
    return jarak

def hitungTotalJarak(jarak, n_kota):
    # fungsi untuk menghitung total jarak yang ada di array kumpulan jarak antar kota
    # Kamus Lokal #
    # jarak_total = float, hasil penjumlahan seluruh kumpulan jarak antar kota
    jarak_total = 0
    for i in range(n_kota-1): # loop untuk mentotalkan jarak antar kota
        jarak_total += jarak[i]
    return jarak_total

# =============== M A I N ==================

koor_x, koor_y, n_kota = getKoordinat()
jarak = hitungJarakAntarKota(koor_x,koor_y,n_kota)
jarak_total = hitungTotalJarak(jarak,n_kota)
print("Jarak totalnya " + str(jarak_total))