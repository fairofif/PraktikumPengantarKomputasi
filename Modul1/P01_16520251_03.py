'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 21 Oktober 2020
Deskripsi   : Program ini untuk mencari rute terpendek dari 3 titik, yang setelah beres tiga titik ada 1 destinasi tambahan yaitu ke resto

Variable Dictionary:

'''

#algorithm
#titik Tuan Mor(0,0)
#titik Tuan Kim
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
#titik Tuan Ryo
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))
#titik resto
x3 = int(input("Masukkan x3: "))
y3 = int(input("Masukkan y3: "))

if x1 < 0:
    if y1 < 0:
        mor_ke_kim = (0 - x1) + (0 - y1)
    else:
        mor_ke_kim = (0 - x1) + y1
else:
    if y1 < 0:
        mor_ke_kim = x1 + (0 - y1)
    else:
        mor_ke_kim = x1 + y1

if x2 < 0:
    if y2 < 0:
        mor_ke_ryo = (0 - x2) + (0 - y2)
    else:
        mor_ke_ryo = (0 - x2) + y2
else:
    if y2 < 0:
        mor_ke_ryo = x2 + (0 - y2)
    else:
        mor_ke_ryo = x2 + y2

if mor_ke_kim < mor_ke_ryo:
    jarak_1 = mor_ke_kim
    if x1 < 0:
        if x2 < 0:
            jarak_x2 = (-1*x1) - (-1*x2)
        else:
            jarak_x2 = (-1*x1) - x2
    else:
        if x2 < 0:
            jarak_x2 = x1 - (-1*x2)
        else:
            jarak_x2 = x1 - x2
    if y1 < 0:
        if y2 < 0:
            jarak_y2 = (-1*y1) - (-1*y2)
        else:
            jarak_y2 = (-1*y1) - y2
    else:
        if y2 < 0:
            jarak_y2 = y1 - (-1*y2)
        else:
            jarak_x2 = y1 - y2
    if jarak_x2 < 0:
        jarak_x2 = -1 * jarak_x2 
    if jarak_y2 < 0:
        jarak_y2 = -1 * jarak_y2     


    jarak_2 = jarak_x2 + jarak_y2
    jarak_total = jarak_1 + jarak_2 + (x3 - x2) + (y3 - y2)
else:
    jarak_1 = mor_ke_ryo
    jarak_2 = (x1 - x2) + (y1 - y2)
    jarak_total = jarak_1 + jarak_2 + (x3 - x1) + (y3 - y1)

print("Jarak terpendeknya adalah " + str(jarak_total))


