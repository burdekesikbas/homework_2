sayi1 = int(input("Lütfen bir sayı giriniz:"))

sayi2 = int(input("Lütfen bir sayı giriniz:"))

sayi3= int(input("Lütfen bir sayı giriniz:"))


if sayi1>sayi2:
    buyukSayi = sayi1
elif sayi3>sayi1:
    buyukSayi = sayi3
else:
    buyukSayi = sayi2
    
    
print("En büyük sayı : " + str(buyukSayi))
    
