#               WHILE Statement
 
print ("adios!")

# The Infinite Loop
# use ctrl + c or ctrl + x
var = 1
while var == 1:
    input("Input the number: ")
    # >
print ("adios")

# Else Statement with while loop
count = 0
while count<5:
    print(count, "kurang dari 5")
    count += 1
else:
    print(count,"tidak kurang dari lima")

# Single Statement Suites
# infinite loop, use ctrl+c
flag = 1
while (flag):
    print("given flag is really true")
print("Goodbye")

# Range
range(11) 
list(range(11))
list(range(1,11,2))
list(range(0,11,2))
list(range(10,0,-1)) 
tuple(range(1,11))
set(range(110))

# FOR LOOP Statement
# used for list and string
range(5)
print(range)
list = range(5)
print(list)
for var in list:
    print(var)

for a in 'Python': 
    print("current letter is: ", a)
print("adios")

# Iterating by Sequence Index
fruits = ['banana', 'wotahmelon', 'mango']
for index in range(len(fruits)):
    print("current fruit", fruits[index])
print("done")

# Else statement with for loop
numbers = [1,3,4,212,1,21312,32445,232,67567,455,43,9790]
for num in numbers:
    if num%2 == 0:
        print("the list contain an even number")
        break
    else:
        print("the list does not contain even number")

# Nested loops
import sys  
for i in range(1,11):       # Masih belom paham
    for j in range (1,11):
        k = i*j
        print(k, end = " ")
    print()

# Break Statement
for letter in 'Python': # First Example
    if letter == 'h':
        break
    print ('Current Letter :', letter)

var = 10 # Second Example
while var > 0:
    print ('Current variable value :', var)
    var -= 1 # var = var - 1
    if var == 5:
        break
print ("Good bye!")

x = int(input("any number: "))

numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num==x:
        print ('number found in list')
        break
    else:
        print ('number not found in list')

# Continue Statement
for letter in 'Python': # First Example
    if letter == 'h':
        continue
    print ('Current Letter :', letter)
    
var = 10 # Second Example
while var > 0:
    var = var -1
    if var == 5:
        continue
    print ('Current variable value :', var)
print ("Good bye!")

# Pass Statement
for letter in 'Python':
    if letter == 'h':
        pass
        print ('This is pass block')
    print ('Current Letter :', letter)
print ("Good bye!")

# Iterator and Generator
# iter using iter()
# generator using #next()
list=[1,2,3,4]
it = iter(list) #           this builds an iterator object
print (next(it)) #          prints next available element in iterator
#                           Iterator object can be traversed using
#                            regular for statement 
# !usr/bin/python3
for x in it:
    print (x, end=" ")
#                               or using next() function
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit() #you have to import sys module for this


import sys
from builtins import list
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()


for x in range (3,8,2):
    print(x)



#example
# Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]
# Tanpa menggunakan while loop
total_tagihan = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] + tagihan[4] 
print(total_tagihan)
# Dengan menggunakan while loop
i = 0 # sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan) # panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0 # mula-mula, set total_tagihan ke 0
while i < jumlah_tagihan: # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] # tambahkan tagihan[i] ke total_tagihan
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.
print(total_tagihan)


tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] < 0:
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
    i += i
print(total_tagihan)


tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke tagihan berikutnya
    if tagihan[i] < 0:
        i += 1
        continue
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)


list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)



list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan
print(total_tagihan)



list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran) 
print(total_pemasukan)



# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
# Pengecekan kendaraan dengan nomor pelat ganjil atau genap 
# Deklarasikan kendaraan_genap dan kendaraan_ganjil = 0
kendaraan_genap = 0 
kendaraan_ganjil = 0
for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1 
    else:
        kendaraan_ganjil += 1
# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil 
# dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0
while i <= jumlah_hari:
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    else:
    	total_pengeluaran += (kendaraan_ganjil * uang_jalan) 
    i += 1
# Cetak total pengeluaran
print(total_pengeluaran) 
