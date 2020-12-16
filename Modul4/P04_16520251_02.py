'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 2 Desember 2020
Deskripsi   : Program untuk menciptakan template game minesweeper
'''

def getElement():
    # fungsi untuk membuat matriks sementara
    # Kamus Lokal #
    # baris = int, batas baris matriks
    # kolom = int, batas kolom matriks
    # M = Matriks sementara, dengan nilai null, dan diperbesar 1 satuan di setiap sisi
    baris = int(input("Masukkan jumlah baris matriks: "))
    kolom = int(input("Masukkan jumlah kolom matriks: "))
    # declare matriks yang diexpand 1 satuan di setiap sisi dengan default null
    M = [["null" for j in range(kolom+2)] for i in range(baris+2)]
    for i in range(1, baris+1): # nested loop untuk mengisi element 
        for j in range(1, kolom+1):
            M[i][j] = str(input("Masukan elemen baris " + str(i) + " kolom " + str(j) + ": "))
    return M, baris, kolom

def getNewMatriks(M, baris, kolom):
    # fungsi untuk membuat matriks angka
    # Kamus Lokal #
    # count = int, jumlah bom disekeliling satu titik
    # M = matriks of char, matriks yang dikelilingi expand string "null"
    for i in range(1, baris+1): # nested loop untuk mengecek kondisi titik matriks
        for j in range(1, kolom+1):
            count = 0
            if M[i][j] == "*":
                M[i][j] = "#"
            else: # ketika isinya '.'
                # mengecek seluruh element sekeliling, jika ketemu bom maka count akan ditambah 1
                if M[i-1][j] == "*" or M[i-1][j] == "#":
                    count += 1
                if M[i+1][j] == "*" or M[i+1][j] == "#":
                    count += 1
                if M[i][j-1] == "*" or M[i][j-1] == "#":
                    count += 1
                if M[i][j+1] == "*" or M[i][j+1] == "#":
                    count += 1
                if M[i+1][j+1] == "*" or M[i+1][j+1] == "#":
                    count += 1
                if M[i-1][j+1] == "*" or M[i-1][j+1] == "#":
                    count += 1
                if M[i-1][j-1] == "*" or M[i-1][j-1] == "#":
                    count += 1
                if M[i+1][j-1] == "*" or M[i+1][j-1] == "#":
                    count += 1
                M[i][j] = str(count)           
    return M

def printNewMatriks(M, baris, kolom):
    # prosedur untuk mencetak matriks angka
    # Kamus Lokal #
    # M = matriks of char
    # baris = int, batas baris matriks yang memiliki isi char
    # kolom = int, batas kolom matriks yang memiliki isi char
    print("Matriks angka: ")
    for i in range(1, baris+1): # loop untuk mengoutput matriks baru
        for j in range(1, kolom+1):
            print(M[i][j], end="")
        print()

# ========== M A I N ===========
M, baris, kolom = getElement()
M = getNewMatriks(M,baris,kolom)
printNewMatriks(M,baris,kolom)