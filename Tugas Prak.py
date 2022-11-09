
print ("[1] Sapi Warrior : 690 hari")
print ("[2] Sapi Mage : 420 hari")
print ("[3] Sapi Assasin : 530 hari")
print ("[4] Sapi Nolep : 330 hari \n")

sapi_warrior = 690
sapi_mage = 420
sapi_assasin = 530
sapi_nolep = 330

entry = True

while entry == True :
    kode_sapi = int (input ("Masukkan kode sapi : "))
    jmlh_sapi = int (input ("Masukkan jumlah sapi : "))
    if kode_sapi == 1 :
        entry = False
        hasil = jmlh_sapi * sapi_warrior
        baru = input ("Apakah ingin menambahkan sapi lain ? [y]/[n] >> ")
        if baru == "n":
            entry = False
            break
        elif baru == "y":
            entry = True
    elif kode_sapi == 2 :
        hasil = jmlh_sapi * sapi_mage
        baru = input ("Apakah ingin menambahkan sapi lain ? [y]/[n] >> ")
        if baru == "n":
            entry = False
            break
        elif baru == "y":
            entry = True
    elif kode_sapi == 3 :
        hasil = jmlh_sapi * sapi_assasin
        baru = input ("Apakah ingin menambahkan sapi lain ? [y]/[n] >> ")
        if baru == "n":
            entry = False
            break
        elif baru == "y":
            entry = True
    elif kode_sapi == 4 :
        hasil = jmlh_sapi * sapi_nolep
        baru = input ("Apakah ingin menambahkan sapi lain ? [y]/[n] >> ")
        if baru == "n":
            entry1 = False
            break
        elif baru == "y":
            entry1 = True
jumlah = hasil
tahun = jumlah/365
x = jumlah % 365
bulan = x / 30
hari = x % 30
print ("Total waktunya", int(tahun),"Tahun", int(bulan), "Bulan", int(hari), "Hari" )
        