'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 1 November 2020
Deskripsi   : Program ini untuk mencari bilangan 10^x terkecil yang lebih besar dari angka N(diinputkan user)

Variable Dictionary:
N = integer, dimasukkan user sebagai pembanding nilai 10^x
x = integer, sebagai bilangan pangkat yang akan terus bertambah 1 jika masih memenuhi kondisi looping
'''

# algorithm
N = int(input("Masukkan N: ")) 
x = 0
# asumsi bahwa nilai 10^x adalah bilangan bulat
# karena jika 10^x bukan bilangan bulat, ketika x <= 0, bilangan 10^x terkecilnya tak hingga dan bernilai semakin mendekati 0
while 10**x <= N:   # looping untuk mencari bilangan 10^x terkecil yang lebih besar dari N
    x += 1          # nilai x terakhir bertambah 1 (x = x + 1)
print(str(10**x))   # mengoutput nilai 10^x yang memenuhi syarat paling kecil yang lebih besar dari N