'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 21 Oktober 2020
Deskripsi   : Program ini untuk menjumlahkan permen dari 4 orang anak, dan membagi rata jumlahnya ke 4 anak tersebut,
              jika permen tidak rata dibagi, sisa permennya akan diambil Tuan Kan

Variable Dictionary:
permen_1 = jumlah permen yang dimiliki anak ke-1
permen_2 = jumlah permen yang dimiliki anak ke-2
permen_3 = jumlah permen yang dimiliki anak ke-3
permen_4 = jumlah permen yang dimiliki anak ke-4
'''

#algorithm
permen_1 = int(input("Masukkan jumlah permen yang dimiliki anak ke-1: "))
if permen_1 < 0:    # jika permen anak ke 1 negatif
    print("Jumlah permen yang dimiliki anak tidak boleh negatif")
else:
    permen_2 = int(input("Masukkan jumlah permen yang dimiliki anak ke-2: "))
    if permen_2 < 0: # jika permen anak ke 2 negatif
        print("Jumlah permen yang dimiliki anak tidak boleh negatif")
    else:
        permen_3 = int(input("Masukkan jumlah permen yang dimiliki anak ke-3: "))
        if permen_3 < 0: # jika permen anak ke 3 negatif
            print("Jumlah permen yang dimiliki anak tidak boleh negatif")
        else:
            permen_4 = int(input("Masukkan jumlah permen yang dimiliki anak ke-4: "))
            if permen_4 < 0: # jika permen anak ke 4 negatif 
                print("Jumlah permen yang dimiliki anak tidak boleh negatif")
            else:
                print("Setiap anak akan mendapatkan " + str((permen_1 + permen_2 + permen_3 + permen_4)//4) + " permen.") #mencari hasil bagi yang dibulatkan ke bawah dari total permen 4 anak
                print("Sisa permen yang diambil Tuan Kan sebanyak " + str((permen_1 + permen_2 + permen_3 + permen_4)%4) + " permen." ) #mencari sisa permen untuk tuan kan
