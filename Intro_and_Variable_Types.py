# Basic Syntax
print("Hello World")
print("Hello \nWorld!")

# Quotation in Python
a = 'Python'
b = " Programming"
c = """ is so freaking easy"""
sentence = a+b+c
print(sentence)

# Multiple Statement in a single line
x = "5"; y = " balon"; print(x+y)

# Parameters
tipe_data = ["Boolean","Float","Integer","String"] 
print(tipe_data)
tipe_data = '\n'.join(tipe_data)
print("List setelah menggunakan .join untuk setiap item list:\n", tipe_data)

# Data Types
nama = "ibe"
type(nama)
suhu = -99
type(suhu)
suhu_matahari = 1000000000
type(suhu_matahari)
suhu_kutub = -4.6
type(suhu_kutub)
ibe_ganteng = TRUE
type(ibe_ganteng)
ibe_jelek = FALSE
type(ibe_jelek)

# Assigning Value to Variable
iphone7 = 2500000 # Automatically Integer
Laptop = input("Masukkan harga laptop:") # Automatically String even the value is number
  # >
 type(Laptop)
Sensors = int(input("Masukkan harga sensor-sensor: ")
              # >
type(Sensors)
mouse = 125000; type(mouse)
headphone = 250000.0; type(headphone)
Kopi_SBUX = "Mahal Banget Ngab"; type(kopi_SBUX)

# Multiple Assignment
a,b,c = 69,68,67
x = y = z = 38000

# Standart Data Types
# There are several data types: Number, String, List, Tuple, Dictionary
# Number Consist of int, float, and complex
              
# Python String
sedotan = "Panjang Banget huehuehue "
print(sedotan)  # Print complete List / sentence
print(sedotan[0]) # Print 1st index of List (1st char)
print(sedotan[4:9])
print(sedotan[7:])
print(sedotan[:12])
print(sedotan[-1])
print(sedotan + "dan bahannya stainless skill xixixi") 
print(sedotan*2)

print("Nama gue %s umur gue %d" % ("siapa dah", 23))

      
# Python List
# Python Lists are similar to arrays in C programming
# all items can be different data type and can be updated
contoh_list = ["bisa string", 20, 90.0, True,'john', 'mayer']
print(contoh_list)
print(contoh_list[0]) # Print first list
print(contoh_list[2:5])
print(contoh_list[:4])
print(contoh_list[2:])
print(contoh_list*2)
print(contoh_list[-1])
      
# Python Tuple
# Just like list but can not be updated/changed
Contoh_Tuple  = ("Contoh tuple", 20, 9.0, False)
print(Contoh_Tuple)
# sisanya kayak list dan string, gue males ngetiknya hehe

      
# Python Dictionary
dict = {}
print(dict)
dict['satu'] = "This is one's value"
dict[2] = "This is two's value"
print(dict)
print(dict.values())
print(dict.keys())
print(dict['satu']) # Print dict one's value
print(dict['2'])
Big_dict = {'nama' = "Johny Deep"; "code" = 6969; 'dept' = "Videos Engineer"}
      
# Example Dictionary
mobil = {'nama' = 'Deep'; 'harga' = 300000000; 'diskon' = 2000000}
motor = {'nama' = 'KLZ'; 'harga' = 30000000; 'diskon' = 1000000}
sepeda = {'nama' = 'Polyglot' = 3000000;  'diskon' = 200000} 
harga_mobil = mobil['harga'] - mobil['diskon']
harga_motor = motor['harga'] - motor['diskon']
harga_sepeda = sepeda['harga'] - sepeda['diskon']
total_harga = harga_motor + harga_mobil + harga_sepeda
total_pajak = total_harga * 0.05
print(total_harga + total_pajak)
      
# Python Set
contoh_set = {"baju", "kaos", "sempak", "celana"} # Mutable
contoh_frozen_set = ({"gope","seceng","goceng"}) # Immutable
             
# Data Conversion
Duit = "Goceng"
in_number = 5000
print(Duit + in_number) # Error
print(Duit + str(number)) # Change it to string

# Variable Global dan Lokal
# Lokal
x = 911
print(x)
def sebuah_fungsi():
      # global x
      x = "telpon polisi"
      print(x)
sebuah_fungsi()
print(x)

# Global
x = 911
print(x)
def sebuah_fungsi():
      global x
      x = "telpon polisi"
      print(x)
sebuah_fungsi()
print(x)      
      
# Delete Variable 
_easting = 213891
print(_easting)
del(_easting)
print(_easting)
