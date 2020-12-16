'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 18 November 2020
Deskripsi   : Program untuk mencari palindrom terpanjang substring

Variable Dictionary:

'''

# algorithm
lenght = int(input("Masukkan panjang string: "))
kata = str(input("Masukkan string: "))
substring = []
for i in range(lenght):
    temp=""
    for j in range(i,lenght):
        temp = temp + kata[j]
        substring += [temp]
banyak_sub = 0
panjang_palindrom = []
for i in substring:
    banyak_sub += 1
for i in range(banyak_sub):
    count_cermin = 0
    panjang_sub = len(substring[i])
    k = panjang_sub - 1
    for j in range(panjang_sub//2):
        if substring[j] == substring[k]:
            count_cermin += 1
        k -= 1
    if count_cermin == panjang_sub//2:
        panjang_palindrom = panjang_palindrom + [panjang_sub]
max_palindrom = 0
for i in panjang_palindrom:
    if i > max_palindrom:
        max_palindrom = i
print("Panjangnya adalah ", max(panjang_palindrom))


