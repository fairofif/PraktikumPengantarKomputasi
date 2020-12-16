'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 29 November 2020
Deskripsi   : Program untuk mengitung nilai f(x) di interval x dari A hingga B
'''

def getAB():
    # fungsi untuk menginputkan nilai A dan B lalu me-return-nya
    # Kamus Lokal #
    # A = int, batas bawah nilai x
    # B = int, batas atas nilai x
    #======================================================================================
    A = int(input("Masukkan A: "))
    B = int(input("Masukkan B: "))
    return A, B
    
def getXAndFX(x):
    # fungsi untuk menghitung fx dari x tertentu
    # Kamus Lokal #
    # x = int
    # fx = int, nilai f(x) = x^2 - 2x + 5, di x tertentu
    #======================================================================================
    x += 1
    fx = (x**2) - (2*x) + 5
    return x, fx 

def printFX(x, fx):
    # prosedur untuk mencetak nilai2 f(x)
    # Kamus Lokal #
    # x = int
    # fx = int
    #======================================================================================
    print("f(" + str(x) + ") = " + str(fx))

#=============== M A I N =================
A, B = getAB() # mengambil nilai return A dan B
x = A - 1
# loop untuk menghitung fx dan men-increment x, lalu mencetaknya
while x < B:
    x, fx = getXAndFX(x) # mengambil nilai return x dan fx
    printFX(x,fx)

