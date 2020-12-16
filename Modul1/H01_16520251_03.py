'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Kelas/Sesi  : 3.1/D
Tanggal     : 18 Oktober 2020
Deskripsi   : Program ini untuk menentukan jenis bilangan yang akan diinputkan oleh user

Variable Dictionary:
x (int)  = bilangan bulat yang akan dicek apakah termasuk bilangan ganji atau bilangan genap 
'''

# Algorithm
x = int(input("Masukkan X: "))   #memasukan bilangan bulat ke variabel x oleh user
if x > 0:   #kondisi x positif
    if x % 2 == 0:  #kondosi x tidak memiliki sisa jika dibagi 2, maka x genap
        print(str(x) + " adalah bilangan positif genap")
    else:   #kondisi x memiliki sisa jika dibagi 2, maka x ganjil
        print(str(x) + " adalah bilangan positif ganjil")
elif x < 0:     #kondisi x negatif
    print(str(x) + " adalah bilangan negatif")
else:   #kondisi x = 0
    print(str(x) + "adalah bilangan nol")