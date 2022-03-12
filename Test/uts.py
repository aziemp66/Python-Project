print("program hitung gaji karyawan")
print("------------------------------")
nama = input("nama pegawai       :")
golongan =input("golongan           :")
totaljamkerja = int(input("total jam kerja    :"))
print("------------------------------")
if totaljamkerja >= 200:
    if golongan == "A":
        jamlembur=totaljamkerja-200
        lembur=jamlembur*5000
    elif golongan == "B":
        jamlembur=totaljamkerja-200
        lembur=jamlembur*7500
    elif golongan == "C":
        jamlembur=totaljamkerja-200
        lembur=jamlembur*10000
    

if golongan == "A":
    gaji_pokok=500000
    tunjangan=10/100 * 500000
elif golongan == "B":
    gaji_pokok=700000
    tunjangan=15/100 * 700000
elif golongan == "C":
    gaji_pokok=900000
    tunjangan=20/100 * 900000

totalgaji=gaji_pokok+tunjangan+lembur

print("Perhitungan gaji")
print("------------------------------")
print("GAJI POKOK       = Rp." ,gaji_pokok)
print("tunjangan        = Rp." ,tunjangan)
print("Lembur           = Rp." ,lembur)
print("------------------------------")
print("Total           = Rp." ,totalgaji)