sayi=int(input("sayı giriniz:"))
asalSayi=True

for i in range(2,sayi):
    if sayi%i==0:
        asalSayi=False
    
if asalSayi==True:
    print("sayı asaldır")
else:
    print("sayı asal değilidr:")