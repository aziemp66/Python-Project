
print("program hitung gaji karyawan")
print("------------------------------")
nama = input("nama pegawai       : ")
gol =input("golongan           : ")
jamKerja = int(input("total jam kerja    : "))
print("------------------------------")

if jamKerja > 200:
    waktuLembur = jamKerja-200
else:
    waktuLembur = 0


if gol.upper() == "A":
    gajiPokok = 500000
    tunjangan = 0.1 * gajiPokok
    lembur = waktuLembur*5000
elif gol.upper() == "B" :
    gajiPokok = 700000
    tunjangan = 0.15 * gajiPokok
    lembur = waktuLembur*7500
elif gol.upper() == "C":
    gajiPokok = 900000
    tunjangan = 0.2 * gajiPokok
    lembur = waktuLembur*10000
else :
    print("Input golongan anda salah, silahkan coba lagi")


gajiTotal = gajiPokok + tunjangan + lembur

print("Perhitungan gaji")
print("------------------------------")
print("GAJI POKOK       = Rp." ,gajiPokok)
print("tunjangan        = Rp." ,tunjangan)
print("Lembur           = Rp." ,lembur)
print("------------------------------")
print("Total           = Rp." ,gajiTotal)