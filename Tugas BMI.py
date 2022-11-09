nama = (input("Masukkan nama :"))
a = int (input("Masukkan berat badan (kg)  :" ))
b = int (input("Masukkan tinggi badan (cm) :"))

#Konversi tinggi badan ke meter

c = (b / 100)

#Rumus BMI = berat badan (kg) / (tinggi badan (kg))^2

nilai = a / (c ** 2)
nilai2 = float(round(nilai, 2))

if nilai <= 18.5 :
    print ("============================")
    print ("Nilai BMI", nama, nilai2,". Anda sekarang Underweight")
elif nilai > 18.5 and nilai < 24.9:
    print ("============================")
    print ("Nilai BMI", nama , nilai2,". Anda sekarang Normalweight")
elif nilai > 25.0 and nilai < 29.9 :
    print ("============================")
    print ("Nilai BMI", nama,  nilai2,"Anda sekarang Overweight")
elif nilai > 30.0 and nilai < 34.9:
    print ("============================")
    print ("Nilai BMI", nama, nilai2,". Anda sekarang Obesity class I")
elif nilai > 35.0 and nilai < 39.9 :
    print ("============================")
    print ("Nilai BMI", nama, nilai2,"Anda sekarang Obesity class II")
else:
    print ("============================")
    print ("Nilai BMI", nama, nilai2,"Anda sekarang Obesity class III")

