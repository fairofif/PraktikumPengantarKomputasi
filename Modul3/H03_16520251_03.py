'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 15 November 2020
Deskripsi   : Program untuk mengecek string apakah kata palindrom atau bukan

Variable Dictionary:
lenght = int , input user banyak char dalam string
kata = string, array of char, inputan user
check_lenght = int, penghitung jumlah huruf dalam kata yang akan dicek jumlahnya
count = int, penghitung jumlah kesamaan suku ke-n dari kiri dengan suku ke-n dari kanan
i = int
j = int
'''

# algorithm
lenght = int(input("Masukkan panjang string: "))
kata = input("Masukkan string: ")

# mencari panjang kata inputan (algoritma pengganti fungsi len())
# kemudian dicek apakah panjang kata sama dengan lenght atau tidak
check_lenght = 0
for i in kata:
    check_lenght += 1
while check_lenght != lenght:
    kata = input("Jumlah huruf tidak sama dengan panjang string.\nMasukkan string: ")
    check_lenght = 0
    for i in kata:
        check_lenght += 1

count = 0 # declare jumlah kesamaan char ke-n kiri dengan char ke-n kanan = 0
# loop untuk mengecek kesamaan char ke-n dari kiri dengan char ke-n dari kanan
j = lenght - 1
for i in range(lenght//2):
    if kata[i] == kata[j]: # kata[i] = kata ke-n dari kiri, kata[j] =  kata ke-n dari kanan
        count +=1
    j -= 1

# jika jumlah kesamaan = panjang kata * 1/2
if count == lenght//2:  
    print(kata + " adalah palindrom")
else: # jika count != lenght//2
    print(kata + " bukan palindrom")