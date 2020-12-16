'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 21 Oktober 2020
Deskripsi   : Program ini untuk mengintegralkan sebuah fungsi y = ax + b

Variable Dictionary:

'''

#algorithm
a_awal = int(input("Masukkan konstanta variable a: "))
b_awal = int(input("Masukkan konstanta variable b: "))
a_akhir = (a_awal/2)

if a_awal == 0:
    if b_awal == 0:
        print("fungsi sebelum diintegralkan: ")
        print("f(x) = 0")
        print("f(x) = 0")
        print("fungsi setelah diintegralkan: ")
        print("F(x) = 0 + C")
    else:
        print("fungsi sebelum diintegralkan: ")
        print("f(x) = " + str(b_awal))
        print("fungsi setelah diintegralkan: ")
        print("F(x) = " + str(b_awal) + "x + C")
else:
    if b_awal == 0:
        print("fungsi sebelum diintegralkan: ")
        print("f(x) = " + str(a_awal) + "x")
        print("fungsi setelah diintegralkan: ")
        print("F(x) = " + str(a_akhir) + "x^2 + C")
    else:
        print("fungsi sebelum diintegralkan: ")
        print("f(x) = " + str(a_awal) + "x + " + str(b_awal))
        print("fungsi setelah diintegralkan: ")
        print("F(x) = " + str(a_akhir) + "x^2 + " + str(b_awal) + "x + C")
