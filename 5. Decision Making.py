#               DECISION MAKING

# IF Statement
if True:                        #always True
    print("Benar!")
else:
    print("Salah")
print("sampai jumpa!")

var1 = 300                      # Anything >0 is always True
if var1:
    print("%d is var1's value" %(var1))
var2 = 0                        # Boolean False
if var2:
    print ("2 - Got a true expression value")
    print (var2)
else:
    print("False")
print ("Good bye!")

# IF ELSE
jumlah  = int(input("masukkan jumlah: "))
#>
diskon = 0
if jumlah<1000:
    diskon = jumlah *0.5
    #net = jumlah-diskon
    print("diskon ", diskon)
else:
    diskon = jumlah * 0.10
    print("diskon ", diskon)
print("Yang harus dibayarkan: ", jumlah - diskon)


# ELIF Statement
jumlah  = int(input("masukkan jumlah: "))
# >
diskon = 0
if jumlah<1000:
    diskon = jumlah *0.5
                                # net = jumlah-diskon
    print("diskon ", diskon)
elif jumlah<5000:               # coba tambah and or &&
    diskon = jumlah * 0.25
    print("diskon ", diskon)
else:
    diskon = jumlah * 0.10
    print("diskon ", diskon)
print("Yang harus dibayarkan: ", jumlah - diskon)

x = "Hassan"
if x == "Salman":
    print("Halo Salman!")
elif x == "Hassan":
    print("Hallo Hassan")
else: 
    print("Hallo Ngab!")


# Nested IF
num = int(input("masukkan angka: "))
# >
if num%2==0:
    if num%3:
        print("dapat dibagi 3 dan 2")
    else:
        print("Tidak dapat dibagi 3 dan dapat dibagi 2")
else:
    if num%3==0:
        print("dapat dibagi 3 tapi tidak dengan 2")
    else:
        print("tidak dapat dibagi 2 dan 3")

uang = 18000
if uang >= 20000:
    print("Sop Buntut")
    sisa = uang - 20000
    print("Sisa uang: ", sisa)
elif uang >= 10000:
    print("Nasi Goreng")
    if uang >= 15000:
        print("dengan ati ampela")
        sisa = uang - 15000
        print("Sisa uang: ", sisa)
    else:
        print("Tanpa ati ampela")
        sisa = uang - 10000
        print("Sisa uang: ", sisa)
elif uang >= 5000:
    print("gorengan")
    sisa = uang - 5000
    print("sisa uang: ", sisa)
else:
    print("Gaada duit")
   

# Single Statement Suite
varr = 100
if (varr == 100): print("value expression is 100")
print ("goodbye")

# Study Case
ph = 5
temp = 50
x1, x2, x3 = "Acid", "lighthly", "Neutral"
y1, y2, y3 = "coldspring", "Warmspring", "Hotspring"

if type(ph) != int or type(temp) != int:
    print("Masukkan nilai ph dan temperatur dengan data integer.")
else:
    if ph < 0 or temp <0 or ph >8 or temp >100:
        print("Masukkan nilai PH diantara 0-8 dan nilai temperatur diantara 0-100")
    else :
        if temp >80:
            if ph >6:
                jenis = x3 +" "+y1
            elif ph>=4:
                jenis  = x2 +" "+y1
            else:
                jenis = x1+" "+y1
        elif temp>40:
            if ph >6:
                jenis = x3 +" "+y2
            elif ph>=4:
                jenis  = x2 +" "+y2
            else:
                jenis = x1+" "+y2
        else:
            if ph >6:
                jenis = x3 +" "+y3 
            elif ph>=4:
                jenis  = x2 +" "+y3
            else:
                jenis = x1+" "+y3
        print(jenis)


jam = 13
if jam >= 5 and jam < 12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam <17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam <19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")
