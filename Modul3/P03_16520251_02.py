'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 18 November 2020
Deskripsi   : mencetak kode rahasia dengan clue list of char

Variable Dictionary:
clue = array 1 dimensi berisi char (list of char)
n_bil = int, jumlah bilangan yang diinput
bilangan = string, bilangan yang diinput
'''

# algorithm
clue = [' ','A','B','E','I','K','L','R','T','U']
n_bil = int(input("Masukkan banyaknya bilangan: "))
# input bilangan sebagai string
bilangan = str(input("Masukkan bilangan: "))
# print hasil kode rahasia
for i in range(n_bil):
    # isi array of char dari bilangan di konversi ke integer
    print(clue[int(bilangan[i])], end="")