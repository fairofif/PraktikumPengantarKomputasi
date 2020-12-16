'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 29 November 2020
Deskripsi   : Program untuk mencetak segitiga pascal
'''
def pascal(P):
    # fungsi untuk mengganti element dalam segitiga, kulit segitiga tetap bernilai 1
    # Kamus Lokal #
    # P = matriks of integer
    # N = int, ukuran matriks N x N
    #=======================================================================================
    for i in range(N): # nested loop untuk mengupdate element di dalam segitiga
        for j in range(N):
            if i > 0 and j > 0:
                P[i][j] = P[i-1][j] + P[i][j-1] # element diubah menjadi (element diatasnya + element dikirinya)
    return P

def printPascal(P):
    # prosedur untuk mencetak matriks
    # Kamus Lokal #
    # P = matriks of integer
    # N = int, ukuran matriks N x N
    #======================================================================================
    for i in range(N): # nested loop untuk mencetak seluruh element matriks
        for j in range(N):
            print(P[i][j], end=" ")
        print()

#=============== M A I N =================
N = int(input("Masukkan N: "))
P = [[1 for j in range(N)] for i in range(N)] # declare matriks N x N dengan default element 1
P = pascal(P)
printPascal(P)
