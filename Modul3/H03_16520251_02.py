'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 15 November 2020
Deskripsi   : Program untuk mengecek seluruh element array B merupakan anagram dari element A atau bukan

Variable Dictionary:
n_A = int, batasan jumlah elemen dari array elementA
n_B = int, batasan jumlah elemen dari array elementB
elementA = array 1 dimensi yang memiliki elemen betipe integer
elementB = array 1 dimensi yang memiliki elemen betipe integer
count = int, penjumlah berapa banyak pasangan sama dari elementA dan elementB
i = int
j = int
'''

# algorithm
# membuat dan mengisi array elementA
n_A = int(input("Masukkan banyaknya elemen A: "))
elementA = [0 for i in range(n_A)]
for i in range(n_A):
    elementA[i] = int(input("Masukkan elemen A ke-" + str(i+1) + ": "))

# membuat dan mengisi array elementB
n_B = int(input("Masukkan banyaknya elemen B: "))
elementB = [0 for i in range(n_B)]
for i in range(n_B):
    elementB[i] = int(input("Masukkan elemen B ke-" + str(i+1) + ": ")) 

count = 0   # declare jumlah pasangan elemen A dan B yang bernilai sama menjadi 0 terlebih dahulu
# nested loop untuk mencari isi elementB yang bernilai sama dengan elementA
for i in range(n_B):
    for j in range(n_A):
        if elementA[j] == elementB[i]: # jika terdapat element yang sama
            count += 1
            elementA[j] = -888           # elementA dan elemenntB diubah menjadi bilangan yang
            elementB[i] = -999           # tidak memenuhi syarat, agar pasangan tidak terhitung dua kali

# jika jumlah pasangan yang sama = banyak indeks data elementA = banyak indeks data elementB
if count == n_A and count == n_B:
    print("B adalah anagram dari A")
else:   # n_A != n_B
    print("B bukan anagram dari A")    
