from ast import For


print ("Menampilkan Bilangan Genap")
number = int(input("Masukkan batas maksimum : "))

for x in range(number+1):
    if(x % 2 == 0 and x != 0):
        print(x)