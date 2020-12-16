'''
NIM         : 16520251
Nama        : Rofif Fairuz Hawary
Sesi/Kelas  : 3.1/D
Tanggal     : 18 Oktober 2020
Deskripsi   : Program ini sebagai kalkulator sederhana yang memiliki operator
              + , - , * , / , dan %

Variable Dictionary:
num_first (int) = bilangan pertama yang dimasukkan user, bilangan merupakan bilangan bulat
num_second (int) = bilangan kedua yang dimasukkan user, bilangan merupakan bilangan bulat
operator (string) = karakter dari operator yang akan dimasukkan user
'''

# Algorithm
print("Program Kalkulator Sederhana")
print("")            # membuat new line
num_first = int(input("Masukkan angka pertama: "))    # memasukkan bilangan bulat ke dalam variabel num_first
num_second = int(input("Masukkan angka kedua: "))     # memasukkan bilangan bulat ke dalam variabel num_second
operator = str(input("Pilih Operator ( + - * /  % ): "))         # memasukkan karakter ke dalam variabel operator
if operator == "+":            # test sebuah kondisi apakah isi dari operator = "+"          
    print(str(num_first) + " " + str(operator) + " " + str(num_second) + " = " + str(num_first + num_second))      # jika operator = "+" , maka angka pertama dan kedua akan ditambah
elif operator == "-":          # test sebuah kondisi apakah isi dari operator = "-"
    print(str(num_first) + " " + str(operator) + " " + str(num_second) + " = " + str(num_first - num_second))      # jika operator = "-" , maka angka pertama dan kedua akan dikurang
elif operator == "*":          # test sebuah kondisi apakah isi dari operator = "*"
    print(str(num_first) + " " + str(operator) + " " + str(num_second) + " = " + str(num_first * num_second))      # jika operator = "*" , maka angka pertama dan kedua akan dikali
elif operator == "/":          # test sebuah kondisi apakah isi dari operator = "/"
    print(str(num_first) + " " + str(operator) + " " + str(num_second) + " = " + str(num_first // num_second))     # jika operator = "/" , maka angka pertama dan kedua akan dibagi dan dibulatkan ke bawah
elif operator == "%":          # test sebuah kondisi apakah isi dari operator = "%"
    print(str(num_first) + " " + str(operator) + " " + str(num_second) + " = " + str(num_first % num_second))      # jika operator = "%" , maka angka pertama dan kedua akan diambil sisa baginya
else:
    print("Operator yang Anda masukkan salah, silahkan coba lagi...")   # error case jika input operator tidak termasuk list syarat