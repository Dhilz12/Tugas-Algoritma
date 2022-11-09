#QUIZ ALGO
#NASYWA FADHIL DHIFULLAH (222410102038)



import random
angka = random.randint(0,100)
batas = 10 

while batas > 0 :
    jawaban = int(input("Angka telah tersedia, silahkan tebak >>>"))

    if jawaban < angka :
        batas -= 1
        print (f'Angka terlalu kecil, tersisa {batas} kesempatan lagi \n')
        continue
    elif jawaban > angka : 
        batas -= 1
        print (f'Angka terlalu besar, tersisa {batas} kesempatan lagi \n')
        continue
    else :
        batas -= 1 
        print (f'Selamat tebakanmu benar \n')
        break
if batas == 0 :
   print ("Anda kurang beruntung")
        
    