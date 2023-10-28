sayi=int(input("Lütfen sayı giriniz:"))
toplam=0
print(sayi)

for i in range(1,sayi + 1):
    if sayi % i ==0:
        toplam=toplam+i
        
if toplam== sayi*2:
    print("girdiğiniz sayı mükemmel sayıdır.")
else:
    print("girdiğiniz sayı mükemmel sayı değildşir.")