'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 4 November 2020
Deskripsi   : Program untuk mencari FPB dari 4 bilangan input

Variable Dictionary:
a = int, bilangan pertama
b = int, bilangan kedua
c = int, bilangan ketiga
d = int, bilangan keempat
terbesar = int, sebagai variable bilangan terbesar penentu batasan loop dalam menentukan fpb
fpb = int, hasil bilangan fpb terakhir
'''

# algorithm
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

terbesar = 1  #mendeclare bilangan terbesar sementara = 1
# loop untuk menentukan bilangan terbesar sebenarnya
while terbesar < a or terbesar < b or terbesar < c or terbesar < d:
    terbesar += 1   # jika masih ada bilangan yang lebih besar dari bilangan dalam variabel terbesar,
                    # maka bilangan terbesar sementara akan bertambah 1

# loop untuk menentukan FPB
for i in range(1, terbesar + 1):        
    if a%i == 0 and b%i == 0 and c%i == 0 and d%i == 0:
        fpb = i     # fpb berubah sementara menjadi i yang terakhir
print("FPB dari keempat bilangan adalah " + str(fpb))