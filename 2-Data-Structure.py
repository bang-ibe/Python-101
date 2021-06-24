#           LIST
# CONCEPT: anything inside [ ] is a f*cking List
x = 5
x # print x

x = []
x

x = [1, 2.0, "halo", True]
x
       
x = [1,2,3,4,5]
x
x + [6,7,8,9,10]  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x                 # akan tetap [1,2,3,4,5]
x.append(6) 
x                 # [1,2,3,4,5,6,...] and so on 
del(x[5:6])
x
x.extend([6,7,8,9,10])
x                  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del(x[5:10])
x
len(x) 
x.index(4) 
x.insert(1,"halo") # insert to the 2nd index
x
del x[1]
x
x.extend([6,7,8,9,10])
x
del x[7:10]
x
del x[5:]
x
x[3]               # Calling Value
x.pop(3)           # delete the 4th index
x
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x
y = x
y
y = x[4:8]
y
y.clear()
y
x


#           TUPLE
#   just like List but can't be changed
tup = ("a", "b", "c", "d", "e")
tup 
tup[1] = "hi there :)"        # - SyntaxError
                              # cannot assign to function call
tup.append["halloo"]          # - AttributeError
                              # 'tuple' object has no attribute 'append
tup = (1,2,3,3,4,2,5,5,4,6)
tup[6]                        # Calling Value
tup[-1]                       # Backward
tup[-2]


#               DICTIONARY
# keys is a single value, can be tuple,int, str
# keys should be different with one and another
directory = {}
directory
directory = {1: "PIC", 2: "Atmega", 3: "Raspberry Pi", 4: "Arduino"}
directory
directory.keys()
directory.values()
print(directory.keys())
print(*directory.keys())
print([*directory.keys()])      # Change keys into a list
print([*directory.values()])
print([*directory.items()])
directory([3])                  # TypeError: 
                                # 'dict' object is not callable
directory.get(3)                # Calling a value

directory[2] = "Arduino Nano"
print([*directory.items()]


# Menggabungkan list jadi dictionary
x = [1,"y","z"]
y = ["satu","dua","tiga"]
z = dict(zip(x,y)) 
z


# Study Case
jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = {'harga_harian': 1000000, 'total_hari':15 } 
cleansing = {'harga_harian': 1500000, 'total_hari':10 } 
integration = {'harga_harian':2000000, 'total_hari':15 } 
transform = {'harga_harian':2500000, 'total_hari':10 }
sub_warehousing = warehousing['harga_harian']*warehousing['total_hari'] 
sub_cleansing = cleansing['harga_harian']*cleansing['total_hari'] 
sub_integration = integration['harga_harian']*integration['total_hari'] 
sub_transform = transform['harga_harian']*transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
if jam > 19:
    print("Selamat malam, anda harus membayar tagihan sebesar:")
elif jam >17:
    print("Selamat sore, anda harus membayar tagihan sebesar:") 
elif jam > 12:
    print("Selamat siang, anda harus membayar tagihan sebesar:")
else:
    print("Selamat pagi, anda harus membayar tagihan sebesar:") 
print(total_harga)


# CONCLUSION
# -List can be added to a list
# -Several methodes that can be used: 
#  .extend([...,...]), .index(...), .append(...), .pop(...), insert(...,...)
# .clear(...), *get(...)
