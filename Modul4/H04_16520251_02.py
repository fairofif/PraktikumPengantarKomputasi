'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 29 November 2020
Deskripsi   : Program untuk menghitung element bernilai positif di matriks, dan mencetak seluruh element matriks
'''

def getNM():
    # fungsi untuk menginput N dan M lalu mereturnnya
    # Kamus Lokal #
    # N = int, batas baris matriks
    # M = int, batas kolom matriks
    #======================================================================================
    N = int(input("Masukkan N: "))
    M = int(input("Masukkan M: "))
    return N, M

def getElementA(A):
    # fungsi untuk menginput element ke matriks A
    # Kamus Lokal #
    # A = matriks of integer
    # N = int, batas baris matriks
    # M = int, batas kolom matriks
    #======================================================================================
    for i in range(N):
        for j in range(M):
            A[i][j] = int(input("Masukkan nilai A[" + str(i+1) + "][" + str(j+1) + "]: "))
    return A

def checkElement(A):
    # fungsi untuk membaca matriks lalu menghitung jumlah element yang positif
    # Kamus Lokal #
    # count = int, jumlah element positif dalam matriks
    # A = matriks of integer
    # N = int, batas baris matriks
    # M = int, batas kolom matriks
    # count = int, banyak bilangan positif
    #======================================================================================
    count = 0
    for i in range(N): # nested loop untuk membaca matriks
        for j in range(M):
            if A[i][j] > 0: # jika element A positif count ditamhah 1
                count += 1
    return count

def printElement(A, count):
    # prosedur untuk mencetak matriks
    # Kamus Lokal #
    # count = int, jumlah element positif dalam matriks
    # A = matriks of integer
    # N = int, batas baris matriks
    # M = int, batas kolom matriks
    # count = int, banyak bilangan positif
    #======================================================================================
    print("Ada " + str(count) + " bilangan positif di matriks.")
    for i in range(N): # nested loop untuk print seluruh element matriks
        for j in range(M):
            print(A[i][j], end=" ")
        print()

#=============== M A I N =================
N, M = getNM()
A = [[0 for j in range(M)] for i in range(N)]   # declare default matriks N x M
A = getElementA(A)
count = checkElement(A)
printElement(A,count)