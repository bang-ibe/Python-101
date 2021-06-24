#------------FUNCTION-----------
#salah satu contoh function bawaan adalah str

def contoh():
    print("hallo")    
contoh() #Panggil function

def nama():
    print("ibe ganteng")
def angka():
    print("88")
nama()

def jumlah(x,y): #Menggunakan Argumen
    z = x + y
    print(z)

def kurang(x,y):   
    z = x - y
    print(z)

def kali(x,y):   
    z = x*y
    print(z)

def bagi(x,y):   
    z = x/y
    print(z)

kali(10,69)

#GLOBAL VS LOCAL VARIABLE
#local
def var():
    a=100
    print(a)
var()

#global
n = 900
def varx():
    global n 
    n=100
    print(n)
varx()

#Penggunaan Return agar Z bisa dipanggil 
# di luar Function
def jumlah(x,y): #Menggunakan Argumen
    z = x +y
    print(z)
    return z

def kurang(x,y):   
    z = x-y
    print(z)
    return z

def kali(x,y):   
    z = x*y
    print(z)
    return z

def bagi(x,y):   
    z = x/y
    print(z)
    return z

output = jumlah(10,29)
print(output) 

#---------------METHOD-----------------
a = [8213092190,320918,12093812,901238]
a.sort() # Mengurutkan terkecil ke besar
print(a)
  
class contoh:
    def nama():
        print("Geosoftware")
    def angka():
        print("Angka") 
contoh.nama()
contoh.angka()

class calculator:
    def jumlah(self, x,y): #Menggunakan Self, cari tau coba
        z = x +y
        print(z)
        return z

    def kurang(self, x,y):   
        z = x-y
        print(z)
        return z

    def kali(self,x,y):   
        z = x*y
        print(z)
        return z

    def bagi(self,x,y):   
        z = x/y
        print(z)
        return z
calculator.kali(10,90)
operasi = calculator()
operasi.kali(69, 99)

class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def jumlah(self): #Menggunakan Self, cari tau coba
        z = self.x + self.y
        print(z)
        return z

    def kurang(self):   
        z = self.x - self.y
        print(z)
        return z

    def kali(self):   
        z = self.x*self.y
        print(z)
        return z

    def bagi(self):   
        z = self.x/self.y
        print(z)
        return z

operasi = calculator()
operasi.kali(90,8) #not working, shouldn't has any argument
#the argument should be in cal()
