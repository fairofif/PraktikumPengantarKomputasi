'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 1 November 2020
Deskripsi   : Program ini untuk menentukan bilangan prima atau bukan prima

Variable Dictionary:
X = integer, bilangan inpur yang akan diuji apakah prima atau bukan
status = integer, sebagai jumlah bilangan dari 2 sampai X-1 yang bisa membagi habis X
i = integer, sebagai bilangan kondisi looping, dan penguji pembagian X
'''

# algorithm
X = int(input("Masukkan X: "))
status = 0                  # status untuk menentukan jumlah angka dari (2 sampai X-1) yang bisa membagi habis X
for i in range(2, X):       # looping dari i = 2 diincrement (+1) hingga i = X-1
    if X%i == 0:            # menentukan apakah X habis dibagi i
        status += 1         # jika X habis dibagi i, maka status jumlah angka yang bisa membagi habis X bertambah 1

if status >= 1 or X < 2:                        # kondisi jika status >= 0 atau X < 2, maka X bukan prima
    print(str(X) + " bukan bilangan prima")
else:                                           # kondisi jika status == 0, maka X adalah prima
    print(str(X) + " adalah bilangan prima")